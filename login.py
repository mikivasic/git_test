

def generate_login(first_name, last_name, bcit_id):

    first_name = first_name[:3]
    last_name = last_name[:3]
    bcit_id = bcit_id[-3:]
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()

    return first_name + last_name + bcit_id


def change_password():
    while True:
        password = input("Enter Password")

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
            if has_digit == False:
                print("Password needs a digit")
            if has_upper == False:
                print("Password needs an upper case letter")
            if has_lower == False:
                print("Password needs a lower case letter")
            if has_special == True:
                print("No special characters")

        else:
            print("Password is not long enough")


def get_book_info():
    """
    function get_book_info(), the function asks the user to enter the following information:
           book title
           book ISBN
           book author last name
           book publisher
           year published
           book price
    The function will eliminate leading and trailing spaces from
        title, ISBN, author name and publisher (use function strip ()).
    The function will return a string from the given information
        in the same order specified above, separated by forward slash (/)
    """
    book_title = str(input("Enter book title: "))
    book_isbn = str(input("Enter book ISBN: "))
    book_author_last_name = str(input("Enter author last name: "))
    year_published = int(input("Enter year published: "))
    book_price = float(input("Enter price: "))
    csv_format = (book_title+","+str(book_isbn)+","+book_author_last_name+","+str(year_published)+","+str(book_price))
    stripped_book_title = book_title.strip()
    stripped_book_isbn = book_isbn.strip()
    stripped_book_author_last_name = book_author_last_name.strip()
    print("The CSV Format string: ")
    print(csv_format)


def main():

    generate_login("joHN", "dOe", "a123456")
    change_password()
    get_book_info()


if __name__ == "__main__":
    main()
