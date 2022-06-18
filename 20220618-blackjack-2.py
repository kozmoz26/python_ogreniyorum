import random

#1. oyuncuya 2 kart ver
birinci_kart=random.randint(2,11)
ikinci_kart=random.randint(2,11)
birinci_oyuncunun_puani=birinci_kart+ikinci_kart

#2. oyuncuya 2 kart ver
birinci_kart=random.randint(2,11)
ikinci_kart=random.randint(2,11)
ikinci_oyuncunun_puani=birinci_kart+ikinci_kart

#1. ve 2. oyunculara puanlarını söyle
print("birinci oyuncunun puanı",birinci_oyuncunun_puani)
print("ikinci oyuncunun puanı",ikinci_oyuncunun_puani)

kart_istiyormu=0
#while döngüsü içinde çalıştır
while kart_istiyormu<2:

    #birinci oyuncuya kart istiyormu sor
    birinci_oyuncu_kart_cekmek_istiyormu=input("1. oyuncu kart çekmek istiyormusunuz(E yada H) : ")

    #eğer isyorsa
    if birinci_oyuncu_kart_cekmek_istiyormu=="E":
        cekilen_kart=random.randint(2,11)
        print("çektiğiniz kart",cekilen_kart)

        #yeni gelen karta göre 1. oyuncunun puanını hesapla
        birinci_oyuncunun_puani=cekilen_kart+birinci_oyuncunun_puani

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

    #istemiyorsa kart verme
    else:
        print("kart çekilmedi\n sıra 2. oyuncuda")

    #ikinci oyuncuya kart istiyormu sor
    ikinci_oyuncu_kart_cekmek_istiyormu=input("2. oyuncu kart çekmek istiyormusunuz(E yada H) : ")
    #eğer istiyorsa
    if ikinci_oyuncu_kart_cekmek_istiyormu=="E":
        cekilen_kart=random.randint(2,11)
        print("çektiğiniz kart",cekilen_kart)

        #yeni gelen karta göre 2. oyuncunun puanını hesapla
        ikinci_oyuncunun_puani=cekilen_kart+ikinci_oyuncunun_puani

        #21 den büyükse kaybettin yaz
        if ikinci_oyuncunun_puani>21:
            print("1. oyuncu kazandı!")
            kart_istiyormu=2
            break

        #21 e eşitse kazandın yaz
        if ikinci_oyuncunun_puani==21:
            print("2. oyuncu çektiği bu kartla 21 i bulup kazandı")
            kart_istiyormu=2
            break

    #istemiyorsa kart verme
    else:
        print("kart çekilmedi\n sıra 2. oyuncuda")
    if birinci_oyuncu_kart_cekmek_istiyormu=="H" and ikinci_oyuncu_kart_cekmek_istiyormu=="H":
        kart_istiyormu=2


    #1. ve 2. oyunculara puanlarını söyle
    print("birinci oyuncunun puanı",birinci_oyuncunun_puani)
    print("ikinci oyuncunun puanı",ikinci_oyuncunun_puani)

    #ikiside "hayır" cevabını verdiyse oyunu puanları karşılaştır, ekrana yaz ve oyunu bitir