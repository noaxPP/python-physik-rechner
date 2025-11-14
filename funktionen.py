import time

def dicht_rechner():
    print("Die Formel lautet:  p = m / V ")
    print("------------------------")
    ges = input("Was ist gesucht? (p, m oder V): ").strip().lower()

    promts = {
        "m": "Masse m (kg): ",
        "p": "Dichte p (kg/m³): ",
        "V": "Volumen V (m³):"
    }
    def get(var):
        return float(input(promts [var]))
    
    if ges == "m":
        rho = get("p")
        V = get("V")
        m = rho * V
        print(f"m = {rho} * {V}")
        print("")
        print(f"m = {m:1f} kg")

    elif ges == "p":
        m = get("m")
        V = get("V")
        rho = m / V
        print(f"p = {m} / {V}")
        print("")
        print(f"p = {rho:3f} kg/m³")

    elif ges == "v":
        rho = get("p")
        m = get("m")
        V = rho / m
        print(f"V = {rho} / {m}")
        print("")
        print(f"V = {V:3f} m³")

    else:
        print("Ein Fehler ist aufgetreten, versuch es erneut!")
        time.sleep(3)

def druck_rechner():
    print("Die Formel lautet: p = F/A")
    geg = input("Was ist gegeben (z.B. 'F und A')?: ").lower()
    ges = input("Was ist gesucht (z.B. p, F oder A)?: ").lower()

    if ges == "p" and "f"in geg and "a"in geg:
        A = float(input("Was ist die Fläche m²?: "))
        F = float(input("Was ist die Kraft in N?: "))
        p = F/A
        print(f"Der Druck p beträgt {p:.0} N")
    
    elif ges == "f" and "p"in geg and "a"in geg:
        A = float(input("Was ist die Fläche A in m²?: "))
        p = float(input("Was ist der Druck p in Pa?: "))
        F = p * A
        print(f"Die Kraft F beträgt {F:.3f} N")
    
    elif ges == "a"and "p"in geg and "f"in geg:
        p = float(input("Was ist der Druck p in Pa?: "))
        F = float(input("Was ist die Kraft f in N?:"))
        A = p * F
        print(f"Die Fläche A beträgt {A:.0f} m2.")

    else:
        print("Ein Fehler ist aufgetreten versuch es erneut!")

def waerme_rechner():
    print("Formel: Q = c * m * ΔT")
    print("Gesucht: Q, m, c oder ΔT\n")

    # Typische spezifische Wärmekapazitäten in J/(kg*K)
    c_werte = {
        "Wasser": 4180,
        "Eis": 2100,
        "Aluminium": 900,
        "Eisen": 450,
        "Kupfer": 385,
        "Blei": 130,
        "Luft": 1000,
        "Holz": 1700,
        "Wachs": 2931
    }
    print("Typische Werte für c [J/(kg*K)]:")
    for stoff, wert in c_werte.items(): 
        print(f"  {stoff:<12} = {wert}")
    print("")
    gesucht = input("Was ist gesucht? (Q, m, c oder ΔT): ").strip().lower()
    
    prompts = {
        "q":  "Wärmeenergie Q (J): ",
        "m":  "Masse m (kg): ",
        "c":  "spezifische Wärmekapazität c (J/(kg*K)): ",
        "t":  "Temperaturänderung ΔT (K oder °C): "
    }

    def get(var):
        return float(input(prompts[var]))
    
    if gesucht == "q":
        c = get("c")
        m = get("m")
        dT = get("t")
        Q = c * m * dT
        print(f"Q = {c} * {m} * {dT}")
        print(f"Q = {Q:.2f} J")       

    elif gesucht == "m":
        Q = get("q")
        c = get("c")
        dT = get("t")
        m = Q / (c * dT)
        print(f"m = {Q} / ({c} * {dT})")
        print(f"m = {m:.4f} kg")

    elif gesucht == "c":
        Q = get("q")
        m = get("m")
        dT = get("t")
        c = Q / (m * dT)
        print(f"c = {Q} / ({m} * {dT})")
        print(f"c = {c:.2f} J/(kg*K)")

    elif gesucht in ("t", "Δt", "dt"):
        Q = get("q")
        m = get("m")
        c = get("c")
        dT = Q / (m * c)
        print(f"ΔT = {Q} / ({m} * {c})")
        print(f"ΔT = {dT:.2f} K")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

