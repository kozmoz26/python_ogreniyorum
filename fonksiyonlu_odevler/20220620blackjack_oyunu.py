
from fonksiyonlar import kart_ver
from fonksiyonlar import puan_soyle
from fonksiyonlar import kart_cek
from fonksiyonlar import oyun_bitir

#1. oyuncuya 2 kart ver
birinci_kart=kart_ver()
ikinci_kart=kart_ver()
birinci_oyuncunun_puani=birinci_kart+ikinci_kart

#2. oyuncuya 2 kart ver
birinci_kart=kart_ver()
ikinci_kart=kart_ver()
ikinci_oyuncunun_puani=birinci_kart+ikinci_kart

#1. ve 2. oyunculara puanlarını söyle
puan_soyle("birinci", birinci_oyuncunun_puani)
puan_soyle("ikinci", ikinci_oyuncunun_puani)

kart_istiyormu=0
while kart_istiyormu < 2:

    #yeni gelen karta göre 1. oyuncunun puanını hesapla
    cekilen_kart =  kart_cek("birinci")
    birinci_oyuncunun_puani=cekilen_kart+birinci_oyuncunun_puani
    puan_soyle("birinci", birinci_oyuncunun_puani)
    oyuncu1_istek=kart_cek("birinci")
    #21 den büyükse kaybettin yaz
    if birinci_oyuncunun_puani>21:
        print("2. oyuncu kazandı!")
        kart_istiyormu=2
        break

    #21 e eşitse kazandın yaz
    if birinci_oyuncunun_puani==21:
        print(" 1. oyuncu çektiği bu kartla 21 i bulup kazandı")
        kart_istiyormu=2
        break


    #yeni gelen karta göre 2. oyuncunun puanını hesapla
    cekilen_kart =  kart_cek("ikinci")
    ikinci_oyuncunun_puani=cekilen_kart+ikinci_oyuncunun_puani
    puan_soyle("ikinci", ikinci_oyuncunun_puani)
    oyuncu2_istek=kart_cek("ikinci")
    #21 den büyükse kaybettin yaz
    if ikinci_oyuncunun_puani>21:
        print("1. oyuncu kazandı!")
        kart_istiyormu=2
        break

    #21 e eşitse kazandın yaz
    if ikinci_oyuncunun_puani==21:
        print(" 2. oyuncu çektiği bu kartla 21 i bulup kazandı")
        kart_istiyormu=2
        break
        
    #iki oyuncuda hayır derse oyunu bitir
    oyun_bitir(oyuncu1_istek, oyuncu2_istek)

    #1. ve 2. oyunculara puanlarını söyle
    puan_soyle("birinci", birinci_oyuncunun_puani)
    puan_soyle("ikinci", ikinci_oyuncunun_puani)

    #puanları karşılaştır, ekrana yaz ve oyunu bitir
    if kart_istiyormu==2:
        if birinci_oyuncunun_puani>ikinci_oyuncunun_puani:
            print("birinci oyuncu kazandı")
        elif birinci_oyuncunun_puani==ikinci_oyuncunun_puani:
            print("berabere kaldınız. Dostluk kazandı")
        else:
            print("ikinci oyuncu kazandı")
        















