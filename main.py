from funktionen import *

while True:
    print("") 
    print("Physik Rechner")
    print("-------------------------------")
    print("Welche Formel möchtest du rechnen?")
    print(
    '''
    1. Dichte
    2. Druck
    3. Wärme
    4. ...
    '''
    )

    auswahl = int(input("Menu Zahl: "))

    if auswahl == 1:
        dicht_rechner()

    elif auswahl == 2:
        druck_rechner()

    elif auswahl == 3:
        waerme_rechner()

    else:
        print("Menu noch nicht verfügbar! :(")