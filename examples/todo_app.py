import sqlite3

# Connect to the database
def fetch_users():
    conn = sqlite3.connect("people_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age FROM people")
    users = cursor.fetchall()
    conn.close()
    return users

# Authenticate user
def authenticate(users):
    print("Welcome to the To-Do App!")
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    for user in users:
        if user[0] == name and str(user[1]) == age:
            print(f"Authentication successful! Welcome, {name}.")
            return True
    print("Authentication failed. Please try again.")
    return False

# To-Do App functionality
def todo_app():
    tasks = []
    while True:
        print("\nTo-Do App Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == "2":
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice == "3":
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number.")
        elif choice == "4":
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    users = fetch_users()
    if authenticate(users):
        todo_app()

if __name__ == "__main__":
    main()