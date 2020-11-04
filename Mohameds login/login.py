# Milos and Mohammadreza Partow
def generate_login():
    """
    the function takes three parameters (first name, last name and BCIT ID), and returns the default login password.
    """
    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name:"))
    bcit_id = str(input("Enter your BCIT ID: "))

    f_name = first_name.capitalize()  # the first character is upper case and the rest of the name is lowercase.
    l_name = last_name.capitalize()  # the first character is upper case and the rest of the name is lowercase.

    print("Your login is %s%s%s" % (f_name[:3], l_name[:3], bcit_id[-3:]))
    return


def change_password():
    """
    The function will prompt the user to enter a new password, if the password meets the specifications,
    the loop terminates and the password will be returned otherwise a message including
    the password specifications and a request to enter another password will be displayed and
    the user will be prompted to enter another password.
    """
    while True:
        password = input("Enter Password: ")

        if len(password) >= 7:
            has_digit = False
            has_upper = False
            has_lower = False
            has_special = False
            for char in password:
                if char.isdigit():
                    has_digit = True
                elif char.islower():
                    has_lower = True
                elif char.isupper():
                    has_upper = True
                else:
                    has_special = True

            if has_digit and has_lower and has_upper and not has_special:
                print("Password Changed")
                return password
            if not has_digit:
                print("Password needs a digit")
            if not has_upper:
                print("Password needs an upper case letter")
            if not has_lower:
                print("Password needs a lower case letter")
            if has_special:
                print("No special characters")

        else:
            print("Password is not long enough")


def main():
    """
    Includes two functions: generate_login(), and change_password().

    All two functions will run one after the other.

    For more information about each function, please see their respective docstrings.
    """
    generate_login()
    change_password()


if __name__ == "__main__" :
    main()
