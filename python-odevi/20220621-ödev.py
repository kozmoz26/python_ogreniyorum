
import random
from re import T

tablo = []*2
renk=["yeşil","mavi","kırmızı","siyah"]

#Tabloyu oluşturalım
yatay = 1
while yatay < 11:
    dikey = 1
    while dikey < 11:
        tablo[yatay][dikey]="bos"
        dikey = dikey+1
    yatay = yatay+1

#10 tane ördek ekleyelim
ordek= 0
while ordek < 10:
    x = random.randint(1,11)
    y = random.randint(1,11)
    if(tablo[x][y]=="bos"):
        tablo[x][y]=random.choice(renk)
        ordek = ordek+1

#ördeklere ateş etmeye başlayalım
bit = False
puan=0
tekrar = 1
vurulan = 0
while tekrar<11:
    x=input("enlemde kaçıncı noktayı vurmak istiyorsunuz(1 den 10 a kadar)")
    y=input("boylamda kaçıncı noktayı vurmak istiyorsunuz(1 den 10 a kadar)")
    if tablo[x][y]!="bos":
        if tablo[x][y]=="mavi":
            p= 1000
        elif tablo[x][y]=="kırmızı":
            p=0
        elif tablo[x][y]=="yeşil":
            p=5000
        if tablo[x][y]=="siyah":
            p=500
    else:
        print("Tüh ördek vuramadın!")

    puan=puan+p
    vurulan = vurulan+1
    
    tekrar = tekrar+1




    # ordekler = {
    #     "renk": ordek_renk,
    #     "puan": int,
    #     "vuruldu": any
    #     }

    # if ordek_renk=="mavi":
    #     ordekler["puan"]=1000

    # if ordek_renk=="kırmızı":
    #     ordekler["puan"]=0

    # if ordek_renk=="yeşil":
    #     ordekler["puan"]=5000

    # if ordek_renk=="siyah":
    #     ordekler["puan"]=500
    # x=ordekler["puan"]

    # if vurulan_y and vurulan_x==x_kordinati and y_kordinati:
    #         ordekler["vuruldu"]=True
    # else:
    #         ordekler["vuruldu"]=False

    # if ordekler["vuruldu"]==False:
    #         ordekler.pop("puan",)


    # print(ordekler)

    # i+=1
    # if i==10:
    #     bit=True
    #     break





