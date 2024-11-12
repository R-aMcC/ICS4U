import random




print(f"{"Simulation d'un tirage":-^45}")
nombres = [int(input("Nombre 1 (0-9):")), int(input("Nombre 2 (0-9):")), int(input("Nombre 3 (0-9):"))]
guessNombres = [-1, -1, -1]
count = 0
while nombres != guessNombres:
    guessNombres = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]
    count += 1
print(f"La combinaison était vraie après {count} essaies")
