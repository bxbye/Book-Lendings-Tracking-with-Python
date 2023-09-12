from backend.models.user import User
from backend.models.book import Book
from backend.models.data_manager import DataManager
import os



# its required for starting app correctly.
def find_root_directory(marker_filename="README.md"):
    current_directory = os.path.abspath(os.path.dirname(__file__))

    while True:
        # Check if the marker file exists in the current directory
        marker_file = os.path.join(current_directory, marker_filename)
        if os.path.exists(marker_file):
            return current_directory

        # Move one level up in the directory tree
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        
        # If we have reached the root of the file system, break the loop
        if parent_directory == current_directory:
            break

        current_directory = parent_directory

    # If the marker file is not found, return the current working directory as the root
    return os.path.abspath(os.getcwd())
# connecting with backend
# pathing works all operations systems correctly.
root_directory = find_root_directory()
print(f"root directory: {root_directory}")

# Instantiate DataManager class with file names
users_file = os.path.join(root_directory, "backend", "data", "users.json")
books_file = os.path.join(root_directory, "backend", "data", "books.json")
lendings_file = os.path.join(root_directory, "backend", "data", "lendings.json")
data_manager = DataManager(users_file, books_file, lendings_file)

# creating sample data for json files.
# create fake book datas.
import requests
import uuid

url = "https://book-finder1.p.rapidapi.com/api/search"

querystring = {"series":"Wings of fire","book_type":"Fiction","lexile_min":"600","lexile_max":"800","results_per_page":"50","page":"1"}

headers = {
	"X-RapidAPI-Key": "2923fe8e25msh4acefcf3398ef6fp162716jsn9f785c993f9d",
	"X-RapidAPI-Host": "book-finder1.p.rapidapi.com"
}
# 50 users will be set
response_books = requests.get(url, headers=headers, params=querystring)
results = response_books.json()['results']
#print(len(results), results[0])
books = []
for index, f_book in enumerate(results):
    id = str(uuid.uuid1())
    title = f_book['title']
    authors = ', '.join(f_book["authors"])
    barkod = str(index)
    new_book = Book(id, title, authors, barkod)
    # update database
    books.append(new_book.__dict__)
data_manager.write_books(books)

users = []
# 10 users will be set
response_users = requests.get("https://jsonplaceholder.typicode.com/users/")
result_users = response_users.json()
for index, f_user in enumerate(result_users):
    id = str(uuid.uuid1())
    ad = f_user["name"].split(" ")[0]
    soyad = f_user["name"].split(" ")[1]
    sicil = str(index)
    type = "fake_person"
    new_user = User(id, ad, soyad, sicil, type)
    users.append(new_user.__dict__)# to convert Class object to dict data type for save to JSON file
data_manager.write_users(users)