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

# Validation Name Function
# ---------------------------------
# The name must contain at least 3 characters.
# Return True if the name is valid, otherwise return False.
def validate_name(name: str) -> bool:
    """
    Checks if the name contains at least 3 characters.
    Args:
        name (string): Original string value.
    Returns:
        valid_name (bool): True if name contains at least 3 characters.
    """
    valid_name = len(name) >= 3
    return valid_name


# Validation Email Function
# ---------------------------------
# The email must contain both "@" and ".".
# Return True if the email format is valid, otherwise return False.
def validate_email(email: str) -> bool:
    """
    Checks if the email contains "@" and ".".
        Args:
            email (string): Original string value.
        Returns:
            valid_email (bool): True if email contains "@" and ".".
    """
    valid_email = "@" in email and "." in email
    return valid_email

