import mysql.connector
from database import get_connection
from colorama import Fore, Style, init

init(autoreset=True)

def register_member():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO members (name, email) VALUES (%s, %s)", (name, email))
        connection.commit()
        print(Fore.GREEN + "[SUCCESS] Member registered!")
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:  # Duplicate entry
            print(Fore.RED + "Member with this email already exists.")
        else:
            print(Fore.RED + "An error occurred while registering the member. Please try again later.")
    finally:
        cursor.close()
        connection.close()

def view_books():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, author FROM books WHERE available = TRUE")
    books = cursor.fetchall()

    print("\n" + Fore.CYAN + "Available Books:")
    for book in books:
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]}")

    cursor.close()
    connection.close()

def search_books():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    keyword = input("Enter book title or author to search: ")
    query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()

    if results:
        print("\n" + Fore.CYAN + "Search Results:")
        for book in results:
            availability = "Yes" if book['available'] else "No"
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Available: {availability}")
    else:
        print(Fore.YELLOW + "No matching books found.")

    cursor.close()
    connection.close()
