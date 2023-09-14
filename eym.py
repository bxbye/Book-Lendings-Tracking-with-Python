from datetime import datetime
import tkinter as tk
import os

from backend.models.lending import Lending
from backend.models.user import User
from backend.models.book import Book
from backend.models.data_manager import DataManager

# main frame
window = tk.Tk()
height = 720
width = 1400
window.geometry(f"{width}x{height}")
window.title("BANDO EYM OTOMASYON YAZILIMI")
# frm_menu
frm_menu = tk.Frame(master=window, relief="raised", borderwidth=2)
frm_menu.pack(side="left", fill=tk.Y)
# frm_main_page which involves menu operations.
frm_main_page = tk.Frame(master=window, relief="raised", borderwidth=2)
frm_main_page.pack(fill=tk.BOTH, expand=True)


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

# menu functions for dynamic ui changing
def add_book():
    window.title("EYM OTOMASYON - KİTAP EKLEME")
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    # frm_add_book
    frame = tk.Frame(master=frm_main_page, relief="groove", borderwidth=3)
    frame.grid(row=0, column=0, sticky="nw")

    lbl_baslik = tk.Label(master=frame, text="Kitap Adı", bg="#85A389", fg="white", relief="raised", borderwidth=2, anchor=tk.W)
    ent_baslik = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_baslik.grid(row=0, column=0, sticky="ew", padx=5)
    ent_baslik.grid(row=0, column=1)

    lbl_yazar = tk.Label(master=frame, text="Yazar", bg="#85A389", fg="white", relief="raised", borderwidth=2, anchor=tk.W)
    ent_yazar = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_yazar.grid(row=1, column=0, sticky="ew", padx=5)
    ent_yazar.grid(row=1, column=1)
    
    lbl_barkod = tk.Label(master=frame, text="Barkod No", bg="#85A389", fg="white", relief="raised", borderwidth=2, anchor=tk.W)
    ent_barkod = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_barkod.grid(row=2, column=0, sticky="ew", padx=5)
    ent_barkod.grid(row=2, column=1)
    
    button = tk.Button(master=frame, text="Kitap Ekle", command= lambda: btn_add_book(ent_baslik, ent_yazar, ent_barkod))
    button.grid(row=3, column=1, sticky="e", ipadx=5, ipady=5)
    # Update the GUI immediately to display the entry widgets
    frm_main_page.update()

def add_user():
    window.title("EYM OTOMASYON - KULLANICI EKLEME")
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    # frm_add_book
    frame = tk.Frame(master=frm_main_page, relief="groove", borderwidth=3)
    frame.grid(row=0, column=0, sticky="nw")

    lbl_ad = tk.Label(master=frame, text="Ad", bg="#85A389", fg="white", relief="raised", borderwidth=2, anchor=tk.W)
    ent_ad = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_ad.grid(row=0, column=0, sticky="ew", padx=5)
    ent_ad.grid(row=0, column=1)

    lbl_soyad = tk.Label(master=frame, text="Soyad", bg="#85A389", fg="white", relief="raised", borderwidth=2, anchor=tk.W)
    ent_soyad = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_soyad.grid(row=1, column=0, sticky="ew", padx=5)
    ent_soyad.grid(row=1, column=1)

    lbl_sicil = tk.Label(master=frame, text="Sicil No", bg="#85A389", fg="white", relief="raised", borderwidth=2, anchor=tk.W)
    ent_sicil = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_sicil.grid(row=2, column=0, sticky="ew", padx=5)
    ent_sicil.grid(row=2, column=1)

    lbl_sinif = tk.Label(master=frame, text="Kullanıcı Türü", bg="#85A389", fg="white", relief="raised", borderwidth=2, anchor=tk.W)
    ent_sinif = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_sinif.grid(row=3, column=0, sticky="ew", padx=5)
    ent_sinif.grid(row=3, column=1)

    button = tk.Button(master=frame, text="Kullanıcı Ekle", command=lambda: btn_add_user(ent_ad, ent_soyad, ent_sicil, ent_sinif))
    button.grid(row=4, column=1, sticky="e", ipadx=5, ipady=5)
    # Update the GUI immediately to display the entry widgets
    frm_main_page.update()
def lend_book():
    window.title("EYM OTOMASYON - KİTAP TESLİM ETME")
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    frm_main_page.columnconfigure(1, minsize=300, weight=1)

    # frame for scanning barcode. includes; lbl_barcode, ent_barcode, btn_barcode_add
    frm_barcode = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frm_barcode.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    lbl_barcode = tk.Label(frm_barcode, text="Barkod No", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10, anchor=tk.W)
    lbl_barcode.pack(side=tk.LEFT)
    ent_barcode = tk.Entry(frm_barcode, width=20, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_barcode.pack(side=tk.LEFT)
    btn_barcode_search = tk.Button(frm_barcode, text="Sepete Ekle", width=10, command=lambda: btn_add_box_of_book(ent_barcode))
    btn_barcode_search.pack(side=tk.LEFT, ipadx=5, ipady=5)

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    last_item = {}
    the_book = {}
    if len(lending_box) > 0:
        last_item = lending_box[-1]
        the_book = {
        "Kitap Adı": last_item["baslik"],
        "Yazar": last_item["yazar"],
        "Barkod No": last_item["barkod"],
        "Durumu": last_item["status"]
    }
    
    frm_book_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_info.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_book.items()):
        frame = tk.Frame(frm_book_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10, anchor=tk.W)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=30, anchor=tk.W)
        key.grid(row=index, column=0)
        value.grid(row=index, column=1)
        frame.pack(fill=tk.X)

    # frame for searching user. includes; lbl_sicil_no, ent_sicil_no, btn_search_user_by_sicil_no
    frm_searc_user = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_searc_user.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    lbl_sicil_no = tk.Label(frm_searc_user, text="Sicil No", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10, anchor=tk.W)
    lbl_sicil_no.pack(side=tk.LEFT)
    ent_sicil_no = tk.Entry(frm_searc_user, width=20, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_sicil_no.pack(side=tk.LEFT)
    btn_search_user = tk.Button(frm_searc_user, text="Kullanıcı Ara", width=10, command=lambda: btn_user_search_by_sicil(ent_sicil_no, "lend_screen"))
    btn_search_user.pack(side=tk.LEFT, ipadx=5, ipady=5)

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    the_user = {}
    last_user = {}
    if (len(searched_user) > 0):
        last_user = searched_user[-1]
        the_user = {
            "Ad": last_user["ad"],
            "Soyad": last_user["soyad"],
            "Sicil No": last_user["sicil"],
            "Kullanıcı Türü": last_user["type"]
        }

    frm_user_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_user_info.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_user.items()):
        frame = tk.Frame(frm_user_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10, anchor=tk.W)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=30, anchor=tk.W)
        key.grid(row=index, column=0)
        value.grid(row=index, column=1)
        frame.pack(fill=tk.X)
        ## this frame will include user informations.
        # otherwise, "Hicbir kullanici secilmedi." mesaji gosterilsin.
    
    # frame for book box. includes; lbl_book_name, btn_remove_book
    frm_book_box = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_box.grid(row=0, column=1, sticky="nsew", rowspan=20)
    # this frame will iclude added books's name and remove button for each.
    # otherwise, "Sepete henuz kitap eklenmedi." mesaji gosterilsin.
    for i, item in enumerate(lending_box):
        frame = tk.Frame(frm_book_box, relief="raised", borderwidth=1)
        lbl = tk.Label(frame, text=item["baslik"], bg="#85A389", fg="white", anchor=tk.W)
        lbl.pack(side="left", fill=tk.X, expand=True)
        frame.pack(fill=tk.X)
    # frame for Operation Button. includes; btn_lend_book
    btn_lend_book = tk.Button(frm_main_page, text="Teslim Et", command= btn_lend_books)
    btn_lend_book.grid(row=21, column=1, sticky="e", ipadx=5, ipady=5)
    btn_clear_box = tk.Button(frm_main_page, text="Sepeti Temizle", command=lambda: [lending_box.clear(), lend_book()])
    btn_clear_box.grid(row=21, column=1, sticky="w", ipadx=5, ipady=5)
    # Update the GUI immediately to display the entry widgets
    frm_main_page.update()

def return_book():
    window.title("EYM OTOMASYON - KİTAP İADE ALMA")
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    frm_main_page.columnconfigure(1, minsize=300, weight=1)

    # frame for scanning barcode. includes; lbl_barcode, ent_barcode, btn_barcode_add
    frm_barcode = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frm_barcode.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    lbl_barcode = tk.Label(frm_barcode, text="Barcode", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10, anchor=tk.W)
    lbl_barcode.pack(side=tk.LEFT)
    ent_barcode = tk.Entry(frm_barcode, width=20, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_barcode.pack(side=tk.LEFT)
    btn_barcode_search = tk.Button(frm_barcode, text="Sepete Ekle", width=10, command=lambda: btn_add_returning_box_of_book(ent_barcode))
    btn_barcode_search.pack(side=tk.LEFT, ipadx=5, ipady=5)

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    last_item = {}
    the_book = {}
    if len(returning_box) > 0:
        last_item = returning_box[-1]
        the_book = {
        "Başlık": last_item["baslik"],
        "Yazar": last_item["yazar"],
        "Barkod No": last_item["barkod"],
        "Durumu": last_item["status"]
    }
    frm_book_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_info.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_book.items()):
        frame = tk.Frame(frm_book_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10, anchor=tk.W)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=30, anchor=tk.W)
        key.grid(row=index, column=0)
        value.grid(row=index, column=1)
        frame.pack(fill=tk.X)

    # frame for searching user. includes; lbl_sicil_no, ent_sicil_no, btn_search_user_by_sicil_no
    frm_searc_user = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_searc_user.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    lbl_sicil_no = tk.Label(frm_searc_user, text="Sicil No", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10, anchor=tk.W)
    lbl_sicil_no.pack(side=tk.LEFT)
    ent_sicil_no = tk.Entry(frm_searc_user, width=20, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_sicil_no.pack(side=tk.LEFT)
    btn_search_user = tk.Button(frm_searc_user, text="Kullanici Ara", width=10, command=lambda: btn_user_search_by_sicil(ent_sicil_no, "return_screen"))
    btn_search_user.pack(side=tk.LEFT, ipadx=5, ipady=5)

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    the_user = {}
    last_user = {}
    if (len(searched_user) > 0):
        last_user = searched_user[-1]
        the_user = {
            "Ad": last_user["ad"],
            "Soyad": last_user["soyad"],
            "Sicil No": last_user["sicil"],
            "Kullanıcı Sınıfı": last_user["type"]
        }

    frm_user_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_user_info.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_user.items()):
        frame = tk.Frame(frm_user_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10, anchor=tk.W)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=10, anchor=tk.W)
        key.grid(row=index, column=0)
        value.grid(row=index, column=1)
        frame.pack(fill=tk.X)
        ## this frame will include user informations.
        # otherwise, "Hicbir kullanici secilmedi." mesaji gosterilsin.
    
    # frame for book box. includes; lbl_book_name, btn_remove_book
    frm_book_box = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_box.grid(row=0, column=1, sticky="nsew", rowspan=20)
    # this frame will iclude added books's name and remove button for each.
    # otherwise, "Sepete henuz kitap eklenmedi." mesaji gosterilsin.
    for i, item in enumerate(returning_box):
        frame = tk.Frame(frm_book_box, relief="raised", borderwidth=1)
        lbl = tk.Label(frame, text=item["baslik"], bg="#85A389", fg="white", anchor=tk.W)
        lbl.pack(side="left", fill=tk.X, expand=True)
        frame.pack(fill=tk.X)
    # frame for Operation Button. includes; btn_lend_book
    btn_lend_book = tk.Button(frm_main_page, text="İade Al", command= btn_return_books)
    btn_lend_book.grid(row=21, column=1, sticky="e", ipadx=5, ipady=5)
    btn_clear_box = tk.Button(frm_main_page, text="Sepeti Temizle", command=lambda: [returning_box.clear(), return_book()])
    btn_clear_box.grid(row=21, column=1, sticky="w", ipadx=5, ipady=5)
    # Update the GUI immediately to display the entry widgets
    frm_main_page.update()
# import function 
from backend.helpers.create_pdf import create_pdf
def other_operations():
    window.title("EYM OTOMASYON - DİĞER İŞLEMLER")
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    frame1 = tk.Frame(master=frm_main_page, relief="groove", borderwidth=2)
    frame1.grid(row=0, column=0, padx=10, pady=10)
    frame2 = tk.Frame(master=frm_main_page, relief="groove", borderwidth=2)
    frame2.grid(row=1, column=0)

    # mevcut kitap adetlerinin gosterilmesi
    count_of_all_books = len(books)
    lbl_all_books = tk.Label(master=frame1, text=f"Toplam Kitap: {count_of_all_books}")
    lbl_all_books.pack()
    count_of_lent_books = len([item for item in lendings if item.get('status') == 'lent'])
    lbl_lended_books = tk.Label(master=frame1, text=f"Dagitilan Kitap: {count_of_lent_books}")
    lbl_lended_books.pack()
    count_of_available_books = count_of_all_books - count_of_lent_books
    lbl_curr_books = tk.Label(master=frame1, text=f"Mevcut Kitap: {count_of_available_books}")
    lbl_curr_books.pack()    

    # kimde hangi kitaplarin oldugunun sorgulanmasi.
    lbl_sicil_no = tk.Label(frame2, text="Sicil No: ")
    lbl_sicil_no.pack(side=tk.LEFT)

    ent_sicil_no = tk.Entry(frame2)
    ent_sicil_no.pack(side=tk.LEFT)

    btn_sicil_no = tk.Button(frame2, text="Sorgula", command=lambda: search_books_by_user_sicil(ent_sicil_no))
    btn_sicil_no.pack(side=tk.LEFT)


menu_items = {
    "Kitap Ekle": add_book,
    "Kullanıcı Ekle": add_user,
    "Kitap Teslimi": lend_book,
    "Kitap İade": return_book,
    "Diğer İşlemler": other_operations
}

# add menu items
for i, (title, func) in enumerate(menu_items.items()):
    button = tk.Button(master=frm_menu, text=title, command=func)
    button.grid(row=i, column=0, sticky="wens", ipadx=5, ipady=5, pady=5)


# connecting with backend
# pathing works all operations systems correctly.
root_directory = find_root_directory()
print(f"root directory: {root_directory}")

# Instantiate DataManager class with file names
users_file = os.path.join(root_directory, "backend", "data", "users.json")
books_file = os.path.join(root_directory, "backend", "data", "books.json")
lendings_file = os.path.join(root_directory, "backend", "data", "lendings.json")
data_manager = DataManager(users_file, books_file, lendings_file)


# reading data at the begining of the programme
users = data_manager.read_users()
books = data_manager.read_books()
lendings = data_manager.read_lendings()

# lists for managing ui states and interactions.
lending_box = [] # lend book sayfasinda barkod taramasi yapildiginda eslesen kitaplar buraya eklenir.
returning_box = [] # return book barkod taramasi yapildiginda eslesen kitaplar buraya eklenir.
searched_user = []
# additional functions
def btn_add_book(baslik, yazar, barkod):
    print(baslik.get(), yazar.get(), barkod.get())
    # check blanks are emty or not
    if (not baslik.get() or not yazar.get() or not barkod.get()):
        print(f"Tum bilgiler doldurulmalidir.")
        return
    # check if books list contains the same book as barkod no
    if any(book.get("barkod") == barkod.get() for book in books):
        print(f"Bu kitap zaten kitaplar listesine eklenmis.")
        return
    new_book = Book(len(books), baslik.get(), yazar.get(), barkod.get())
    # update database
    books.append(new_book.__dict__)
    data_manager.write_books(books)
    # delete entries
    baslik.delete(0, tk.END)
    yazar.delete(0, tk.END)
    barkod.delete(0, tk.END)
    print(f"Yeni kitap eklendi.")

# parametre olarak gelen veriler Entry objesidir. Icerideki degisiklikler formu etkilemektedir.
def btn_add_user(ad, soyad, sicil, sinif):
    print(ad.get(), soyad.get(), sicil.get(), sinif.get())
    # check blanks are emty or not
    if (not ad.get() or not soyad.get() or not sicil.get() or not sinif.get()):
        print(f"Tum bilgiler doldurulmalidir.")
        return
    # check if books list contains the same book as barkod no
    if any(user.get("sicil") == sicil.get() for user in users):
        print(f"Bu kullanici zaten users listesine eklenmis.")
        return
    new_user = User(len(users), ad.get(), soyad.get(), sicil.get(), sinif.get())
    users.append(new_user.__dict__)# to convert Class object to dict data type for save to JSON file
    data_manager.write_users(users)
    # clean entry fields.
    ad.delete(0, tk.END)
    soyad.delete(0, tk.END)
    sicil.delete(0, tk.END)
    sinif.delete(0, tk.END)
    print(f"Yeni bir kullanici eklendi.")

def btn_add_box_of_book(ent_barkod):
    barkod = ent_barkod.get()
    
    # if books not exist in books list or if book already added to lending_box we can not add to box again.
    if any(book.get("barkod") == barkod for book in books):
        if any(b.get("barkod") == barkod for b in lending_box):
            print(f"sepete daha onceden eklenmis kitabi tekrar sepete ekleyemeyiz.")
            return
    else:
        print(f"kitaplar listesinde olmayan kitabi sepete ekleyemezsiniz. Once kitabi barkod numarasiyla birlikte kaydediniz.")
        return
    searched_book = next(book for book in books if book.get("barkod") == barkod)
    # check is the book status available or not?
    if (searched_book and searched_book.get("status") != "available"):
        # sepete eklenemez cunku mevcut degil, baskasina verilmistir.
        print("Bu kitap su an musait degil. Once iade edilip kutuphanede mevcut olmasi gerekir.")
        return    
    # check status of book
    # books listesinde aranacak.
    for book in books:
        if(book["barkod"] == barkod):
            lending_box.append(book)
            print(book)
            lend_book()
            return
    print(f"barkod: {barkod} numarali kitap kayitlarda bulunamadi.")

# code reputation couldn't provided. So i copied above code.
def btn_add_returning_box_of_book(ent_barkod):
    barkod = ent_barkod.get()
    
    # if books not exist in books list or if book already added to lending_box we can not add to box again.
    if any(book.get("barkod") == barkod for book in books):
        if any(b.get("barkod") == barkod for b in returning_box):
            print(f"sepete daha onceden eklenmis kitabi tekrar sepete ekleyemeyiz.")
            return
    else:
        print(f"kitaplar listesinde olmayan kitabi sepete ekleyemezsiniz. Once kitabi barkod numarasiyla birlikte kaydediniz.")
        return
    searched_book = next(book for book in books if book.get("barkod") == barkod)
    # check is the book status available or not?
    if (searched_book and searched_book.get("status") != "unavailable"):
        # sepete eklenemez cunku mevcut degil, baskasina verilmistir.
        print("Bu kitap su an unavailable degil. Zaten kutuphanede olan kitap iade edilemez.")
        return    
    # check status of book
    # books listesinde aranacak.
    for book in books:
        if(book["barkod"] == barkod):
            returning_box.append(book)
            print(book)
            return_book()
            return
    print(f"barkod: {barkod} numarali kitap kayitlarda bulunamadi.")

def btn_user_search_by_sicil(ent_sicil, screen_name):
    sicil_no = ent_sicil.get()
    for user in users:
        if(user["sicil"] == sicil_no):
            searched_user.append(user)
            print(user)
            if screen_name == "lend_screen":
                lend_book()
            elif screen_name == "return_screen":
                return_book()
            return
    print(f"sicil: {sicil_no} numarali kullanici kayitlarda bulunamadi.")
    return
def btn_lend_books():
    # lending_box listesindeki tum kitaplar, en son aratilan kullaniciya teslim edilecek.
    # sepetteki kitaplar
    for book in lending_box:
        print(book.items())
    # teslim edilecek kullanici
    if (len(searched_user) <= 0):
        print(f"Kitaplarin teslim edilecegi kullaniciyi secmeniz gerekmektedir.")
        return
    user_to_lend = searched_user[-1]
    for i, book in enumerate(lending_box):
        new_lending = Lending(len(lendings), user_to_lend.get("sicil"), book.get("barkod"), datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        lendings.append(new_lending.__dict__)
        update_book_status(book.get("barkod"), "unavailable")
    # update json files.
    data_manager.write_lendings(lendings)
    data_manager.write_books(books)
    # veritabaninda da guncellenecek.
    # islemler bitince ui guncellenecek. ui'da kullanilan listeler temizlenecek.
    if(len(lending_box) <= 0):
        print("Sepete hic kitap eklenmemistir.")
    lending_box.clear()
    searched_user.clear()
    lend_book()

def btn_return_books():
    # lending_servisten, bu kitaplar son aranan kullaniciya aitse status returned olup kitaplar alinacak.
    # sepetteki kitaplari goster
    for book in returning_box:
        print(book.items())
    # geri teslim edecek kullanici
    if (len(searched_user) <= 0):
        print(f"Kitaplarin teslim edilecegi kullaniciyi secmeniz gerekmektedir.")
        return
    user_to_return = searched_user[-1]

    # sepettenki her kitap icin tek tek lendings'den kontrol yapilacak. bu kitap bu kullanici tarafindan mi alinmis?
    check_box_books = True
    for book in returning_box:
        if(check_lending_cervice(book.get("barkod"), user_to_return.get("sicil"))):
            print(f"{book.get('barkod')} ve {user_to_return.get('sicil')} eslesmistir.")
        else:
            print(f"{book.get('barkod')} ve {user_to_return.get('sicil')} eslesmemistir.")
            check_box_books = False
    #  Alindiysa lending_servisde iade edilecek, kitap status guncellenecek.
    if(check_box_books):
        print(f"tum kitaplar bu kisiye aittir. Hepsi topluca teslim alinabilir.")
        for rb in returning_box:
            update_lendings_status(rb.get("barkod"), user_to_return.get("sicil"), "returned")
            update_book_status(rb.get("barkod"), "available")

        # update db json files
        data_manager.write_lendings(lendings)
        data_manager.write_books(books)
        # cache veriler silinecek.
        returning_box.clear()
        searched_user.clear()
        return_book() # update ui screen to fill it again with new datas.
    #  alinmadiysa islem yapilmayacak.
    else:
        print("kitap listesinde bu kisiye ait olmayan kitap mevcuttur.")
    return

# returns True if parameters matches otherwise book belongs to another user
def check_lending_cervice(book_barcode, user_sicil):
    for lended_book in lendings:
        print(lended_book)
        if(lended_book.get("book_barkod") == book_barcode and lended_book.get("user_sicil") == user_sicil and not lended_book.get("status") == "returned"):
            return True
    return False #if for loop finishes without return True
def update_lendings_status(barcode, sicil, status):
    # update status of matched object
    for lended_book in lendings:
        if(lended_book.get("book_barkod") == barcode and lended_book.get("user_sicil") == sicil):
            lended_book["status"] = status
            lended_book["returned_date"] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
def update_book_status(barkod, status):
    for book in books:
        if(book.get("barkod") == barkod):
            book["status"] = status
            break
    print(f"{barkod} barkod numarali kitap durumu {status} olarak guncellendi.")
    return

def find_book_by_barcode(barcode_no):
    for book in books:
        if(book.get("barkod") == barcode_no):
            return book
    return None
def search_books_by_user_sicil(sicil_no):
    sicil_id = sicil_no.get()
    # find user info
    curr_user = find_user_by_sicil_id(sicil_id)
    if not curr_user:
        raise Exception('Bu sicil numarali kullanici bulunamadi.')
    print(curr_user)
    # search user sicil_no from lending records
    records = []
    for lend_record in lendings:
        if(lend_record.get("user_sicil") == sicil_no.get()):
            book = find_book_by_barcode(lend_record.get("book_barkod"))
            lending_info = {
                'title': book.get('baslik'),
                'status': "emanet verildi" if lend_record.get('returned_date') == None else "iade edildi",
                'lent_date': lend_record.get('lent_date'),
                'returned_date': '' if lend_record.get('returned_date') == None else lend_record.get('lent_date')
            }
            records.append(lending_info)
    if(len(records) == 0):
        print("Bu kisiye ait teslimat bilgisi yoktur.")
    
    # call create_pdf function with datas
    print(records)
    creation_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    create_pdf(records, curr_user, creation_date)
# returns user if exist, otherwise return false
def find_user_by_sicil_id(sicil_id):
    for user in users:
        if(user["sicil"] == sicil_id):
            return user
    return None

# update ui after each operations.
window.mainloop()