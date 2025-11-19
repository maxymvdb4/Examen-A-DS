class Player:
    def __init__(self, name:str, number:int):
        self.name = name
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Player) and self.name == other.name:
            return True

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        else:
            if self.number < other.number:
                return True

    def __str__(self):
        return f"{self.name} ({self.number})"

# 1. Creëer drie speler objecten en plaats ze in een lijst.
print("--- 1. Initialisatie ---")
lijst = [
    Player("Maxym", 17),
    Player("Kevin", 4),
    Player("Eden", 10),
    Player("Maxym", 99) # Extra speler met dezelfde naam om eq te testen
]

# 2. Print één van de objecten naar de console (test __str__)
print(f"Test __str__ op het eerste object: {lijst[0]}")
print("---")

# 3. Test de eq methode (gebruik de operator ==)
print("--- 2. Test __eq__ (Gelijkheid op naam) ---")
# Test 1: Spelers met dezelfde naam (Maxym) maar verschillend nummer
gelijkheid_test_1 = lijst[0] == lijst[3]
print(f"Is '{lijst[0]}' gelijk aan '{lijst[3]}'? -> {gelijkheid_test_1}")

# Test 2: Spelers met verschillende namen (Maxym en Kevin)
gelijkheid_test_2 = lijst[0] == lijst[1]
print(f"Is '{lijst[0]}' gelijk aan '{lijst[1]}'? -> {gelijkheid_test_2}")

# Test 3: Speler vergelijken met een string (moet False geven)
gelijkheid_test_3 = lijst[0] == "Maxym"
print(f"Is '{lijst[0]}' gelijk aan de string 'Maxym'? -> {gelijkheid_test_3}")
print("---")


# 4. Test de lt methode door de sorted functie toe te passen op de lijst.
print("--- 3. Test __lt__ (Sorteren op nummer) ---")
print(f"Originele lijst: {lijst}")

# De sorted functie roept intern de __lt__ methode aan voor de vergelijkingen
gesorteerde_lijst = sorted(lijst)

# 5. Print de gesorteerde lijst
print(f"Gesorteerde lijst (op rugnummer): {gesorteerde_lijst}")
print("---")

# Optionele extra test voor __lt__ (gebruik de operator <)
print("--- 4. Test __lt__ met operator < ---")
# Kevin (4) is kleiner dan Maxym (17)
lt_test = lijst[1] < lijst[0]
print(f"Is '{lijst[1]}' (nr 4) < '{lijst[0]}' (nr 17)? -> {lt_test}")

if lt_test:
    print("gelukt (Kevin < Maxym)")
else:
    print("niet gelukt")

