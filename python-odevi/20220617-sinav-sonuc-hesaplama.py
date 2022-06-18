"""
bir öğrenci iki sınava giriyor ilk sınavın nota etkisi %40 ikincisinin %60
geçme notu:%50
ikinci sınavdan en az 50 almak zorunda
öğrencinin geçme kalma durumunu bulan bir kod yaz
"""

#öğrencinin sınavdan kaç aldığını öğrenen bir kod
ilk_sinav_sonucu=int(input("ilk sınavdan kaç aldınız"))
ikinci_sinav_sonucu=int(input("ikinci sınavdan kaç aldınız"))

#öğrencinin ikinci sınavdan 50 altı alma sonucunda sınıfta kalma durumu
if ikinci_sinav_sonucu<50:
    print("sınıfta kaldınız")

#sınavların puanını hesapla
ilk_sinavin_yuzdesi=ilk_sinav_sonucu*0.10
ilk_sinav_puani=ilk_sinav_sonucu - ilk_sinavin_yuzdesi

ikinci_sinavin_yuzdesi=ikinci_sinav_sonucu*0.10
ikinci_sinav_puani=ikinci_sinav_sonucu + ikinci_sinavin_yuzdesi

#ortalamasını bul
sinavlarin_toplami=ilk_sinav_puani+ikinci_sinav_puani
ortalama=sinavlarin_toplami/2
#geçme/kalma durmunu bul
if ortalama<50:
    print("sınıfta kaldınız")   
else:
    print("tebrikler,", ortalama ,"ile sınıftan geçtiniz")



