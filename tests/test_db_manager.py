import pytest
from db_manager import DatabaseManager

@pytest.fixture
def db_manager():
    db = DatabaseManager()
    db.create_database("test_db")
    return db

def test_create_table(db_manager):
    db_manager.create_table("users", "id INT, name TEXT")
    assert True  # Add specific checks for table creation if needed

def test_insert_data(db_manager):
    db_manager.create_table("users", "id INT, name TEXT")
    db_manager.insert_data("users", "id, name", "1, 'John'")
    assert True  # Add specific checks for data insertion if needed

def test_query_data(db_manager):
    db_manager.create_table("users", "id INT, name TEXT")
    db_manager.insert_data("users", "id, name", "1, 'John'")
    db_manager.query_data("SELECT * FROM users")
    assert True  # Add specific checks for query results if needed