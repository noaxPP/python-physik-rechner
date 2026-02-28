from funktionen import *
import time 

while True:
    print("") 
    print("Physik Rechner")
    print("-------------------------------")
    print("Welches Thema wählst du?")
    print(
    '''
    1. Mechanik
    2. Arbeit, Energie und Leistung
    3. Dichte und Druck
    '''
    )

    auswahl = int(input("Menu Zahl: "))

    if auswahl == 1:
        print('''
        1. Bewegung
        2. Kräfte      
        '''
        )
        wahl = int(input("Menu Zahl: "))
        if wahl == 1:
            print('''
            1. Geschwindigkeit
            2. Beschleunigung
            3. Weg bei gleichmäßiger Bewegung
            ''')
            wahl2 = int(input("Formel Zahl: "))
            if wahl2 == 1:
                geschwindigkeit_rechner()
                time.sleep(3)
            elif wahl2 == 2:
                beschleunigung_rechner()
                time.sleep(3)
            elif wahl2 == 3:
                weg_gleichmäßig_bewegung_rechner()
                time.sleep(3)
            else:
               fehler()
        
        elif wahl == 2:
            print('''
            1. Kraft
            2. Gewichtskraft
            3. Hookesches Gesetz (Federkraft)
            ''')
            wahl2 = int(input("Formel Zahl: "))
            if wahl2 == 1:
                kraft_rechner()
                time.sleep(3.5)
            elif wahl2 == 2:
                gewichts_kraft_rechner()
                time.sleep(3.5)
            elif wahl2 == 3:
                federkraft_rechner()
                time.sleep(3.5)
            else:
                fehler()

    elif auswahl == 2:
        print('''
        1. Arbeit
        2. Energie
        3. Leistung
        ''')
        wahl = int(input("Menu Zahl: "))    
        if wahl == 1:
            arbeit_rechner()
            time.sleep(3)
        elif wahl == 2:
            print('''
            1. Kinetische Energie
            2. Potentielle Energie
            ''')
            wahl2 = int(input("Formel Zahl: "))
            if wahl2 == 1:
                kinetische_energie_rechner()
                time.sleep(3)
            elif wahl2 == 2:
                potentielle_energie_rechner()
                time.sleep(3)
            else:
                fehler()
            time.sleep(3)
        elif wahl == 3:
            leistung_rechner()
            time.sleep(3)
        else:
            fehler()

    elif auswahl == 3:
        print('''
        1. Dichte
        2. Druck
        ''')  
        wahl = int(input("Menu Zahl: "))
        if wahl == 1:
            dicht_rechner()
            time.sleep(3)
        elif wahl == 2:
            print('''
            1. Druck
            2. Hydrostatischer Druck
            ''')
            wahl2 = int(input("Formel Zahl: "))
            if wahl2 == 1:
                druck_rechner()
                time.sleep(3)
            elif wahl2 == 2:
                #hydrostatischer_druck_rechner()
                time.sleep(3)
            else:
                fehler()
    else:
        fehler()       
# they are just from the old menu 
   #elif auswahl == 3:
   #    waerme_rechner()
   #    time.sleep(3)
   #
   #elif auswahl == 4:
   #    schmelz_rechner()
   #    time.sleep(3)

   #elif auswahl == 5:
   #    verdampfungs_rechner()
   #    time.sleep(3)

   #elif auswahl == 6:
   #    dicht_rechner()
   #    time.sleep(3)

   #else:
   #    print("Menu noch nicht verfügbar! :(")
   #    time.sleep(3)