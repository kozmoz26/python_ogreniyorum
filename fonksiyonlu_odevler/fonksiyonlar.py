

#matematiksel islem fonksiyonları
from typing import Any


def islemi_sor():
    #islemi soran kod
    islem=input("yapacağınız işlemi seçin (toplama(+),çıkarma(-),bölme(/),çarpma(*) çıkmak için \"quit\" yazın :")
    return islem


def sayi_dizisini_olustur():
    #sayı sayısını bulan kod
    islemdeki_sayilarin_sayisi=int(input("yapacağınız işlemde kaç sayı istiyorsunuz :"))
    sayilar_listesi=[]
    i=0
    while i<islemdeki_sayilarin_sayisi:
        sayi=int(input("sayı nedir :"))
        sayilar_listesi.append(sayi)  
        i+=1
    return sayilar_listesi

def matematiksel_islem_fonksiyonu(islem:str, sayilarin_listesi:list):
    #matematiksel işlem
    donguya_ilk_kezmi_giriyoruz=True
    for sayi in sayilarin_listesi:
        if donguya_ilk_kezmi_giriyoruz==True:  
            x=sayi
            donguya_ilk_kezmi_giriyoruz=False 
        else:
            if islem=="+":
                x=x+sayi
            elif islem=="-":
                x=x-sayi
            elif islem=="/":
                x=x/sayi
            else:
                x=x*sayi
    return x



#blackjack fonksiyonları

def kart_ver():
    import random
    kart=random.randint(2,11)
    return kart


def puan_soyle(hangi_oyuncu:str, puan:int):
    print(hangi_oyuncu, "oyuncunun puanı",puan)


def kart_cek():    
    kart_cekmek=input("1. oyuncu kart çekmek istiyormusunuz(E yada H) : ")
    if kart_cekmek=="E":
        cekilen_kart=kart_ver()
        print("çektiğiniz kart",cekilen_kart)
    else:
        print("kart çekilmedi\n sıra 2. oyuncuda")
    return cekilen_kart


def puan_hesapla(cekilen_kart:int):    
    oyuncunun_puani=cekilen_kart+oyuncunun_puani
    print(oyuncunun_puani)