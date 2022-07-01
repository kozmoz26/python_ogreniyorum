



class LiblaryMember:
    def __init__(self, adi, soyadi, membertype):
        self.adi = adi
        self.soyadi=soyadi
        self.membertype=membertype

adi=input("adınızı giriniz")
soyadi=input("soyadınızı giriniz")
telefon_numarasi=input("telefon numaranızı giriniz")
membertype="user"
member=LiblaryMember(adi, soyadi,membertype)



class Liblarian:

    def lend_book():
        pass

    def take_back_book():
        pass

    def show_book():
        pass

    def verify_member():
        pass
    def create_fine():   
        pass


class Liblary:
    def __init__(self,books,library_members):
        self.books=books
        self.library_member=library_members
        
    def get_books():
        pass

    def get_reader():
        pass

class Book:
    def __init__(self,title,published_year,author,publisher):
        self.title=title
        self.published_year=published_year
        self.author=author
        self.publisher=publisher






        





