"""
hesap makinesi yap
toplama çıkarma vs. hepsi olsun ve program bitmesin tekrar tekrar çalıştırabilsin
bir tuşa basılınca programdan çıkılabilsin
""" 


islem=input("yapacağınız işlemi seçin(\"toplama\",\"cıkarma\",\"bolme\",\"carpma\")")

islemdeki_sayilarin_sayisi=int(input("yapacağınız işlemde kaç sayı istiyorsunuz"))
sayilar=[]
i=0
while i<islemdeki_sayilarin_sayisi:
    
    x=int(input("sayı nedir"))
    sayilar.append(x)
    i+=1

toplam=0
if islem=="toplama":
    for x in sayilar:
        toplam=toplam+x
    print(toplam)
    print(sayilar)