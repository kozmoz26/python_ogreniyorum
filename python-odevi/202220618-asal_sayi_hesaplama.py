#1 den 100 e kadar olan asal sayıları getiren bir kod yaz

#1 den 100 e kadar sayıları kontrol et ( 1 hariç, 100 dahil)
for sayi in range(1,101):  

    #sayı birden büyük olmalı. 1 asal değil
    if sayi > 1:  

        #ikiden başlayıp sayıya kadar tek tek başka sayıya bölünüyormu kontrol et
        for i in range(2,sayi):  
            if (sayi % i) == 0:  
                #eğer bölnüyorsa yazdırmadan çık
                break  
            
            #bölünmüyorsa asaldır ekrana yazdır
        else:  
            print(sayi)  







