import time

def kmh_to_ms(v):
    return v / 3.6

def fehler():
    print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def cm_to_m(cm):
    return cm * 100

def dicht_rechner():
    print("Die Formel lautet:  p = m / V ")
    print("------------------------")
    ges = input("Was ist gesucht? (p, m oder V): ").strip().lower()

    prompts = {
        "m": "Masse m (kg): ",
        "p": "Dichte p (kg/m³): ",
        "V": "Volumen V (m³):"
    }
    def get(var):
        return float(input(prompts [var]))
    
    if ges == "m":
        rho = get("p")
        V = get("V")
        m = rho * V
        print(f"m = {rho} kg/m³ * {V} m³")
        print(f"m = {m:1f} kg")

    elif ges == "p":
        m = get("m")
        V = get("V")
        try:
            rho = m / V
            print(f"p = {m} kg / {V} m³")
            print(f"p = {rho:3f} kg/m³")
        except ZeroDivisionError:
            print("Das Volumen V darf nicht 0 sein!")
    

    elif ges == "v":
        rho = get("p")
        m = get("m")
        try:
            V = m / rho
            print(f"V = {m} kg / {rho} kg/m³")
            print(f"V = {V:3f} m³")
        except ZeroDivisionError:
            print("Die Dichte p darf nicht 0 sein!")

    else:
        fehler()
        time.sleep(3)

def druck_rechner():
    print("Die Formel lautet: p = F/A")
    print("---------------------------")
    ges = input("Was ist gesucht (p, F oder A)?: ").strip().lower()

    prompts = {
        "p": "Druck p (Pa): ",
        "F": "Kraft F (N): ",
        "A": "Fläche A (m²): "
    }
    def get(var):
        return float(input (prompts [var]))

    if ges == "p":
        F = get("F")
        A = get("A")
        try:
            p = F / A
            print(f"p = {F} N / {A} m²")
            print(f"p = {p:.3f} Pa")
        except ZeroDivisionError:
            print("Die Fläche A darf nicht 0 sein!")

    elif ges == "f":
        p = get("p")
        A = get("A")
        F = A * p
        print(f"F = {p} Pa * {A} m²")
        print(f"F = {F:.3f} N")

    elif ges == "a":
        F = get("F")
        p = get("p")
        try:
            A = F / p
            print(f"A = {F} N / {p} Pa")
            print(f"A = {A:.3f} m²")
        except ZeroDivisionError:
            print("Der Druck p darf nicht 0 sein!")
    else:
       fehler()

def waerme_rechner():
    print("Formel: Q = c * m * ΔT")
    print("------------------------\n")
    
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
        print(f"Q = {c} J/(kg*K) * {m} kg * {dT} K")
        print(f"Q = {Q:.2f} J")       

    elif gesucht == "m":
        Q = get("q")
        c = get("c")
        dT = get("t")
        try:
            m = Q / (c * dT)
            print(f"m = {Q} J / ({c} J/(kg*K) * {dT} K)")
            print(f"m = {m:.4f} kg")
        except ZeroDivisionError:
            print("c * ΔT darf nicht 0 ergeben!")

    elif gesucht == "c":
        Q = get("q")
        m = get("m")
        dT = get("t")
        try:
            c = Q / (m * dT)
            print(f"c = {Q} J / ({m} kg * {dT} K)")
            print(f"c = {c:.2f} J/(kg*K)")
        except ZeroDivisionError:
            print("m * ΔT darf nicht 0 ergeben!")

    elif gesucht in ("t", "Δt", "dt"):
        Q = get("q")
        m = get("m")
        c = get("c")
        try:
            dT = Q / (m * c)
            print(f"ΔT = {Q} J / ({m} kg * {c} J/(kg*K))")
            print(f"ΔT = {dT:.2f} K")
        except ZeroDivisionError:
            print("m * c darf nicht 0 ergeben!")

    else:
        fehler()

def schmelz_rechner():
    print("Formel: Qs = qs ⋅ m ")
    print("------------------------\n")
    ges = input("Was ist gesucht? (Qs, m oder qs): ").strip()

    prompts = {
        "Qs": "Schmelzwärme Qs (J): ",
        "m": "Masse m (kg): ",
        "qs": "spezifische Schmelzwärme qs (J/kg): "
    }

    def get(var):
        return float(input(prompts[var]))
    
    if ges == "Qs":
        qs = get("qs")
        m = get("m")
        Qs = qs * m
        print(f"Qs = {qs} J/kg * {m} kg")
        print(f"Qs = {Qs:.2f} J")

    elif ges == "m":
        Qs = get("Qs")
        qs = get("qs") 
        try:
            m = Qs / qs
            print(f"m = {Qs} J / {qs} J/kg")
            print(f"m = {m:.4f} kg")
        except ZeroDivisionError:
            print("Die spezifische Schmelzwärme darf nicht 0 sein!")

    elif ges == "qs":
        Qs = get("Qs")
        m = get("m")
        try:
            qs = Qs / m
            print(f"qs = {Qs} J / {m} kg")
            print(f"qs = {qs:.2f} J/kg")
        except ZeroDivisionError:
            print("Die Masse m darf nicht 0 sein!")
    else:
        fehler()

def verdampfungs_rechner():
    print("Formel: Qv = qv * m")
    print("------------------------\n")
    ges = input("Was ist gesucht? (Qv, m oder qv): ").strip()

    prompts = {
        "Qv": "Verdampfungswärme Qv (J): ",
        "m": "Masse m (kg): ",
        "qv": "spezifische Verdampfungswärme qv (J/kg): "
    }

    def get(var):
        return float(input(prompts[var]))
    
    if ges == "Qv":
        qv = get("qv")
        m = get("m")
        Qv = qv * m
        print(f"Qv = {qv} J/kg * {m} kg")
        print(f"Qv = {Qv:.2f} J")

    elif ges == "m":
        Qv = get("Qv")
        qv = get("qv")
        try:
            m = Qv / qv
            print(f"m = {Qv} J / {qv} J/kg")
            print(f"m = {m:.4f} kg")
        except ZeroDivisionError:
            print("Die spezifische Verdampfungswärme darf nicht 0 sein!")

    elif ges == "qv":
        Qv = get("Qv")
        m = get("m")
        try:
            qv = Qv / m
            print(f"qv = {Qv} J / {m} kg")
            print(f"qv = {qv:.2f} J/kg")
        except ZeroDivisionError:
            print("Die Masse m darf nicht 0 sein!")

    else:
        fehler()

def dampferwaermung_rechner():
    print("Formel: Q = c * m * ΔT")
    print("------------------------\n")

    # Typische spezifische Wärmekapazitäten von Dämpfen in J/(kg*K)
    c_werte = {
        "Wasserdampf": 2010,
        "Luft": 1000,
        "Stickstoff-Dampf": 1040,
        "Sauerstoff-Dampf": 918,
        "Kohlendioxid-Dampf": 839,
        "Wasserstoff-Dampf": 14300,
        "Helium-Dampf": 5193
    }
    print("Typische Werte für c [J/(kg*K)]:")
    for stoff, wert in c_werte.items():
        print(f" {stoff:<15} = {wert}")
    print("")
    ges = input("Was ist gesucht? (Q, m, c oder ΔT -> t): ").strip().lower()
    
    prompts = {
        "q": "Wärmeenergie Q (J): ",
        "m": "Masse m (kg): ",
        "c": "spezifische Wärmekapazität c (J/(kg*K)): ",
        "t": "Temperaturänderung ΔT (K oder °C): "
    }
    def get(var):
        return float(input(prompts[var]))
    
    if ges == "q":
        c = get("c")
        m = get("m")
        dT = get("t")
        Q = c * m * dT
        print(f"Q = {c} J/(kg*K) * {m} kg * {dT} K")
        print(f"Q = {Q:.2f} J")

    elif ges == "m":
        Q = get("q")
        c = get("c")
        dT = get("t")
        try:
            m = Q / (c * dT)
            print(f"m = {Q} J / ({c} J/(kg*K) * {dT} K)")
            print(f"m = {m:.4f} kg")
        except ZeroDivisionError:
            print("c * ΔT darf nicht 0 sein!")

    elif ges == "c":
        Q = get("q")
        m = get("m")
        dT = get("t")
        try:
            c = Q / (m * dT)
            print(f"c = {Q} J / ({m} kg * {dT} K)")
            print(f"c = {c:.2f} J/(kg*K)")
        except ZeroDivisionError:
            print("m * ΔT darf nicht 0 sein!")

    elif ges in ("t", "Δt", "dt"):
        Q = get("q")
        m = get("m")
        c = get("c")
        try:
            dT = Q / (m * c)
            print(f"ΔT = {Q} J / ({m} kg * {c} J/(kg*K))")
            print(f"ΔT = {dT:.2f} K")
        except ZeroDivisionError:
            print("m * c darf nicht 0 sein!")

    else:
        fehler()

def geschwindigkeit_rechner():
    print("Formel: v = s / t")
    print("------------------------\n")
    ges = input("Was ist gesucht? (v, s oder t): ").strip().lower()

    prompts = {
        "v": "Geschwindigkeit v (m/s): ",
        "s": "Strecke s (m): ",
        "t": "Zeit t (s):"
    }

    def get(var):
        return float(input(prompts[var]))
    
    if ges == "v":
        if input("Wird s in cm angegeben? (j/n): ").strip().lower() == "j":
            s = cm_to_m(get("s"))
        else:
            s = get("s")
        t = get("t")
        try:
            v = s / t
            print(f"v = {s} m / {t} s")
            print(f"v = {v:.2f} m/s")
        except ZeroDivisionError:
            print("Die Zeit t darf nicht 0 sein!")

    elif ges == "s":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = kmh_to_ms(get("v"))
        else:
            v = get("v")
        t = get("t")
        s = v * t
        print(f"s = {v} m/s * {t} s")
        print(f"s = {s:.2f} m")

    elif ges == "t":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = kmh_to_ms(get("v"))
        else:
            v = get("v")
        if input("Wird s in cm angegeben? (j/n): ").strip().lower() == "j":
            s = cm_to_m(get("s"))
        else:
            s = get("s")
        try:
            t = s / v
            print(f"t = {s} m / {v} m/s")
            print(f"t = {t:.2f} s")
        except ZeroDivisionError:
            print("Die Geschwindigkeit v darf nicht 0 sein!")

    else:
        fehler()

def beschleunigung_rechner():
    print("Formel: a = Δv / Δt")
    print("------------------------\n")
    ges = input("Was ist gesucht? (a, dv oder dt): ").strip().lower()

    prompts = {
        "a": "Beschleunigung a (m/s²): ",
        "dv": "Geschwindigkeitsänderung Δv (m/s oder km/h): ",
        "dt": "Zeitänderung Δt (s): "
    }
    def get(var):
        return float(input(prompts[var]))
    
    if ges == "a":
        if input("Wird Δv in km/h angegeben? (j/n): ").strip().lower() == "j":
            dv = kmh_to_ms(get("dv"))
        else:
            dv = get("dv")
        dt = get("dt")
        try:
            a = dv / dt
            print(f"a = {dv} m/s / {dt} s")
            print(f"a = {a:.2f} m/s²")
        except ZeroDivisionError:
            print("Die Zeitänderung darf nicht 0 sein!")
    
    elif ges == "dv":
        a = get("a")
        dt = get("dt")
        dv = a * dt
        print(f"Δv = {a} m/s² * {dt} s")
        print(f"Δv = {dv:.2f} m/s")
        
    elif ges == "dt":
        a = get("a")
        if input("Wird Δv in km/h angegeben? (j/n): ").strip().lower() == "j":
            dv = kmh_to_ms(get("dv"))
        else:
            dv = get("dv")
        try:
            dt = dv / a
            print(f"Δt = {dv} m/s / {a} m/s²")
            print(f"Δt = {dt:.2f} s")
        except ZeroDivisionError:
            print("Die Beschleunigung a darf nicht 0 sein!")

    else:
        fehler()

def weg_gleichmäßig_bewegung_rechner():
    print("Formel: s = v * t")
    print("Gesucht: s, v oder t\n")
    print("")
    ges = input("Was ist gesucht? (s, v oder t): ").strip().lower()

    prompts = {
        "s": "Weg s (m): ",
        "v": "Geschwindigkeit v (m/s oder km/h): ",
        "t": "Zeit t (s): "
    }
    
    def get(var):
        return float(input(prompts[var]))
    
    if ges == "s":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = kmh_to_ms(get("v"))
        else:
            v = get("v")
        t = get("t")
        s = v * t
        print(f"s = {v} m/s * {t} s")
        print(f"s = {s:.2f} m")
    
    elif ges == "v":
        if input("Wird s in cm angegeben? (j/n): ").strip().lower() == "j":
            s = cm_to_m(get("s"))
        else:
            s = get("s")
        t = get("t")
        if t == 0:
            print("Die Zeit t darf nicht 0 sein!")
            return
        try:
            v = s / t
            print(f"v = {s} m / {t} s")
            print(f"v = {v:.2f} m/s")
        except ZeroDivisionError:
            print("Der Weg s darf nicht 0 sein!")
    
    elif ges == "t":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = kmh_to_ms(get("v"))
        else:
            v = get("v")
        if input("Wird s in cm angegeben? (j/n): ").strip().lower() == "j":
            s = cm_to_m(get("s"))
        else:
            s = get("s")
        try:
            t = s / v
            print(f"t = {s} m / {v} m/s")
            print(f"t = {t:.2f} s")
        except ZeroDivisionError:
            print("Die Geschwindigkeit v ddarf nicht 0 sein")
    
    else: 
        fehler()

def kraft_rechner():
    print("Formel: F = m * a")
    print("Gesucht: F, m oder a")
    print("")
    ges = input("Was ist gesucht? (F, m oder a): ").strip().lower()

    prompts = {
        "F": "Kraft F (N): ",
        "m": "Masse m (kg): ",
        "a": "Beschleunigung a (m/s² oder km/h): "
    }
    def get(var):
        return float(input(prompts[var]))
    
    if ges == "f":
        if input("Wird a in km/h angegeben? (j/n): ").strip().lower() == "j":
            a = kmh_to_ms(get("a"))
        else:
            a = get("a")
        m = get("m")
        F = m * a
        print(f"F = {m} kg * {a} m/s²")
        print(f"F = {F:.0} N")

    elif ges == "m":
        frage = input("Wird a in km/h angegeben? (j/n): ").strip().lower()
        if frage == "j":
            a = kmh_to_ms(get("a"))
        else:
            a = get("a")
        F = get("F")
        try:
            m = F / a
            print(f"m = {F} N/ {a} m/s²")
            print(f"m = {m:.4f} kg")
        except ZeroDivisionError:
            print("Die Beschleunigung a darf nicht 0 sein!")
    
    elif ges == "a":
        m = get("m")
        F = get("F")
        try:
            a = F / m
            print(f"a = {F} N / {m} kg")
            print(f"a = {a:.2f} m/s²")
        except ZeroDivisionError:
            print("Die Masse m darf nicht 0 sein!")

    else:
        fehler()

def gewichts_kraft_rechner():
    print("Formel: Fg = m * g")
    print("Gesucht: Fg, m oder g")
    
    g_werte = {
        "Erde": 9.81,
        "Mond": 1.62,
        "Mars": 3.71,
        "Jupiter": 24.79
    }
    print("Typische Werte fü Ortsfaktor g [m/s²]:")
    for planet, wert in g_werte.items():
        print(f"{planet:<10} = {wert} m/s²")
    print("")
    ges = input("Was ist gesucht? (Fg, m oder g): ").strip().lower()

    prompts = {
        "Fg": "Gewichtskraft Fg (n): ",
        "m": "Masse m (kg): ",
        "g": "Ortsfaktor g (m/s²): "
    }
    def get(var):
        return float(input(prompts[var]))
    
    if ges == "fg":
        m = get("m")
        g = get("g")
        Fg = m * g
        print(f"Fg = {m} kg * {g} m/s² ")
        print(f"Fg = {Fg:.2f} N")

    elif ges == "m":
        Fg = get("Fg")
        g = get("g")
        try:
            m = Fg / g
            print(f"m = {Fg} N / {g} m/s²")
            print(f"m = {m:.4f} kg")
        except ZeroDivisionError:
            print("Der Ortsfaktor g darf nicht 0 sein!")

    elif ges == "g":
        Fg = get("Fg")
        m = get("m")
        try:
            g = Fg / m
            print(f"g = {Fg} N / {m} kg")
            print(f"g = {g:.2f} m/s²")
        except ZeroDivisionError:
            print("Die Masse m darf nicht 0 sein!")

    else:
        fehler()
    
def federkraft_rechner():
    print("Formel: F = D * s")
    print("------------------------\n")
    ges = input("Was ist gesucht? (F, D oder s): ").strip().lower()

    prompts = {
        "F": "Federkraft F (N): ",
        "D": "Federkonstante D (N/m): ",
        "s": "Federweg s (m): "
    }
    def get(var):
        return float(input(prompts[var]))
    
    if ges == "f":
        D = get("D")
        if input("Wird s in cm angegeben? (j/n): ").strip().lower() == "j":
            s = cm_to_m(get("s"))
        else:
            s = get("s")
        F = D * s
        print(f"F = {D} N/m * {s} m")
        print(f"F = {F:.2f} N")

    elif ges == "d":
        F = get("F")
        if input("Wird s in cm angegeben? (j/n): ").strip().lower() == "j":
            s = cm_to_m(get("s"))
        else:
            s = get("s")
        try:
            D = F / s
            print(f"D = {F} N / {s} m")
            print(f"D = {D:.2f} N/m")
        except ZeroDivisionError:
           print("Der Federweg s darf nicht 0 sein!") 
    
    elif ges == "s":
        D = get("D")
        F = get("F")
        try:
            s = F / D
            print(f"s = {F} N / {D} N/m")
            print(f"s = {s:.2f} m")
        except ZeroDivisionError:
            print("Die Federkonstante D darf nicht 0 sein!")
    else:
        fehler()

    

