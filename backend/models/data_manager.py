import json

class DataManager:
    def __init__(self, users_file, books_file, lendings_file):
        self.users_file = users_file
        self.books_file = books_file
        self.lendings_file = lendings_file

    def read_users(self):
        users_data = []
        try:
            with open(self.users_file, 'r') as file:
                users_data = json.load(file)
        except:
            print(f"dosya okuma hatasi! {self.users_file}'da sorun olabilir.")
        return users_data

    def write_users(self, users_data):
        with open(self.users_file, 'w') as file:
            json.dump(users_data, file)

    def read_books(self):
        books_data = []
        try:
            with open(self.books_file, 'r') as file:
                books_data = json.load(file)
        except:
            print(f"dosya okuma hatasi! {self.books_file}'da sorun olabilir.")
        return books_data

    def write_books(self, books_data):
        with open(self.books_file, 'w') as file:
            json.dump(books_data, file)

    def read_lendings(self):
        lendings_data = []
        try:
            with open(self.lendings_file, 'r') as file:
                lendings_data = json.load(file)
        except:
            print(f"dosya okuma hatasi! {self.users_file}'da sorun olabilir.")
        return lendings_data

    def write_lendings(self, lendings_data):
        with open(self.lendings_file, 'w') as file:
            json.dump(lendings_data, file)

    # dosyalarin yedeklenmesi gerek. senede 1 kere yedeklense yeterli olur.
    # raporlama yapilmasi gerek. dosyalar okunup istenen rapor formatinda cikti uretilmesi yapilabilir.