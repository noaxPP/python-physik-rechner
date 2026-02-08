from funktionen import *
import time 

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
    4. Spezifische Schmelzwärme
    5. Spezifische Verdampfungswärme
    6. Dampferwärmung
    7. ...
    '''
    )

    auswahl = int(input("Menu Zahl: "))

    if auswahl == 1:
        dicht_rechner()
        time.sleep(3)

    elif auswahl == 2:
        druck_rechner()
        time.sleep(3)

    elif auswahl == 3:
        waerme_rechner()
        time.sleep(3)
    
    elif auswahl == 4:
        schmelz_rechner()
        time.sleep(3)

    elif auswahl == 5:
        verdampfungs_rechner()
        time.sleep(3)

    elif auswahl == 6:
        dampferwaermung_rechner()
        time.sleep(3)

    else:
        print("Menu noch nicht verfügbar! :(")
        time.sleep(3)