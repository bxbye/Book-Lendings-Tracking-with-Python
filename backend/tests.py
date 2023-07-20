import json
import os
import sys
sys.path.append(os.getcwd())

from backend.models.data_manager import DataManager
from backend.models.book import Book
from backend.models.lending import Lending
from backend.models.user import User
# Create instances of User, Book, and Lending classes
user1 = User(1, "John", "Doe", "U12345", "employee")
user2 = User(2, "Alice", "Smith", "U67890", "student")
book1 = Book(101, "Python Programming", "John Smith", "B12345")
book2 = Book(102, "JavaScript for Beginners", "Emily Johnson", "B67890")
lending1 = Lending(1001, "U12345", "B12345", "2023-07-20")
lending2 = Lending(1002, "U67890", "B67890", "2023-07-18")

# Instantiate DataManager class with file names
users_file = "backend/data/users.json"
books_file = "backend/data/books.json"
lendings_file = "backend/data/lendings.json"
data_manager = DataManager(users_file, books_file, lendings_file)
# Prepare data for writing to JSON files
users_data = [user1.__dict__, user2.__dict__]
books_data = [book1.__dict__, book2.__dict__]
lendings_data = [lending1.__dict__, lending2.__dict__]

# Write data to JSON files
data_manager.write_users(users_data)
data_manager.write_books(books_data)
data_manager.write_lendings(lendings_data)