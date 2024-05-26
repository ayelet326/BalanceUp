from pydantic import BaseModel, ValidationError, EmailStr, constr
from typing import Optional
import re


class User(BaseModel):
    id: int
    name: str
    password: str
    email: Optional[EmailStr]
    phone: Optional[str]  # Define phone as Optional[str]
    current_balance: float

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
