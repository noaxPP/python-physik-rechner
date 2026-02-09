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
        p = A/F
        print(f"p = {F} / {A}")
        print("")
        print(f"p = {p:.3f} Pa")

    elif ges == "f":
        p = get("p")
        A = get("A")
        F = A * p
        print(f"F = {p} * {A}")
        print("")
        print(f"F = {F:.3f} N")

    elif ges == "a":
        F = get("F")
        p = get("p")
        A = p * F
        print(f"A = {p} * {F}")
        print("")
        print(f"A = {A:.3f} m²")

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

def schmelz_rechner():
    print("Formel: Qs = qs ⋅ m ")
    print("Gesucht: Qs, m oder qs\n")
    print("")
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
        print(f"Qs = {qs} * {m}")
        print(f"Qs = {Qs:.2f} J")

    elif ges == "m":
        Qs = get("Qs")
        qs = get("qs")
        m = Qs / qs
        print(f"m = {Qs} / {qs}")
        print(f"m = {m:.4f} kg")

    elif ges == "qs":
        Qs = get("Qs")
        m = get("m")
        qs = Qs / m
        print(f"qs = {Qs} / {m}")
        print(f"qs = {qs:.2f} J/kg")
    
    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def verdampfungs_rechner():
    print("Formel: Qv = qv * m")
    print("Gesucht: Qv, m oder qv\n")
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
        print(f"Qv = {qv} * {m}")
        print(f"Qv = {Qv:.2f} J")

    elif ges == "m":
        Qv = get("Qv")
        qv = get("qv")
        m = Qv / qv
        print(f"m = {Qv} / {qv}")
        print(f"m = {m:.4f} kg")

    elif ges == "qv":
        Qv = get("Qv")
        m = get("m")
        qv = Qv / m
        print(f"qv = {Qv} / {m}")
        print(f"qv = {qv:.2f} J/kg")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def dampferwaermung_rechner():
    print("Formel: Q = c * m * ΔT")
    print("Gesucht: Q, m, c oder ΔT")

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
        print(f"Q = {c} * {m} * {dT}")
        print(f"Q = {Q:.2f} J")

    elif ges == "m":
        Q = get("q")
        c = get("c")
        dT = get("t")
        m = Q / (c * dT)
        print(f"m = {Q} / ({c} * {dT})")
        print(f"m = {m:.4f} kg")

    elif ges == "c":
        Q = get("q")
        m = get("m")
        dT = get("t")
        c = Q / (m * dT)
        print(f"c = {Q} / ({m} * {dT})")
        print(f"c = {c:.2f} J/(kg*K)")

    elif ges in ("t", "Δt", "dt"):
        Q = get("q")
        m = get("m")
        c = get("c")
        dT = Q / (m * c)
        print(f"ΔT = {Q} / ({m} * {c})")
        print(f"ΔT = {dT:.2f} K")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def geschwindigkeit_rechner():
    print("Formel: v = s / t")
    print("Gesucht: v, s oder t\n")
    print("")
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
        print(f"v = {s} / {t}")
        print(f"v = {v:.2f} m/s")

    elif ges == "s":
        v = get("v")
        t = get("t")
        s = v * t
        print(f"s = {v} * {t}")
        print(f"s = {s:.2f} m")

    elif ges == "t":
        s = get("s")
        v = get("v")
        t = s / v
        print(f"t = {s} / {v}")
        print(f"t = {t:.2f} s")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

def beschleunigung_rechner():
    print("Formel: a = Δv / Δt")
    print("Gesucht: a, dv oder dt\n")
    print("")
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
        print(f"a = {dv} / {dt}")
        print(f"a = {a:.2f} m/s²")
    
    elif ges == "dv":
        a = get("a")
        dt = get("dt")
        kmh_dv = a * dt *3.6
        dv = a * dt
        print(f"Δv = {a} * {dt}")
        print(f"Δv = {dv:.2f} m/s")
        print(f"oder Δv = {kmh_dv:.2f} km/h")

    elif ges == "dt":
        a = get("a")
        if input("Wird Δv in km/h angegeben? (j/n): ").strip().lower() == "j":
            dv = get("dv") / 3.6
        else:
            dv = get("dv")
        dt = dv / a
        print(f"Δt = {dv} / {a}")
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
        print(f"s = {v} * {t}")
        print(f"s = {s:.2f} m")
    
    elif ges == "v":
        s = get("s")
        t = get("t")
        kmh_v = s / t * 3.6
        v = s / t
        print(f"v = {s} / {t}")
        print(f"v = {v:.2f} m/s")
        print(f"oder v = {kmh_v:.2f} km/h")
    
    elif ges == "t":
        if input("Wird v in km/h angegeben? (j/n): ").strip().lower() == "j":
            v = get("v") / 3.6
        else:
            v = get("v")
        s = get("s")
        t = s / v
        print(f"t = {s} / {v}")
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
        print(f"F = {m} * {a}")
        print(f"F = {F:.0} N")

    elif ges == "m":
        if input("Wird a in km/h angegeben? (j/n): ").strip().lower() == "j":
            a = get("a") / 3.6
        else:
            a = get("a")
        F = get("F")
        m = F / a
        print(f"m = {F} / {a}")
        print(f"m = {m:.4f} kg")
    
    elif ges == "a":
        m = get("m")
        F = get("F")
        a = F / m
        print(f"a = {F} / {m}")
        print(f"a = {a:.2f} m/s²")

    else:
        print("Ein Fehler ist aufgetreten, bitte versuche es erneut!")

