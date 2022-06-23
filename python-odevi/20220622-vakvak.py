
import random


#10 tane ördek sözlüğü
ordek={
"renk": str,
"puan": int,
"vuruldu": "vurulmadı",
"x":random.randint(1,6),
"y":random.randint(1,6)
}
ordek2={
"renk": str,
"puan": int,
"vuruldu": "vurulmadı",
"x":random.randint(1,6),
"y":random.randint(1,6)
}
ordek3={
"renk": str,
"puan": int,
"vuruldu": "vurulmadı",
"x":random.randint(1,6),
"y":random.randint(1,6)
}
ordek4={
"renk": str,
"puan": int,
"vuruldu": "vurulmadı",
"x":random.randint(1,6),
"y":random.randint(1,6)
}

ordekler={
"ordek1":ordek,
"ordek2":ordek2,
"ordek3":ordek3,
"ordek4":ordek4,
}

#ördeklerin rengini ve puanını bul
renk=["kırmızı","mavi","yeşil","siyah"]

ordek1_rengi=random.choice(renk)
ordek["renk"]=ordek1_rengi 

ordek2_rengi=random.choice(renk)
ordek2["renk"]=ordek2_rengi

ordek3_rengi=random.choice(renk)
ordek3["renk"]=ordek3_rengi

ordek4_rengi=random.choice(renk)
ordek4["renk"]=ordek4_rengi

#ördekleri vur
ordek1_kordinati=[ordek["x"], ordek["y"]]
ordek2_kordinati=[ordek2["x"], ordek2["y"]]
ordek3_kordinati=[ordek3["x"], ordek3["y"]]
ordek4_kordinati=[ordek4["x"], ordek4["y"]]
print(ordek1_kordinati)
print(ordek2_kordinati)
print(ordek3_kordinati)
print(ordek4_kordinati)
i=0
while i<4:
    vurulan_x_kordinati=int(input("1 ile 5 arası enlemde hangi noktayı vurmak istediğinizi yazın : "))
    vurulan_y_kordinati=int(input("1 ile 5 arası boylamda hangi noktayı vurmak istediğini yazın : "))
    vurulan_kordinat=[vurulan_x_kordinati, vurulan_y_kordinati]
    if vurulan_kordinat==ordek1_kordinati:
        ordek["vuruldu"]="vuruldu"
    if vurulan_kordinat== ordek2_kordinati:
        ordek2["vuruldu"]="vuruldu"
    if vurulan_kordinat== ordek3_kordinati:
        ordek3["vuruldu"]="vuruldu"
    if vurulan_kordinat==ordek4_kordinati:
        ordek4["vuruldu"]="vuruldu"
    i=i+1


#ördeklerin puanini sözlüğe yazdır
ordek1_puani=ordek1_rengi
ordek2_puani=ordek2_rengi
ordek3_puani=ordek3_rengi
ordek4_puani=ordek4_rengi
if ordek1_puani=="kırmızı":
    ordek["puan"]=0
if ordek1_puani=="mavi":
    ordek["puan"]=1000
if ordek1_puani=="yeşil":
    ordek["puan"]=5000    
if ordek1_puani=="siyah":
    ordek["puan"]=500

if ordek2_puani=="kırmızı":
    ordek2["puan"]=0
if ordek2_puani=="mavi":
    ordek2["puan"]=1000
if ordek2_puani=="yeşil":
    ordek2["puan"]=5000    
if ordek2_puani=="siyah":
    ordek2["puan"]=500

if ordek3_puani=="kırmızı":
    ordek3["puan"]=0
if ordek3_puani=="mavi":
    ordek3["puan"]=1000
if ordek3_puani=="yeşil":
    ordek3["puan"]=5000    
if ordek3_puani=="siyah":
    ordek3["puan"]=500

if ordek4_puani=="kırmızı":
    ordek4["puan"]=0
if ordek4_puani=="mavi":
    ordek4["puan"]=1000
if ordek4_puani=="yeşil":
    ordek4["puan"]=5000    
if ordek4_puani=="siyah":
    ordek4["puan"]=500

print(ordek)
print(ordek2)
print(ordek3)
print(ordek4)






 