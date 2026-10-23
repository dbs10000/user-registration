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




# # ---------------------------------
# # MAIN Validation Function
# # ---------------------------------
def validate_user_data(name: str, email: str, password: str) -> bool:
    """
    This is an Orchestrator Function.
    ---------------------------------
    It calls:
    - validate_name(name)
    - validate_email(email)
    - validate_password(password)

    It checks if all three functions return True in order to validate the users data.
    Otherwise it will return ValueError statements and False.

    Args:
        name   (string): Original string value
        email   (string): Original string value
        password (string): Original string value

    Returns:
        ValueErrors (string): Descriptive error messages if the data is not valid.
        True (boolean): If all user data is valid.
        False (boolean): If any user data is invalid.
    """

    # Name Validator
    if not validate_name(name):
        print("ValueError: Your name must contain at least 3 characters.")

    # Email Validator
    if not validate_email(email):
        print("ValueError: Your email must contain both '@' and '.' for it to be valid.")

    # Password Validator
    if not validate_password(password):
        print("ValueError: Your password must be at least 8 characters long. Contains at least one uppercase letter. Contains at least one digit")
    
    # Return True if all user data is valid, else False 
    return all([validate_name(name), validate_email(email), validate_password(password)])



# # ---------------------------------
# # Registration Function
# # ---------------------------------
# def create_user_account(name: str, email: str, password: str) -> dict:

#     # Validates the inputs
#     if validate_user_data(name, email, password):
#         user = {"name" : name, "email" : email, "password" : password}
   
#         # Checks whether the email already exists in registered_users list.
#         if email in registered_users:
#             print("ValueError: Email already exists in Registered Users")
#             user["error message"] = "ValueError: Email already exists in Registered Users"
#             failed_registrations.append(user)
#             return None
#         else:
#             user["status"] = "active"
#             registered_users.append(user)
#             return user



# NEW CODE BUT STILL NOT RIGHT
# # ---------------------------------
# def create_user_account(name: str, email: str, password: str) -> dict:

#     is_valid_user = validate_user_data(name, email, password)

#     user = {
#         "name" : name,
#         "email" : email,
#         "password" : password,
#     }

#     for user in registered_users:
#         if email in user["email"]:
#                 print("ValueError: Email already exists in Registered Users")
#                 user["error message"] = "ValueError: Email already exists"
#                 failed_registrations.append(user)

#     if is_valid_user:
#         print(f"is_valid_user :{is_valid_user}")
#         user["status"] = "active"
#         registered_users.append(user)

#     else:
#         print(f"is_valid_user :{is_valid_user}")
#         user["error message"] = "ValueError: Invalid data"
#         failed_registrations.append(user)








# # ---------------------------------
# # TESTING
# # ---------------------------------

# # Valid Registration
# # ---------------------------------
name = "Dylan"
email = "dylan@gmail.com"
password = "Password123"

print()
print(f"Created User:\n{create_user_account(name, email, password)}")
print()
print(f"Registered Users:\n{registered_users}")
print()
print(f"Failed Registrations:\n{failed_registrations}")

# # Duplicate Registration
# # ---------------------------------
name = "Dy"
email = "dylan@gmail.com"
password = "Password123"

print()
print(f"Created User:\n{create_user_account(name, email, password)}")
print()
print(f"Registered Users:\n{registered_users}")
print()
print(f"Failed Registrations:\n{failed_registrations}")