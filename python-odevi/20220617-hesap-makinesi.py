"""
hesap makinesi yap
toplama çıkarma vs. hepsi olsun ve program bitmesin tekrar tekrar çalıştırabilsin
bir tuşa basılınca programdan çıkılabilsin
""" 

#istediğin zaman çıkmanı ve kodun loopta olmasını sağlayan kod
from re import T


quit=0
while quit==0:
    islem=input("yapacağınız işlemi seçin (toplama(+),çıkarma(-),bölme(/),çarpma(*) çıkmak için \"quit\" yazın :")
    if islem=="quit":
        quit=1
    else:
        #sayı sayısını bulan kod
        islemdeki_sayilarin_sayisi=int(input("yapacağınız işlemde kaç sayı istiyorsunuz :"))
        sayilar_listesi=[]
        i=0
        while i<islemdeki_sayilarin_sayisi:
            sayi=int(input("sayı nedir :"))
            sayilar_listesi.append(sayi)
            i+=1

        #toplama
        if islem=="+":
            toplam =0
            for sayi in sayilar_listesi:
                toplam=toplam+sayi
            print(toplam) 

        #çıkartma        
        if islem=="-":
            donguya_ilk_kezmi_giriyoruz=True
            for sayi in sayilar_listesi:
                if donguya_ilk_kezmi_giriyoruz==True:  
                    cikartma=sayi
                    donguya_ilk_kezmi_giriyoruz=False 
                else:
                    cikartma=cikartma-sayi
            print(cikartma) 

        #bölme
        if islem=="/":
            donguya_ilk_kezmi_giriyoruz=True
            for sayi in sayilar_listesi:
                if donguya_ilk_kezmi_giriyoruz==True:
                    bolme=sayi
                    donguya_ilk_kezmi_giriyoruz=False
                else:
                    bolme=bolme/sayi
            print(bolme)
        #çarpma
        if islem=="*":
            donguya_ilk_kezmi_giriyoruz=True
            for x in sayilar_listesi:
                if donguya_ilk_kezmi_giriyoruz==True:
                    carpma=sayi
                    donguya_ilk_kezmi_giriyoruz=False
                else:
                    carpma=carpma*sayi
            print(carpma)





























