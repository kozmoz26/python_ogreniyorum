
import keyboard
import time

notalar=("do","re","mi","fa","sol","la","si")
(d, r, m, f, s, l, ş ) = notalar

bit = False
while bit == False:
    basilan = keyboard.read_key()
    if basilan == "d":
        print(d)
    if basilan == "r":
        print(r)
    if basilan == "m":
        print(m)    
    if basilan == "f":
        print(f)
    if basilan == "s":
        print(s)
    if basilan == "l":
        print(l)
    if basilan == "ş":
        print(ş)
    if basilan=="q":
        bit = True
        break
    time.sleep(0.20)









