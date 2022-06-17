
"""
bir restoran öğrencilere yiyeceklerde %&40 indirim içeceklerde %50  indirim yapmaktadır bu bilgiye göre fıyat hesaplamsı yapan bir program yaz.
yiyecek:20 tl
içecek:10 tl
öğrencilerin ve indirimleri fiyatlara göre hesapla
"""

#yiyecek ve içecek sayısını soran kod
yiyecek_sayisi=int(input("kaç tane yiyecek satın alacaksınız"))
icecek_sayisi=int(input("kaç tane içecek satın alacaksınız"))



#yiyeceğin indirimini hesaplayan kod
yiyecek_indirim=0.40
yiyecek_fiyat=20
yiyecegin_indirimi=(yiyecek_fiyat*yiyecek_indirim)
yiyecek_indirimli_fiyat=(yiyecek_fiyat-yiyecegin_indirimi)
toplam_yiyecek_fiyati=(yiyecek_indirimli_fiyat*yiyecek_sayisi)

#içeceğin indirimini hesaplayan kod
icecek_indirim=0.50
icecek_fiyat=10
icecegin_indirimi=(icecek_fiyat*icecek_indirim)
icecek_indirimli_fiyat=(icecek_fiyat-icecegin_indirimi)
toplam_icecek_fiyati=(icecek_indirimli_fiyat*icecek_sayisi)

#toplam fiyatı hesaplayan kod

toplam_fiyat=int(toplam_icecek_fiyati+toplam_yiyecek_fiyati)

print(toplam_fiyat,"lira")

