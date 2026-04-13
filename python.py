import random
import time

#welkom
print ("Welkom in de game")
naam = input("Voer uw naam in: ")
print (f" Hello {naam}, kies een moeilijkheid")

#Moeilijkheid kiezen
print ("1- Easy ( 3 cijfers)")
print ("2- Medium (4 cijfers)")
print ("3- Hard ( 5 cijfers)")
keuze = input("Typ 1, 2 of 3: ")

if keuze == "1":
    code_length = 3
if keuze == "2":
    code_length = 4
elif keuze == "3":
    code_length= 5



