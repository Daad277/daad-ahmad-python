import random
import time

# ANSI kleuren voor feedback
GREEN = "\033[32m"
YELLOW = "\033[93m"
RESET = "\033[0m"

#welkom
print ("Welkom in de game")
naam = input("Voer uw naam in: ")
print (" Hello "+naam+" kies een moeilijkheid")

#Moeilijkheid kiezen
print ("1- Easy (3 cijfers)")
print ("2- Medium (4 cijfers)")
print ("3- Hard (5 cijfers)")
keuze = input("Typ 1, 2 of 3: ")

if keuze == "1":
    code_length = 3
elif keuze == "2":
    code_length = 4
elif keuze == "3":
    code_length= 5


# Geheime code
def maak_code(length):
    code = ""
    for _ in range(length):
        code += str(random.randint(0, 9))
    return code

Opnieuw = "ja"
while opnieuw == "ja":
    geheime_code = maak_code(code_length)
    pogingen = 0














