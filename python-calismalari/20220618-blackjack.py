#blackcheck oyununu kodla

import random
oyuncu1_kart_sayisi=0
oyuncu2_kart_sayisi=0

x=0
while x==0:

        #oyuncu 1 in kart çekme kodu
    kart_cekme_oyuncu1=str(input("kart çekmek istermisiniz(evet , hayır) \n"))
            
    if kart_cekme_oyuncu1=="evet":
            oyuncu1_cekilen_kart=int(random.uniform(2,11))
            oyuncu1_kart_sayisi=oyuncu1_cekilen_kart+oyuncu1_kart_sayisi
            print(oyuncu1_cekilen_kart,"çektiniz yeni kart sayınız",oyuncu1_kart_sayisi,"\n" )
    if oyuncu1_kart_sayisi==21:
        print("OYUNCU 1 KAZANDI!")
        x=1
        break
    if oyuncu1_kart_sayisi>=21:
        print("OYUNCU 2 KAZANDI!")
        x=1  
        break
    print("sıra 2. oyuncuda")
    if kart_cekme_oyuncu1=="hayır":
        print("kart çekilmedi \nsıra 2. oyucunda\n")


        #oyuncu 2 nin kart çekme kodu
    kart_cekme_oyuncu2=str(input("kart çekmek istermisiniz(evet , hayır) \n"))
             
    if kart_cekme_oyuncu2=="evet":
            oyuncu2_cekilen_kart=int(random.uniform(2,11))
            oyuncu2_kart_sayisi=oyuncu2_cekilen_kart+oyuncu2_kart_sayisi
            print(oyuncu2_cekilen_kart,"çektiniz yeni kart sayınız",oyuncu2_kart_sayisi,"\n" )
    if oyuncu2_kart_sayisi==21:
        print("OYUNCU 2 KAZANDI!")
        x=1
        break
    if oyuncu2_kart_sayisi>=21:
        print("OYUNCU 1 KAZANDI!")
        x=1       
        break
    print("sıra 1. oyuncuda")
    if kart_cekme_oyuncu2=="hayır":
        print("kart çekilmedi \nsıra 1. oyucunda\n")







