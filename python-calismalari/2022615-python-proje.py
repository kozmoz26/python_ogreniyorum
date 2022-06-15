
import random
import time



# 1)fındık varmı kontrol et
findik=int(input("fındık varsa 1 yoksa 2 ye bas :"))

# 	varsa, fındık var de ve sonraki adıma geç
if (findik==1):
        print("fındık var")
#  	yoksa fındık al
elif (findik==2):
        print("fındık yok.Fındık alın")
elif findik>>2:
        print("lütfen geçerli bir sayı giriniz")
    
    

# 2)fındık kıracağı varmı kontrol et
kiracak=int(input("kıracak varsa 1 yoksa 2 ye bas :"))

# 	varsa:kıracak var yaz ve sonraKi adıma geç
if (kiracak==1):
    print("kıracak var")

# 	yoksa:fındık kıracağı al
else:
    print("kıracak yok.Kıracak alın")

# 3)kaç tane fındık olduğunu sor
findik_sayisi=int(input("kaç tane fındık var?"))

# 4)fındıkları kır
findiklar=[]
findiklar.append(findik_sayisi)
rastgele_sayi=random.randint(2,findik_sayisi)
kirilan_findikler=0
while kirilan_findikler<findik_sayisi:
    time.sleep( 0.25 )
    if(kirilan_findikler==rastgele_sayi):
        print("bu fındık kırılamadı. biraz sert çıktı. Dur bir daha deneyeyim")
    print(kirilan_findikler+1,"fındık kırıldı")
    kirilan_findikler=kirilan_findikler+1
    
# 5)kırdığın fındıkların çöplerini çöpe at
print("fındık kabukları çöpe atıldı")

# 6)fındık kıracağını yerine koy
print("fındık kıracağı yerine koyuldu")










