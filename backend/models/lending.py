import datetime


class Lending:
    def __init__(self, id, user_sicil, book_barkod, lent_date):
        self.id = id
        self.user_sicil = user_sicil
        self.book_barkod = book_barkod
        self.status = "lent"
        self.lent_date = lent_date
        self.returned_date = None
        