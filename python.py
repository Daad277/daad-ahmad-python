import random
import time

# ANSI kleuren voor feedback
GREEN = "\033[32m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Welkom
print("Welkom in het game!")
naam = input("Voer uw naam in: ")
print(f"Hallo {naam}, laten we starten!")

# Moeilijkheid kiezen
print("Kies een moeilijkheid:")
print("1 - Easy (3 cijfers)")
print("2 - Medium (4 cijfers)")
print("3 - Hard (5 cijfers)")
keuze = input("Typ 1, 2 of 3: ")

if keuze == "1":
    code_lengte = 3
elif keuze == "2":
    code_lengte = 4
elif keuze == "3":
    code_lengte = 5

# Functie om geheime code te maken
def maak_code(lengte):
    code = ""
    for _ in range(lengte):
        code += str(random.randint(0, 9))
    return code

opnieuw = "ja"
while opnieuw == "ja":
    # Start van een nieuwe ronde
    geheime_code = maak_code(code_lengte)
    pogingen = 0
    start_tijd = time.time()

    while True:
        # Input van speler en lengte check
        gok = input(f"Raad de {code_lengte}-cijfer code: ")
        if len(gok) != code_lengte or not gok.isdigit():
            print(f"Voer exact {code_lengte} cijfers in!")
            continue

        pogingen += 1
        feedback = ""

        # Feedback berekenen
        for i in range(len(gok)):
            if gok[i] == geheime_code[i]:
                feedback += GREEN + "+" + RESET
            elif gok[i] in geheime_code:
                feedback += YELLOW + "-" + RESET
            else:
                feedback += " "

        print("Feedback:", feedback)

        # Winconditie
        if gok == geheime_code:
            eind_tijd = time.time()
            totaal_tijd = round(eind_tijd - start_tijd, 2)
            print(f"Goed geraden, {naam}!")
            print(f"Aantal pogingen: {pogingen}")
            print(f"Totaal tijd: {totaal_tijd} seconden")
            break
        else:
            print("Probeer opnieuw!")

    # Vraag om opnieuw te spelen
    opnieuw = input("Wil je opnieuw spelen? (ja/nee): ").lower()
    print()
    if opnieuw != "ja":
        print(f"tot ziens!")
        break




