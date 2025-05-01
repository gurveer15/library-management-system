from colorama import Fore, Style, init
import admin
import member

init(autoreset=True)

def main():
    print(Fore.CYAN + "Welcome to the Library Management System")
    print(Fore.CYAN + "-" * 50)

    while True:
        print("\n" + Fore.YELLOW +  "User Menu:")
        print("1. Admin")
        print("2. Member")
        print("3. Exit")
        print("-" * 50)
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            if admin.authenticate_admin():
                while True:
                    print("\n" + Fore.YELLOW + "Admin Menu:")
                    print("1. Add Book")
                    print("2. View Books")
                    print("3. Search Books")
                    print("4. Issue Book")
                    print("5. Return Book")
                    print("6. View Fine History")
                    print("7. Back")
                    admin_choice = input("Enter your choice: ").strip()

                    if admin_choice == '1':
                        admin.add_book()
                    elif admin_choice == '2':
                        admin.view_books()
                    elif admin_choice == '3':
                        admin.search_books()
                    elif admin_choice == '4':
                        admin.issue_book()
                    elif admin_choice == '5':
                        admin.return_book()
                    elif admin_choice == '6':
                        admin.view_fine_history()
                    elif admin_choice == '7':
                        break
                    else:
                        print(Fore.RED + "[ERROR] Invalid choice. Please try again.")
            else:
                print("[ERROR] Authentication failed. Please try again.")
                
        elif choice == '2':
            while True:
                print("\n" + Fore.YELLOW + "Member Menu:")
                print("1. Register as Member")
                print("2. Search Books")
                print("3. View Available Books")
                print("4. Back")
                member_choice = input("Enter your choice: ").strip()

                if member_choice == '1':
                    member.register_member()
                elif member_choice == '2':
                    member.search_books()
                elif member_choice == '3':
                    member.view_books()
                elif member_choice == '4':
                    break
                else:
                    print(Fore.RED + "[ERROR] Invalid choice. Please try again.")

        elif choice == '3':
            print(Fore.CYAN + "\nThank you for using the system. Goodbye!")
            break
        else:
            print(Fore.RED + "[ERROR] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
