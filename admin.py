import mysql.connector
from datetime import datetime, date, timedelta
from database import get_connection
from colorama import Fore, init
import getpass

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin1234"  

init(autoreset=True)

def authenticate_admin():
    print("\nPlease login to access admin features.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("[SUCCESS] Admin logged in successfully.")
        return True
    else:
        print("[ERROR] Invalid credentials.")
        return False

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    connection.commit()
    print(Fore.GREEN + "[SUCCESS] Book added!")

    cursor.close()
    connection.close()

def view_books():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print(Fore.CYAN + "\nAvailable Books:")
    for book in books:
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Available: {'Yes' if book[3] else 'No'}")

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
        print(Fore.CYAN + "\nSearch Results:")
        for book in results:
            availability = "Yes" if book['available'] else "No"
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Available: {availability}")
    else:
        print(Fore.RED + "No matching books found.")

    cursor.close()
    connection.close()

def issue_book():
    view_books()
    book_id = int(input("Enter Book ID to issue: "))
    member_id = int(input("Enter Member ID who is issuing: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT available FROM books WHERE id = %s", (book_id,))
    result = cursor.fetchone()

    if result and result[0]:
        return_date = date.today() + timedelta(days=14)
        cursor.execute(
            "INSERT INTO issued_books (book_id, member_id, issue_date, return_date) VALUES (%s, %s, CURDATE(), %s)",
            (book_id, member_id, return_date)
        )
        cursor.execute("UPDATE books SET available = FALSE WHERE id = %s", (book_id,))
        connection.commit()
        print(Fore.GREEN + "[SUCCESS] Book issued!")
        print(Fore.YELLOW + f"Book issued! Please return by: {return_date} to avoid fines.")
    else:
        print(Fore.RED + "[ERROR] Book not available!")

    cursor.close()
    connection.close()

def return_book():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        book_id = int(input("Enter Book ID to return: "))
        member_id = int(input("Enter Member ID who is returning the book: "))

        cursor.execute(
            "SELECT * FROM issued_books WHERE book_id = %s AND member_id = %s",
            (book_id, member_id)
        )
        issued_book = cursor.fetchone()

        if not issued_book:
            print(Fore.RED + f"Book ID {book_id} is not issued to Member ID {member_id}.")
            return

        return_due_date = issued_book['return_date']
        today = date.today()

        if today > return_due_date:
            days_late = (today - return_due_date).days
            fine = days_late * 5
            print(Fore.RED + f"Returned {days_late} days late. Fine = ₹{fine}")
            cursor.execute("""
                INSERT INTO fine_history (member_id, book_id, fine_amount, return_date)
                VALUES (%s, %s, %s, %s)
            """, (member_id, book_id, fine, today))
        else:
            print(Fore.GREEN + "Returned on time. No fine.")

        cursor.execute("UPDATE books SET available = TRUE WHERE id = %s", (book_id,))
        cursor.execute("DELETE FROM issued_books WHERE book_id = %s AND member_id = %s", (book_id, member_id))

        connection.commit()
        print(Fore.GREEN + f"Book ID {book_id} successfully returned by Member ID {member_id}.")

    except Exception as e:
        print(Fore.RED + f"[ERROR] {e}")
    finally:
        cursor.close()
        connection.close()

def view_fine_history():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
       SELECT fine_history.*, members.name, books.title
       FROM fine_history
       JOIN members ON fine_history.member_id = members.id
       JOIN books ON fine_history.book_id = books.id
       ORDER BY fine_history.return_date DESC;
    """)
    results = cursor.fetchall()

    print(Fore.CYAN + "\nFine History:")
    for row in results:
        print(f"Member: {row['name']} | Book: {row['title']} | Fine: ₹{row['fine_amount']} | Returned: {row['return_date']}")

    cursor.close()
    connection.close()
