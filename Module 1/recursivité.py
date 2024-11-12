


def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n-1)
    
#print(factorielle(5)) # 120
#print (factorielle(3)) # 1
 

def pgfc(a, b):
    if b == 0:
        return a
    else:
        return pgfc(b, a % b)
    
print(pgfc(12, 15)) # 3

def paire(n):
    return n % 2 == 0


def afficheRecursif(n, pos):
    print(n[pos])
    if pos < len(n)-1:
        afficheRecursif(n, pos+1)

def checheRecursif(n, pos, val):
    if n[pos] == val:
        return True
    elif pos < len(n)-1:
        return checheRecursif(n, pos+1, val)
    else:
        return False
    

def rechercheBinaire(liste, d, f, val):
    if d > f:
        return -1
    m = (d + f) // 2
    if liste[m] == val:
        return m
    elif val > liste[m]:
        return rechercheBinaire(liste, m+1, f, val)
    else:
        return rechercheBinaire(liste, d, m-1, val)
    

rechercheBinaire([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9, 5) # 4