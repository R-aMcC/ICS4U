import time
import sys

title = "Conversion de masse en force"
print(f"{title:^60}")
while True:
    inp = input("Quel est ta masse? (kg): ")
    try:
        kg = float(inp)
        break
    except:
        print("[ERREUR] Entre un nombre réelle \nInput: "+inp)



i = 0
print()
while i<10 :
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.5)
    i+=1


print()

print(f"\nLa force que tu exerce sur la terre est égale à la masse fois la force gravitationelle terreste de 9,81\nTu excerce une force de {round(kg*9.81)}N sur la terre.")