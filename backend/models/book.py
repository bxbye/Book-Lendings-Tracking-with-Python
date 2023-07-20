class Book:
    def __init__(self, id, baslik, yazar, barkod, status="available"):
        self.id = id
        self.baslik = baslik
        self.yazar = yazar
        self.barkod = barkod
        self.status = status