# ===============================================================
# Secure User Registration System
# ---------------------------------
# A small user registration system.
# 
# ===============================================================



# ---------------------------------
# Database Simulation
# ---------------------------------
registered_users = []
failed_registrations = []


# ---------------------------------
# Validation Functions
# ---------------------------------

# Validate Name Function
# ---------------------------------
# The name must contain at least 3 characters.
# Return True if the name is valid, otherwise return False.
def validate_name(name: str) -> bool:
    """
    Checks if the name contains at least 3 characters.
    Args:
        name (string): Original string value.
    Returns:
        is_valid_name (bool): True if name contains at least 3 characters.
    """
    is_valid_name = len(name) >= 3
    return is_valid_name


# Validate Email Function
# ---------------------------------
# The email must contain both "@" and ".".
# Return True if the email format is valid, otherwise return False.
def validate_email(email: str) -> bool:
    """
    Checks if the email contains "@" and ".".
    Args:
        email (string): Original string value.
    Returns:
        is_valid_email (bool): True if email contains "@" and ".".
    """
    is_valid_email = "@" in email and "." in email
    return is_valid_email


# Validate Password Function
# ---------------------------------
# The password must meet all of the following conditions:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one digit
# Return True if the password is valid, otherwise return False.
def validate_password(password: str) -> bool:
    """
    Checks if the password meets the following conditions:
        - Is at least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one digit
    Args:
        password (string): Original string value.
    Returns:
        is_valid_password (bool): True if password meets all three conditions.
    """ 
    valid_length = len(password) >= 8
    has_digit = not password.isalpha()
    has_uppercase = (not password == password.lower())
    is_valid_password = all([valid_length, has_digit, has_uppercase])
    return is_valid_password

