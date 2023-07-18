import tkinter as tk

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


# menu functions for dynamic ui changing
def add_book():
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    # frm_add_book
    frame = tk.Frame(master=frm_main_page, relief="groove", borderwidth=3)
    frame.grid(row=0, column=0, sticky="nw")

    lbl_baslik = tk.Label(master=frame, text="Kitap Adi", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    ent_baslik = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_baslik.grid(row=0, column=0, sticky="ew", padx=5)
    ent_baslik.grid(row=0, column=1)

    lbl_yazar = tk.Label(master=frame, text="Yazar", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    ent_yazar = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_yazar.grid(row=1, column=0, sticky="ew", padx=5)
    ent_yazar.grid(row=1, column=1)
    
    lbl_barkod = tk.Label(master=frame, text="Barkod No", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    ent_barkod = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_barkod.grid(row=2, column=0, sticky="ew", padx=5)
    ent_barkod.grid(row=2, column=1)
    
    button = tk.Button(master=frame, text="Kitap Ekle", command= lambda: btn_add_book(ent_baslik, ent_yazar, ent_barkod))
    button.grid(row=3, column=1, sticky="e", ipadx=5, ipady=5)

def add_user():
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    # frm_add_book
    frame = tk.Frame(master=frm_main_page, relief="groove", borderwidth=3)
    frame.grid(row=0, column=0, sticky="nw")

    lbl_ad = tk.Label(master=frame, text="Ad", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    ent_ad = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_ad.grid(row=0, column=0, sticky="ew", padx=5)
    ent_ad.grid(row=0, column=1)

    lbl_soyad = tk.Label(master=frame, text="Soyad", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    ent_soyad = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_soyad.grid(row=1, column=0, sticky="ew", padx=5)
    ent_soyad.grid(row=1, column=1)

    lbl_sicil = tk.Label(master=frame, text="Sicil No", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    ent_sicil = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_sicil.grid(row=2, column=0, sticky="ew", padx=5)
    ent_sicil.grid(row=2, column=1)

    lbl_sinif = tk.Label(master=frame, text="Sinifi", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    ent_sinif = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    lbl_sinif.grid(row=3, column=0, sticky="ew", padx=5)
    ent_sinif.grid(row=3, column=1)

    button = tk.Button(master=frame, text="Kullanici Ekle", command=lambda: btn_add_user(ent_ad, ent_soyad, ent_sicil, ent_sinif))
    button.grid(row=4, column=1, sticky="e", ipadx=5, ipady=5)
def lend_book():
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    frm_main_page.columnconfigure(1, minsize=300, weight=1)

    # frame for scanning barcode. includes; lbl_barcode, ent_barcode, btn_barcode_add
    frm_barcode = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frm_barcode.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    lbl_barcode = tk.Label(frm_barcode, text="Barcode", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10)
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
        "Baslik": last_item["baslik"],
        "Yazar": last_item["yazar"],
        "Barkod No": last_item["barkod"],
        "Durumu": last_item["status"]
    }
    
    frm_book_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_info.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_book.items()):
        frame = tk.Frame(frm_book_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=10)
        key.grid(row=index, column=0)
        value.grid(row=index, column=1)
        frame.pack(fill=tk.X)

    # frame for searching user. includes; lbl_sicil_no, ent_sicil_no, btn_search_user_by_sicil_no
    frm_searc_user = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_searc_user.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    lbl_sicil_no = tk.Label(frm_searc_user, text="Sicil No", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10)
    lbl_sicil_no.pack(side=tk.LEFT)
    ent_sicil_no = tk.Entry(frm_searc_user, width=20, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_sicil_no.pack(side=tk.LEFT)
    btn_search_user = tk.Button(frm_searc_user, text="Kullanici Ara", width=10, command=lambda: btn_user_search_by_sicil(ent_sicil_no))
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
            "Sinif": last_user["sinif"]
        }

    frm_user_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_user_info.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_user.items()):
        frame = tk.Frame(frm_user_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=10)
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
        lbl = tk.Label(frame, text=item["baslik"])
        btn = tk.Button(frame, text="Remove", command=lambda: print(f"Book {i} sepetten cikarildi."))
        lbl.pack(side="left", fill=tk.X)
        btn.pack(side="right", ipadx=1, ipady=1)
        frame.pack(fill=tk.X)
    # frame for Operation Button. includes; btn_lend_book
    btn_lend_book = tk.Button(frm_main_page, text="Teslim Et", command=lambda: print("Teslim et tusuna basildi."))
    btn_lend_book.grid(row=21, column=1, sticky="ew", ipadx=5, ipady=5)

def return_book():
    # update main layout
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    frm_main_page.columnconfigure(1, minsize=300, weight=1)
    

    # frame for scanning barcode. includes; lbl_barcode, ent_barcode, btn_barcode_add
    frm_barcode = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frm_barcode.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    lbl_barcode = tk.Label(frm_barcode, text="Barcode", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10)
    lbl_barcode.pack(side=tk.LEFT)
    ent_barcode = tk.Entry(frm_barcode, width=20, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_barcode.pack(side=tk.LEFT)
    btn_barcode_search = tk.Button(frm_barcode, text="Sepete Ekle", width=10, command=lambda: print(f"barcode {ent_barcode.get()} sorgulandi. bulunan kitap sepete eklendi."))
    btn_barcode_search.pack(side=tk.LEFT, ipadx=5, ipady=5)

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    the_book = {
        "Baslik": "Kumarbaz",
        "Yazar": "Dostoyevski",
        "Barkod No": "123456789",
        "Durumu": "Mevcut"
    }
    frm_book_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_info.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_book.items()):
        frame = tk.Frame(frm_book_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=10)
        key.grid(row=index, column=0)
        value.grid(row=index, column=1)
        frame.pack(fill=tk.X)

    # frame for searching user. includes; lbl_sicil_no, ent_sicil_no, btn_search_user_by_sicil_no
    frm_searc_user = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_searc_user.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    lbl_sicil_no = tk.Label(frm_searc_user, text="Sicil No", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10)
    lbl_sicil_no.pack(side=tk.LEFT)
    ent_sicil_no = tk.Entry(frm_searc_user, width=20, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_sicil_no.pack(side=tk.LEFT)
    btn_search_user = tk.Button(frm_searc_user, text="Kullanici Ara", width=10, command=lambda: print(f"sicil_no {ent_sicil_no.get()} sorgulandi. kullanici bilgileri ekranda gosteriliyor."))
    btn_search_user.pack(side=tk.LEFT, ipadx=5, ipady=5)

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    the_user = {
        "Ad": "Kadir",
        "Soyad": "KAYA",
        "Sicil No": "7385",
        "Sinif": "Personel"
    }
    frm_user_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_user_info.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    for index, (key, value) in enumerate(the_user.items()):
        frame = tk.Frame(frm_user_info, relief="sunken", borderwidth=1)
        key = tk.Label(frame, text=key, bg="#85A389", fg="white", width=10)
        value = tk.Label(frame, text=value, bg="#F1C27B", fg="black", width=10)
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
    for i in range(20):
        frame = tk.Frame(frm_book_box, relief="raised", borderwidth=1)
        lbl = tk.Label(frame, text=f"Book {i} title of the penguin")
        btn = tk.Button(frame, text="Remove", command=lambda: print(f"Book {i} sepetten cikarildi."))
        lbl.pack(side="left", fill=tk.X)
        btn.pack(side="right", ipadx=1, ipady=1)
        frame.pack(fill=tk.X)
    # frame for Operation Button. includes; btn_lend_book
    btn_return_book = tk.Button(frm_main_page, text="Iade Al", command=lambda: print("Iade Al tusuna basildi."))
    btn_return_book.grid(row=21, column=1, sticky="ew", ipadx=5, ipady=5)

def other_operations():
    pass

menu_items = {
    "Add Book": add_book,
    "Add User": add_user,
    "Lend Book": lend_book,
    "Return Book": return_book,
    "Other Operations": other_operations,
    "Kadir Operations": other_operations
}

# add menu items
for i, (title, func) in enumerate(menu_items.items()):
    button = tk.Button(master=frm_menu, text=title, command=func)
    button.grid(row=i, column=0, sticky="wens", ipadx=5, ipady=5, pady=5)



# parameter definitions
users = [] # keeps all user who registered to library.
books = [] # keeps all book information which belongs to library.
lendings = [] # keeps all lending records book by book.

lending_box = [] # lend book sayfasinda barkod taramasi yapildiginda eslesen kitaplar buraya eklenir.
returning_box = [] # return book barkod taramasi yapildiginda eslesen kitaplar buraya eklenir.
searched_user = []
# additional functions
def btn_add_book(baslik, yazar, barkod):
    print(baslik.get(), yazar.get(), barkod.get())
    new_book = {
        "id": len(books),
        "baslik": baslik.get(),
        "yazar": yazar.get(),
        "barkod": barkod.get(),
        "status": "Mevcut"
    }
    books.append(new_book)
    # delete entries
    baslik.delete(0, tk.END)
    yazar.delete(0, tk.END)
    barkod.delete(0, tk.END)

    print("books")
    for book in books:
        print(book)

# parametre olarak gelen veriler Entry objesidir. Icerideki degisiklikler formu etkilemektedir.
def btn_add_user(ad, soyad, sicil, sinif):
    print(ad.get(), soyad.get(), sicil.get(), sinif.get())
    new_user = {
        "id": len(users),
        "ad": ad.get(),
        "soyad": soyad.get(),
        "sicil": sicil.get(),
        "sinif": sinif.get()
    }
    users.append(new_user)
    ad.delete(0, tk.END)
    soyad.delete(0, tk.END)
    sicil.delete(0, tk.END)
    sinif.delete(0, tk.END)
    print("users")
    for user in users:
        print(user)

def btn_add_box_of_book(ent_barkod):
    barkod = ent_barkod.get()
    # books listesinde aranacak.
    for book in books:
        if(book["barkod"] == barkod):
            lending_box.append(book)
            print(book)
            lend_book()
            return
    print(f"barkod: {barkod} numarali kitap kayitlarda bulunamadi.")
def btn_user_search_by_sicil(ent_sicil):
    sicil_no = ent_sicil.get()
    for user in users:
        if(user["sicil"] == sicil_no):
            searched_user.append(user)
            print(user)
            lend_book()
            return
    print(f"sicil: {sicil_no} numarali kullanici kayitlarda bulunamadi.")

window.mainloop()