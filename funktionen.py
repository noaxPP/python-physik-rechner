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
        print(f"m = {rho} kg/m³ * {V} m³")
        print(f"m = {m:1f} kg")

    elif ges == "p":
        m = get("m")
        V = get("V")
        rho = m / V
        print(f"p = {m} kg / {V} m³")
        print(f"p = {rho:3f} kg/m³")

    elif ges == "v":
        rho = get("p")
        m = get("m")
        V = m / rho
        print(f"V = {m} kg / {rho} kg/m³")
        print(f"V = {V:3f} m³")

    else:
        print("Ein Fehler ist aufgetreten, versuch es erneut!")
        time.sleep(3)

def druck_rechner():
    print("Die Formel lautet: p = F/A")
    print("---------------------------")
    ges = input("Was ist gesucht (p, F oder A)?: ").strip().lower()

    promts = {
        "p": "Druck p (Pa): ",
        "F": "Kraft F (N): ",
        "A": "Fläche A (m²): "
    }
    def get(var):
        return float(input (promts [var]))

    if ges == "p":
        F = get("F")
        A = get("A")
        p = F / A
        print(f"p = {F} N / {A} m²")
        print(f"p = {p:.3f} Pa")

    elif ges == "f":
        p = get("p")
        A = get("A")
        F = A * p
        print(f"F = {p} Pa * {A} m²")
        print(f"F = {F:.3f} N")

    elif ges == "a":
        F = get("F")
        p = get("p")
        A = F / p
        print(f"A = {F} N / {p} Pa")
        print(f"A = {A:.3f} m²")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

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
        m = Q / (c * dT)
        print(f"m = {Q} J / ({c} J/(kg*K) * {dT} K)")
        print(f"m = {m:.4f} kg")

    elif gesucht == "c":
        Q = get("q")
        m = get("m")
        dT = get("t")
        c = Q / (m * dT)
        print(f"c = {Q} J / ({m} kg * {dT} K)")
        print(f"c = {c:.2f} J/(kg*K)")

    elif gesucht in ("t", "Δt", "dt"):
        Q = get("q")
        m = get("m")
        c = get("c")
        dT = Q / (m * c)
        print(f"ΔT = {Q} J / ({m} kg * {c} J/(kg*K))")
        print(f"ΔT = {dT:.2f} K")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def schmelz_rechner():
    print("Formel: Qs = qs ⋅ m ")
    print("------------------------\n")
    ges = input("Was ist gesucht? (Qs, m oder qs): ").strip()

    promts = {
        "Qs": "Schmelzwärme Qs (J): ",
        "m": "Masse m (kg): ",
        "qs": "spezifische Schmelzwärme qs (J/kg): "
    }

    def get(var):
        return float(input(promts[var]))
    
    if ges == "Qs":
        qs = get("qs")
        m = get("m")
        Qs = qs * m
        print(f"Qs = {qs} J/kg * {m} kg")
        print(f"Qs = {Qs:.2f} J")

    elif ges == "m":
        Qs = get("Qs")
        qs = get("qs")
        m = Qs / qs
        print(f"m = {Qs} J / {qs} J/kg")
        print(f"m = {m:.4f} kg")

    elif ges == "qs":
        Qs = get("Qs")
        m = get("m")
        qs = Qs / m
        print(f"qs = {Qs} J / {m} kg")
        print(f"qs = {qs:.2f} J/kg")
    
    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def verdampfungs_rechner():
    print("Formel: Qv = qv * m")
    print("------------------------\n")
    print("")
    ges = input("Was ist gesucht? (Qv, m oder qv): ").strip()

    promts = {
        "Qv": "Verdampfungswärme Qv (J): ",
        "m": "Masse m (kg): ",
        "qv": "spezifische Verdampfungswärme qv (J/kg): "
    }

    def get(var):
        return float(input(promts[var]))
    
    if ges == "Qv":
        qv = get("qv")
        m = get("m")
        Qv = qv * m
        print(f"Qv = {qv} J/kg * {m} kg")
        print(f"Qv = {Qv:.2f} J")

    elif ges == "m":
        Qv = get("Qv")
        qv = get("qv")
        m = Qv / qv
        print(f"m = {Qv} J / {qv} J/kg")
        print(f"m = {m:.4f} kg")

    elif ges == "qv":
        Qv = get("Qv")
        m = get("m")
        qv = Qv / m
        print(f"qv = {Qv} J / {m} kg")
        print(f"qv = {qv:.2f} J/kg")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

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
    
    promts = {
        "q": "Wärmeenergie Q (J): ",
        "m": "Masse m (kg): ",
        "c": "spezifische Wärmekapazität c (J/(kg*K)): ",
        "t": "Temperaturänderung ΔT (K oder °C): "
    }
    def get(var):
        return float(input(promts[var]))
    
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
        m = Q / (c * dT)
        print(f"m = {Q} J / ({c} J/(kg*K) * {dT} K)")
        print(f"m = {m:.4f} kg")

    elif ges == "c":
        Q = get("q")
        m = get("m")
        dT = get("t")
        c = Q / (m * dT)
        print(f"c = {Q} J / ({m} kg * {dT} K)")
        print(f"c = {c:.2f} J/(kg*K)")

    elif ges in ("t", "Δt", "dt"):
        Q = get("q")
        m = get("m")
        c = get("c")
        dT = Q / (m * c)
        print(f"ΔT = {Q} J / ({m} kg * {c} J/(kg*K))")
        print(f"ΔT = {dT:.2f} K")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

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
        s = get("s")
        t = get("t")
        v = s / t
        print(f"v = {s} m / {t} s")
        print(f"v = {v:.2f} m/s")

    elif ges == "s":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = get("v") / 3.6
        else:
            v = get("v")
        t = get("t")
        s = v * t
        print(f"s = {v} m/s * {t} s")
        print(f"s = {s:.2f} m")

    elif ges == "t":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = get("v") / 3.6
        else:
            v = get("v")
        
        s = get("s")
        t = s / v
        print(f"t = {s} m / {v} m/s")
        print(f"t = {t:.2f} s")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def beschleunigung_rechner():
    print("Formel: a = Δv / Δt")
    print("------------------------\n")
    ges = input("Was ist gesucht? (a, dv oder dt): ").strip().lower()

    promts = {
        "a": "Beschleunigung a (m/s²): ",
        "dv": "Geschwindigkeitsänderung Δv (m/s oder km/h): ",
        "dt": "Zeitänderung Δt (s): "
    }
    def get(var):
        return float(input(promts[var]))
    
    if ges == "a":
        if input("Wird Δv in km/h angegeben? (j/n): ").strip().lower() == "j":
            dv = get("dv") / 3.6
        else:
            dv = get("dv")
        dt = get("dt")
        a = dv / dt
        print(f"a = {dv} m/s / {dt} s")
        print(f"a = {a:.2f} m/s²")
    
    elif ges == "dv":
        a = get("a")
        dt = get("dt")
        dv = a * dt
        print(f"Δv = {a} m/s² * {dt} s")
        print(f"Δv = {dv:.2f} m/s")
        
    elif ges == "dt":
        a = get("a")
        if input("Wird Δv in km/h angegeben? (j/n): ").strip().lower() == "j":
            dv = get("dv") / 3.6
        else:
            dv = get("dv")
        dt = dv / a
        print(f"Δt = {dv} m/s / {a} m/s²")
        print(f"Δt = {dt:.2f} s")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def weg_gleichmäßig_bewegung_rechner():
    print("Formel: s = v * t")
    print("Gesucht: s, v oder t\n")
    print("")
    ges = input("Was ist gesucht? (s, v oder t): ").strip().lower()

    promts = {
        "s": "Weg s (m): ",
        "v": "Geschwindigkeit v (m/s oder km/h): ",
        "t": "Zeit t (s): "
    }
    
    def get(var):
        return float(input(promts[var]))
    
    if ges == "s":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = get("v") / 3.6
        else:
            v = get("v")
        t = get("t")
        s = v * t
        print(f"s = {v} m/s² * {t} s")
        print(f"s = {s:.2f} m")
    
    elif ges == "v":
        s = get("s")
        t = get("t")
        v = s / t
        print(f"v = {s} m / {t} s")
        print(f"v = {v:.2f} m/s")
    
    elif ges == "t":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = get("v") / 3.6
        else:
            v = get("v")
        s = get("s")
        t = s / v
        print(f"t = {s} m / {v} m/s²")
        print(f"t = {t:.2f} s")
    
    else: 
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def kraft_rechner():
    print("Formel: F = m * a")
    print("Gesucht: F, m oder a")
    print("")
    ges = input("Was ist gesucht? (F, m oder a): ").strip().lower()

    prompts = {
        "F": "Kraft F (N): ",
        "m": "Masse m (kg): ",
        "a": "Beschleunigung a (m/s²): "
    }
    def get(var):
        return float(input(prompts[var]))
    
    if ges == "f":
        if input("Wird a in km/h angegeben? (j/n): ").strip().lower() == "j":
            a = get("a") / 3.6
        else:
            a = get("a")
        m = get("m")
        F = m * a
        print(f"F = {m} kg * {a} m/s²")
        print(f"F = {F:.0} N")

    elif ges == "m":
        frage = input("Wird a in km/h angegeben? (j/n): ").strip().lower()
        if frage == "j":
            a = get("a") / 3.6
        else:
            a = get("a")
        F = get("F")
        m = F / a
        print(f"m = {F} N/ {a} m/s²")
        print(f"m = {m:.4f} kg")
    
    elif ges == "a":
        m = get("m")
        F = get("F")
        a = F / m
        print(f"a = {F} N / {m} kg")
        print(f"a = {a:.2f} m/s²")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

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
        m = Fg / g
        print(f"m = {Fg} N / {g} m/s²")
        print(f"m = {m:.4f} kg")

    elif ges == "g":
        Fg = get("Fg")
        m = get("m")
        g = Fg / m
        print(f"g = {Fg} N / {m} kg")
        print(f"g = {g:.2f} m/s²")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")
    