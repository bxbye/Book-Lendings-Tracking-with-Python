import tkinter as tk

# main frame
window = tk.Tk()
window.title("BANDO EYM OTOMASYON YAZILIMI")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=0)

# frm_menu
frm_menu = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2)

# frm_main_page which involves menu pages.
frm_main_page = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2)

frm_menu.grid(row=0, column=0, sticky="nswe")
frm_main_page.grid(row=0, column=1, sticky="nswe")


def add_book():
    print("destroy all frames inside of frm_main_page")
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    # frm_add_book
    frame = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frame.pack()
    book_labels = [
        "Kitap Adi",
        "Yazar",
        "Barkod No"
    ]
    for index, item in enumerate(book_labels):
        label = tk.Label(master=frame, text=item, bg="#85A389", fg="white", relief="raised", borderwidth=2)
        entry = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
        label.grid(row=index, column=0, sticky="ew", padx=5)
        entry.grid(row=index, column=1)
    button = tk.Button(master=frame, text="Kitap Ekle")
    button.grid(row=len(book_labels), column=1, sticky="e", ipadx=5, ipady=5)

def add_user():
    print("destroy all frames inside of frm_main_page")
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    # frm_add_book
    frame = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frame.pack()
    user_labels = [
        "Ad",
        "Soyad",
        "Sicil No",
        "Sinifi"
    ]
    for index, item in enumerate(user_labels):
        label = tk.Label(master=frame, text=item, bg="#85A389", fg="white", relief="raised", borderwidth=2)
        entry = tk.Entry(master=frame, width=50, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
        label.grid(row=index, column=0, sticky="ew", padx=5)
        entry.grid(row=index, column=1)
    button = tk.Button(master=frame, text="Kullanici Ekle")
    button.grid(row=len(user_labels), column=1, sticky="e", ipadx=5, ipady=5)
def lend_book():
    print("destroy all frames inside of frm_main_page")
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    
    frm_main_page.rowconfigure([0,1,2], minsize=100, weight=1)
    frm_main_page.columnconfigure(1, minsize=200, weight=1)
    
    # frame for scanning barcode. includes; lbl_barcode, ent_barcode, btn_barcode_add
    frm_barcode = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frm_barcode.grid(row=0, column=0, sticky="ewns")

    lbl_barcode = tk.Label(frm_barcode, text="Barcode:", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    lbl_barcode.grid(row=0, column=0, sticky="ew")
    ent_barcode = tk.Entry(frm_barcode, width=30, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_barcode.grid(row=0, column=1)
    btn_barcode_search = tk.Button(frm_barcode, text="Sepete Ekle", command=lambda: print(f"barcode {ent_barcode.get()} sorgulandi. bulunan kitap sepete eklendi."))
    btn_barcode_search.grid(row=1, column=1, sticky="e", ipadx=5, ipady=5)
    # frame for searching user. includes; lbl_sicil_no, ent_sicil_no, btn_search_user_by_sicil_no
    frm_searc_user = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_searc_user.grid(row=1, column=0, sticky="ewns")

    lbl_sicil_no = tk.Label(frm_searc_user, text="Sicil No:", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    lbl_sicil_no.grid(row=0, column=0, sticky="ew")
    ent_sicil_no = tk.Entry(frm_searc_user, width=30, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_sicil_no.grid(row=0, column=1)
    btn_search_user = tk.Button(frm_searc_user, text="Kullanici Ara", command=lambda: print(f"sicil_no {ent_sicil_no.get()} sorgulandi. kullanici bilgileri ekranda gosteriliyor."))
    btn_search_user.grid(row=1, column=1, sticky="e", ipadx=5, ipady=5)
    
    # frame for book box. includes; lbl_book_name, btn_remove_book
    frm_book_box = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_box.grid(row=0, column=1, sticky="nsew", rowspan=4)
    # this frame will iclude added books's name and remove button for each.
    # otherwise, "Sepete henuz kitap eklenmedi." mesaji gosterilsin.
    for i in range(3):
        lbl = tk.Label(frm_book_box, text=f"Book {i} title of the penguin")
        btn = tk.Button(frm_book_box, text="Remove", command=lambda: print(f"Book {i} sepetten cikarildi."))
        lbl.grid(row=i, column=0, columnspan=4, sticky="e")
        btn.grid(row=i, column=4, sticky="e")

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    frm_user_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_user_info.grid(row=2, column=0, sticky="nswe")
    lbl_user_sicil_no = tk.Label(frm_user_info, text="7385")
    lbl_user_name = tk.Label(frm_user_info, text="Kadir KAYA")
    lbl_user_sicil_no.grid(row=0, column=0)
    lbl_user_name.grid(row=0, column=1)
        ## this frame will include user informations.
        # otherwise, "Hicbir kullanici secilmedi." mesaji gosterilsin.
    # frame for Operation Button. includes; btn_lend_book
    btn_lend_book = tk.Button(frm_main_page, text="Teslim Et", command=lambda: print("Teslim et tusuna basildi."))
    btn_lend_book.grid(row=3, column=0, sticky="e", ipadx=5, ipady=5)

    pass
def return_book():
    print("destroy all frames inside of frm_main_page")
    for widget in frm_main_page.winfo_children():
        widget.destroy()
    
    frm_main_page.rowconfigure([0,1,2], minsize=100, weight=1)
    frm_main_page.columnconfigure(1, minsize=200, weight=1)
    
    # frame for scanning barcode. includes; lbl_barcode, ent_barcode, btn_barcode_add
    frm_barcode = tk.Frame(master=frm_main_page, relief="ridge", borderwidth=3)
    frm_barcode.grid(row=0, column=0, sticky="ewns")

    lbl_barcode = tk.Label(frm_barcode, text="Barcode:", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    lbl_barcode.grid(row=0, column=0, sticky="ew")
    ent_barcode = tk.Entry(frm_barcode, width=30, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_barcode.grid(row=0, column=1)
    btn_barcode_search = tk.Button(frm_barcode, text="Sepete Ekle", command=lambda: print(f"barcode {ent_barcode.get()} sorgulandi. bulunan kitap sepete eklendi."))
    btn_barcode_search.grid(row=1, column=1, sticky="e", ipadx=5, ipady=5)
    # frame for searching user. includes; lbl_sicil_no, ent_sicil_no, btn_search_user_by_sicil_no
    frm_searc_user = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_searc_user.grid(row=1, column=0, sticky="ewns")

    lbl_sicil_no = tk.Label(frm_searc_user, text="Sicil No:", bg="#85A389", fg="white", relief="raised", borderwidth=2)
    lbl_sicil_no.grid(row=0, column=0, sticky="ew")
    ent_sicil_no = tk.Entry(frm_searc_user, width=30, bg="#F1C27B", fg="black", relief="groove", borderwidth=2)
    ent_sicil_no.grid(row=0, column=1)
    btn_search_user = tk.Button(frm_searc_user, text="Kullanici Ara", command=lambda: print(f"sicil_no {ent_sicil_no.get()} sorgulandi. kullanici bilgileri ekranda gosteriliyor."))
    btn_search_user.grid(row=1, column=1, sticky="e", ipadx=5, ipady=5)
    
    # frame for book box. includes; lbl_book_name, btn_remove_book
    frm_book_box = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_book_box.grid(row=0, column=1, sticky="nsew", rowspan=4)
    # this frame will iclude added books's name and remove button for each.
    # otherwise, "Sepete henuz kitap eklenmedi." mesaji gosterilsin.
    for i in range(3):
        lbl = tk.Label(frm_book_box, text=f"Book {i} title of the penguin")
        btn = tk.Button(frm_book_box, text="Remove", command=lambda: print(f"Book {i} sepetten cikarildi."))
        lbl.grid(row=i, column=0, columnspan=4, sticky="e")
        btn.grid(row=i, column=4, sticky="e")

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name
    frm_user_info = tk.Frame(frm_main_page, relief="ridge", borderwidth=3)
    frm_user_info.grid(row=2, column=0, sticky="nswe")
    lbl_user_sicil_no = tk.Label(frm_user_info, text="7385")
    lbl_user_name = tk.Label(frm_user_info, text="Kadir KAYA")
    lbl_user_sicil_no.grid(row=0, column=0)
    lbl_user_name.grid(row=0, column=1)


    btn_return_book = tk.Button(frm_main_page, text="Iade Al", command=lambda: print("Iade Al tusuna basildi."))
    btn_return_book.grid(row=3, column=0, sticky="e", ipadx=5, ipady=5)

    # frame for scanning barcode. includes; lbl_barcode, ent_barcode, btn_barcode_add

    # frame for searching user. includes; lbl_sicil_no, ent_sicil_no, btn_search_user_by_sicil_no

    # frame for book box. includes; lbl_book_name, btn_remove_book

    # frame_for user information. includes; lbl_user_sicil_no, lbl_user_name

    # frame for Operation Button. includes; btn_return_book
    pass

def other_operations():
    pass

menu_items = {
    "Add Book": add_book,
    "Add User": add_user,
    "Lend Book": lend_book,
    "Return Book": return_book,
    "Other Operations": other_operations
}

# add menu items
for i, (title, func) in enumerate(menu_items.items()):
    button = tk.Button(master=frm_menu, text=title, command=func)
    button.grid(row=i, column=0, sticky="we", ipadx=10, ipady=10)



# frm_main_page will dynamically adjust with menu operations' screen.


# frm_add_user


# frm_lend_book


# frm_return_book






window.mainloop()