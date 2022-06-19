
from fonksiyonlar import matematiksel_islem_fonksiyonu
from fonksiyonlar import islemi_sor
from fonksiyonlar import sayi_dizisini_olustur

#islemi soralım
islem = islemi_sor()

#sayı listesini oluşturalım
sayilar_listesi = sayi_dizisini_olustur()

#isleme ve sayı listesine göre metamatiksel işlemi gerçekleştirelim
sonuc = matematiksel_islem_fonksiyonu (islem,sayilar_listesi)

#sonucu ekrana yazalım
print (sonuc)

















