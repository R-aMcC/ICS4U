import sys
import time


text = ["Voici text #1", "Voici text #2", "Voici text #3"]
text.append("J'adore entrer dans une discussion à propos de n'importe quoi dans les domaines de technologie.")


def printChar(msg):
    for c in msg:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

for i in range(len(text)):
    printChar(text[i])
    print()
