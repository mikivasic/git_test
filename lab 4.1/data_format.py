# Milos Vasic and Mohammadreza Partow
import login


def main():
    """
    All functions will run one after the other.

    For more information about each function, please see their respective docstrings.
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    bcit_id = input("Enter your BCIT ID: ")

    generate_login = login.generate_login(first_name, last_name, bcit_id)
    print(generate_login)
    password = login.change_password()
    print(password)

    book_title = str(input("Enter book title: "))
    book_isbn = str(input("Enter book ISBN: "))
    book_author_last_name = str(input("Enter author last name: "))
    year_published = int(input("Enter year published: "))
    book_price = float(input("Enter price: "))
    print("The CSV Format String: ")
    csv_format = (book_title + "," + str(book_isbn) + "," + book_author_last_name + "," + str(year_published) + "," +
                  str(book_price))
    print(csv_format)

    json = f'{{"book_title":"{book_title}",' \
           f'{{book_isbn":"{book_isbn}",' \
           f'{{book_author_last_name":"{book_author_last_name}",' \
           f'{{year_published":"{str(year_published)}",' \
           f'{{book_price":"{str(book_price)}"}}'
    print("The JSON String: ")
    print(json)


if __name__ == "__main__" :
    main()
