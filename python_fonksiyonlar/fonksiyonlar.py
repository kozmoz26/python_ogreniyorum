


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

def matematiksel_islem_fonksiyonu(islem:Any, sayilarin_listesi:Any):
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





















