from datetime import datetime
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
    window.title("EYM OTOMASYON - KİTAP EKLEME")
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
    btn_search_user = tk.Button(frm_searc_user, text="Kullanici Ara", width=10, command=lambda: btn_user_search_by_sicil(ent_sicil_no, "lend_screen"))
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
    lbl_barcode = tk.Label(frm_barcode, text="Barcode", bg="#85A389", fg="white", relief="raised", borderwidth=2, width=10)
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
    for i, item in enumerate(returning_box):
        frame = tk.Frame(frm_book_box, relief="raised", borderwidth=1)
        lbl = tk.Label(frame, text=item["baslik"])
        btn = tk.Button(frame, text="Remove", command=lambda: print(f"Book {i} sepetten cikarildi."))
        lbl.pack(side="left", fill=tk.X)
        btn.pack(side="right", ipadx=1, ipady=1)
        frame.pack(fill=tk.X)
    # frame for Operation Button. includes; btn_lend_book
    btn_lend_book = tk.Button(frm_main_page, text="İade Al", command= btn_return_books)
    btn_lend_book.grid(row=21, column=1, sticky="e", ipadx=5, ipady=5)
    btn_clear_box = tk.Button(frm_main_page, text="Sepeti Temizle", command=lambda: [returning_box.clear(), return_book()])
    btn_clear_box.grid(row=21, column=1, sticky="w", ipadx=5, ipady=5)
    # Update the GUI immediately to display the entry widgets
    frm_main_page.update()

def other_operations():
    window.title("EYM OTOMASYON - DİĞER İŞLEMLER")
    pass

menu_items = {
    "Kitap Ekle": add_book,
    "Kullanıcı Ekle": add_user,
    "Kitap Teslimi": lend_book,
    "Kitap İade": return_book,
    "Diğer İşlemler": other_operations,
    "Kadir'in İşlemleri": other_operations
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
lending_service = [] # tum teslim edilen kitaplar icin bu serviste bir dict/object olusturulacaktir.
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
    new_book = {
        "id": len(books),
        "baslik": baslik.get(),
        "yazar": yazar.get(),
        "barkod": barkod.get(),
        "status": "available"
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
    # check blanks are emty or not
    if (not ad.get() or not soyad.get() or not sicil.get() or not sinif.get()):
        print(f"Tum bilgiler doldurulmalidir.")
        return
    # check if books list contains the same book as barkod no
    if any(user.get("sicil") == sicil.get() for user in users):
        print(f"Bu kullanici zaten users listesine eklenmis.")
        return
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
        lending = {
            "id": i,
            "book_barkod": book.get("barkod"),
            "user_sicil": user_to_lend.get("sicil"),
            "status": "lent",
            "lent_date": datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            "returned_date": None
        }
        # lending_service[] adinda bir listede tum kitaplara ve teslim edilen kisiye ait veriler tutulacak.
        lending_service.append(lending)
        # update book status from books
        update_book_status(book.get("barkod"), "unavailable")
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

    # sepettenki her kitap icin tek tek lending_service'den kontrol yapilacak. bu kitap bu kullanici tarafindan mi alinmis?
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
            update_lending_service_status(rb.get("barkod"), user_to_return.get("sicil"), "returned")
            update_book_status(rb.get("barkod"), "available")

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
    for lended_book in lending_service:
        if(lended_book.get("book_barkod") == book_barcode and lended_book.get("user_sicil") == user_sicil):
            return True
    return False #if for loop finishes without return True
def update_lending_service_status(barcode, sicil, status):
    # update status of matched object
    for lended_book in lending_service:
        if(lended_book.get("book_barkod") == barcode and lended_book.get("user_sicil") == sicil):
            lended_book["status"] = status
def update_book_status(barkod, status):
    for book in books:
        if(book.get("barkod") == barkod):
            book["status"] = status
            break
    print(f"{barkod} barkod numarali kitap durumu {status} olarak guncellendi.")
    return
# update ui after each operations.
window.mainloop()