from ..connection import get_database
from ...models.user import User
from bson import ObjectId

db = get_database()
users_collection = db["users"]


async def create_user(user: User):
    """
    Creates a new user in the users collection.

    Parameters:
    user (User): The user object to be created.

    Returns:
    User: The created User object with the assigned ID.

    Raises:
    Exception: If the creation process fails.
    """
    try:
        user_dict = user.dict()
        result = await users_collection.insert_one(user_dict)
        user.id = str(result.inserted_id)
        await users_collection.update_one({'_id': result.inserted_id}, {'$set': {'id': user.id}})
        return user
    except Exception as e:
        raise Exception(f"An error occurred while creating the user: {str(e)}")


async def get_user_by_id(user_id: ObjectId) -> User:
    """
    Retrieves a user from the users collection based on the provided user ID.

    Parameters:
    user_id (ObjectId): The unique identifier of the user.

    Returns:
    User: A User object if the user is found, otherwise None.

    Raises:
    Exception: If the retrieval process fails or no user is found with the provided ID.
    """
    user_data = await users_collection.find_one({"_id": user_id})
    return User(**user_data) if user_data else None


async def update_user(user_id: ObjectId, user: User):
    """
    Update user details in the database.

    Args:
        user_id (ObjectId): The unique identifier of the user to be updated.
        user (User): An instance of the User model containing the updated user details.

    Returns:
        Optional[User]: If the update operation is successful and the user details are modified,
                        returns the updated user instance.
                        If the user with the specified user_id does not exist in the database,
                        or if the update operation fails for any reason, returns None.

    Raises:
        Any exceptions raised during the update operation will be propagated to the caller.
    """
    result = await users_collection.update_one({"_id": user_id}, {"$set": user.dict()})
    if result.modified_count == 1:
        return user
    else:
        return None


from bson import ObjectId


async def delete_user(user_id: ObjectId):
    """
    Deletes a user from the users collection in the database based on the provided user ID.

    Parameters:
    user_id (ObjectId): The unique identifier of the user to be deleted.

    Returns:
    None

    Raises:
    Exception: If the deletion process fails.
    """
    try:
        result = await users_collection.delete_one({"_id": user_id})
        if result.deleted_count == 0:
            raise Exception(f"No user found with ID: {user_id}")
    except Exception as e:
        raise Exception(f"An error occurred while deleting the user: {str(e)}")


async def find_user_by_credentials(username: str, password: str) -> User:
    """
    Finds a user in the users collection based on the provided username and password.

    Parameters:
    username (str): The username of the user.
    password (str): The password of the user.

    Returns:
    User: A User object if the user is found, otherwise None.

    Raises:
    Exception: If the retrieval process fails.
    """
    user_data = await users_collection.find_one({"name": username, "password": password})
    return User(**user_data) if user_data else None
