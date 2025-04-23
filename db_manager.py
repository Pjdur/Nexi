import sqlite3

class DatabaseManager:
    def __init__(self):
        self.connection = None

    def create_database(self, db_name):
        try:
            self.connection = sqlite3.connect(f"{db_name}.db")
            print(f"Database '{db_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error occurred while creating database: {e}")

    def create_table(self, table_name, schema):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})")
            self.connection.commit()
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error occurred while creating table: {e}")

    def insert_data(self, table_name, columns, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
            self.connection.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error occurred while inserting data: {e}")

    def query_data(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Error occurred while querying data: {e}")