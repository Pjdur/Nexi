from db_manager import DatabaseManager
from encryption import Encryption

def main():
    print("Welcome to Nexi - A Python-Based Database Management System")
    db_manager = DatabaseManager()
    
    while True:
        print("\nOptions:")
        print("1. Create Database")
        print("2. Create Table")
        print("3. Insert Data")
        print("4. Query Data")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            db_name = input("Enter database name: ")
            db_manager.create_database(db_name)
        elif choice == "2":
            table_name = input("Enter table name: ")
            schema = input("Enter table schema (e.g., id INT, name TEXT): ")
            db_manager.create_table(table_name, schema)
        elif choice == "3":
            table_name = input("Enter table name: ")
            columns = input("Enter columns (e.g., id, name): ")
            values = input("Enter values (e.g., 1, 'John'): ")
            db_manager.insert_data(table_name, columns, values)
        elif choice == "4":
            query = input("Enter SQL query: ")
            db_manager.query_data(query)
        elif choice == "5":
            print("Exiting Nexi. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()