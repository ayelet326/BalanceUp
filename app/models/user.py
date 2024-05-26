from pydantic import BaseModel, ValidationError, EmailStr, constr, Field
from typing import Optional
import re


class User(BaseModel):
    id: int
    name: constr(min_length=3, max_length=8)
    password: constr(min_length=8, max_length=10)
    email: Optional[EmailStr]
    phone: Optional[str]
    current_balance: float

    @Field
    def name(cls, v):
        if not v.isalpha():
            raise ValueError('Name must contain only English letters')

    @Field
    def password(cls, v):
        if not (8 <= len(v) <= 10):
            raise ValueError('Password must be between 8 and 10 characters long')

    def validate_email(self):
        if self.email and not self.email.endswith('@example.com'):
            raise ValueError("Email must end with '@example.com'")

    def validate_phone(self):
        phone_regex = r'^\+?1?\d{9,15}$'
        if self.phone and not re.match(phone_regex, self.phone):
            raise ValueError("Invalid phone number format")

    def is_valid_user(self):
        try:
            self.validate_email()
            self.validate_phone()
            self.validate()
            return True
        except ValidationError:
            return False
