class ErrorMessages:
    """ Contains all the error messages used in the application. """
    USERNAME_REQUIRED_ERROR = "Epic sadface: Username is required"
    PASSWORD_REQUIRED_ERROR = "Epic sadface: Password is required"
    INVALID_CREDENTIALS_ERROR = "Epic sadface: Username and password do not match any user in this service"
    USER_LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."

    INVENTORY_ACCESS_DENIED_ERROR = "Epic sadface: You can only access '/inventory.html' when you are logged in."
    CART_ACCESS_DENIED_ERROR = "Epic sadface: You can only access '/cart.html' when you are logged in."
    CHECKOUT_STEP1_ACCESS_DENIED_ERROR = "Epic sadface: You can only access '/checkout-step-one.html' when you are logged in."
    CHECKOUT_STEP2_ACCESS_DENIED_ERROR = "Epic sadface: You can only access '/checkout-step-two.html' when you are logged in."
    CHECKOUT_STEP3_ACCESS_DENIED_ERROR = "Epic sadface: You can only access '/checkout-complete.html' when you are logged in."

    FIRST_NAME_REQUIRED_ERROR = "Error: First Name is required"
    LAST_NAME_REQUIRED_ERROR = "Error: Last Name is required"
    ZIP_CODE_REQUIRED_ERROR = "Error: Postal Code is required"
