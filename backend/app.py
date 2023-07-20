# Assuming you have your UI ready and imported the required classes.
# UI operations...
import os
import sys
sys.path.append(os.getcwd())
# Instantiate the DataManager class with the file names.
from backend.models.data_manager import DataManager


data_manager = DataManager('users.json', 'books.json', 'lendings.json')

# Read data from the JSON files.
users_data = data_manager.read_users()
books_data = data_manager.read_books()
lendings_data = data_manager.read_lendings()

# Process the data as needed by your UI.

# If you need to modify the data:
# Modify the data (e.g., add, remove, or update users, books, or lendings).

# Write the modified data back to the JSON files.
data_manager.write_users(users_data)
data_manager.write_books(books_data)
data_manager.write_lendings(lendings_data)

# Continue with your UI operations...
