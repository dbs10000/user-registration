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
        name (str): The users name.
    Returns:
        is_valid_name (bool): True if name contains at least 3 characters.
    """
    is_valid_name = len(name) >= 3
    return is_valid_name


# Validate Email Function
# ---------------------------------
def validate_email(email: str) -> bool:
    """
    Checks if the email contains both "@" and ".".
    Args:
        email (string): The users email address.
    Returns:
        is_valid_email (bool): True if email contains both "@" and ".".
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
        password (str): The users password.
    Returns:
        is_valid_password (bool): True if password meets all three conditions.
    """ 
    valid_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    is_valid_password = all([valid_length, has_digit, has_uppercase])
    return is_valid_password




# ---------------------------------
# MAIN Validation Function
# ---------------------------------
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



# ---------------------------------
# Registration Function
# ---------------------------------
def create_user_account(name: str, email: str, password: str) -> dict:
    """
    This function checks if a user is valid and can be added to the registered user list.

    If the users information is invalid, or their email already exists inside the registered users list, they will get put into the failed registration list along with a error message.

    Args:
        name (str): The users name.
        email (str): The users email.
        password (str): The users password.
    Returns:
        new_user (dict): If the user registration is valid.
        None (None): If the user fails the registration.
    """
    # Checks if user data is valid
    is_valid_user = validate_user_data(name, email, password)

    # If the user data is not valid
    if not is_valid_user:
        print("ValueError: Users information is invalid")
        value_error_user = "ValueError: Users information is invalid"
        invalid_user = {
            "name": name,
            "email" : email,
            "password" : password,
            "error message" : value_error_user
        }
        failed_registrations.append(invalid_user)
        
    
    elif is_valid_user:
        # Checks if an email already exists
        is_duplicate_email = any(email == user["email"] for user in registered_users)

        if is_duplicate_email:
            value_error = "ValueError: Email already exists in Registered Users"
            invalid_user = {
                "name": name,
                "email" : email,
                "password" : password,
                "error message" : value_error
            }
            failed_registrations.append(invalid_user)

        if not is_duplicate_email:
            new_user = {
                "name": name,
                "email" : email,
                "password" : password,
                "status" : "active"
            }
            registered_users.append(new_user)
            return new_user
        


# ---------------------------------
# TESTING
# ---------------------------------
thick_line_break = "=" * 30
thin_line_break = "-" * 30

# Valid Registration
# ---------------------------------
name = "Dylan"
email = "dylan@gmail.com"
password = "Password123"
user = create_user_account(name, email, password)

print()
print(thick_line_break)
print("valid registration test".upper())
print(thick_line_break)
print("User:".upper(), user)
print(thin_line_break)
print("registered users".upper())
print(thin_line_break)
print(registered_users)
print(thin_line_break)
print("failed_registrations".upper())
print(thin_line_break)
print(failed_registrations)
print(thin_line_break)
print()


# Duplicate Email
# ---------------------------------
name = "Dylan"
email = "dylan@gmail.com"
password = "Password123"

user = create_user_account(name, email, password)

print()
print(thick_line_break)
print("duplicate email test".upper())
print(thick_line_break)
print("User:".upper(), user)
print(thin_line_break)
print("registered users".upper())
print(thin_line_break)
print(registered_users)
print(thin_line_break)
print("failed_registrations".upper())
print(thin_line_break)
print(failed_registrations)
print(thin_line_break)
print()



# Invalid Name
# ---------------------------------
name = "Jo"
email = "jo@hotmail.com"
password = "He11oHi3"

user = create_user_account(name, email, password)

print()
print(thick_line_break)
print("invalid name test".upper())
print(thick_line_break)
print("User:".upper(), user)
print(thin_line_break)
print("registered users".upper())
print(thin_line_break)
print(registered_users)
print(thin_line_break)
print("failed_registrations".upper())
print(thin_line_break)
print(failed_registrations)
print(thin_line_break)
print()


# Invalid Email
# ---------------------------------
name = "Sara"
email = "saraoutlook.com"
password = "SaraJl4dd9"

user = create_user_account(name, email, password)

print()
print(thick_line_break)
print("invalid email test".upper())
print(thick_line_break)
print("User:".upper(), user)
print(thin_line_break)
print("registered users".upper())
print(thin_line_break)
print(registered_users)
print(thin_line_break)
print("failed_registrations".upper())
print(thin_line_break)
print(failed_registrations)
print(thin_line_break)
print()


# Invalid Password
# ---------------------------------
name = "Jeremy"
email = "jeremy@bt-internet.com"
password = "hello"

user = create_user_account(name, email, password)

print()
print(thick_line_break)
print("invalid password test".upper())
print(thick_line_break)
print("User:".upper(), user)
print(thin_line_break)
print("registered users".upper())
print(thin_line_break)
print(registered_users)
print(thin_line_break)
print("failed_registrations".upper())
print(thin_line_break)
print(failed_registrations)
print(thin_line_break)
print()