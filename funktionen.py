import time


def kmh_to_ms(value):
    return value / 3.6


def cm_to_m(value):
    return value / 100.0


def error_message():
    print("An error occurred. Please try again!")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Please enter a valid number.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"j", "y", "ja", "yes"}:
            return True
        if answer in {"n", "nein", "no"}:
            return False
        print("Please answer with yes or no.")


def read_speed(prompt):
    if ask_yes_no("Is the value given in km/h? (j/n): "):
        return kmh_to_ms(read_float(prompt))
    return read_float(prompt)


def read_length(prompt):
    if ask_yes_no("Is the value given in cm? (j/n): "):
        return cm_to_m(read_float(prompt))
    return read_float(prompt)


def density_calculator():
    print("Formula: rho = m / V")
    print("------------------------")
    target = input("What are you looking for? (rho, m or V): ").strip().lower()

    if target == "m":
        rho = read_float("Density rho (kg/m^3): ")
        volume = read_float("Volume V (m^3): ")
        mass = rho * volume
        print(f"m = {rho} kg/m^3 * {volume} m^3")
        print(f"m = {mass:.3f} kg")

    elif target == "rho":
        mass = read_float("Mass m (kg): ")
        volume = read_float("Volume V (m^3): ")
        try:
            rho = mass / volume
            print(f"rho = {mass} kg / {volume} m^3")
            print(f"rho = {rho:.3f} kg/m^3")
        except ZeroDivisionError:
            print("The volume V must not be 0!")

    elif target == "v":
        rho = read_float("Density rho (kg/m^3): ")
        mass = read_float("Mass m (kg): ")
        try:
            volume = mass / rho
            print(f"V = {mass} kg / {rho} kg/m^3")
            print(f"V = {volume:.3f} m^3")
        except ZeroDivisionError:
            print("The density rho must not be 0!")

    else:
        error_message()
        time.sleep(1)


def pressure_calculator():
    print("Formula: p = F / A")
    print("---------------------------")
    target = input("What are you looking for? (p, F or A): ").strip().lower()

    if target == "p":
        force = read_float("Force F (N): ")
        area = read_float("Area A (m^2): ")
        try:
            pressure = force / area
            print(f"p = {force} N / {area} m^2")
            print(f"p = {pressure:.3f} Pa")
        except ZeroDivisionError:
            print("The area A must not be 0!")

    elif target == "f":
        pressure = read_float("Pressure p (Pa): ")
        area = read_float("Area A (m^2): ")
        force = area * pressure
        print(f"F = {pressure} Pa * {area} m^2")
        print(f"F = {force:.3f} N")

    elif target == "a":
        force = read_float("Force F (N): ")
        pressure = read_float("Pressure p (Pa): ")
        try:
            area = force / pressure
            print(f"A = {force} N / {pressure} Pa")
            print(f"A = {area:.3f} m^2")
        except ZeroDivisionError:
            print("The pressure p must not be 0!")
    else:
        error_message()


def hydrostatic_pressure_calculator():
    print("Formula: p = rho * g * h")
    print("------------------------")
    target = input("What are you looking for? (p, rho, g or h): ").strip().lower()

    if target == "p":
        rho = read_float("Density rho (kg/m^3): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        height = read_float("Height h (m): ")
        pressure = rho * g * height
        print(f"p = {rho} kg/m^3 * {g} m/s^2 * {height} m")
        print(f"p = {pressure:.3f} Pa")

    elif target == "rho":
        pressure = read_float("Pressure p (Pa): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        height = read_float("Height h (m): ")
        try:
            rho = pressure / (g * height)
            print(f"rho = {pressure} Pa / ({g} m/s^2 * {height} m)")
            print(f"rho = {rho:.3f} kg/m^3")
        except ZeroDivisionError:
            print("g * h must not be 0!")

    elif target == "g":
        pressure = read_float("Pressure p (Pa): ")
        rho = read_float("Density rho (kg/m^3): ")
        height = read_float("Height h (m): ")
        try:
            g = pressure / (rho * height)
            print(f"g = {pressure} Pa / ({rho} kg/m^3 * {height} m)")
            print(f"g = {g:.3f} m/s^2")
        except ZeroDivisionError:
            print("rho * h must not be 0!")

    elif target == "h":
        pressure = read_float("Pressure p (Pa): ")
        rho = read_float("Density rho (kg/m^3): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        try:
            height = pressure / (rho * g)
            print(f"h = {pressure} Pa / ({rho} kg/m^3 * {g} m/s^2)")
            print(f"h = {height:.3f} m")
        except ZeroDivisionError:
            print("rho * g must not be 0!")

    else:
        error_message()


def heat_calculator():
    print("Formula: Q = c * m * ΔT")
    print("------------------------\n")

    specific_heat_values = {
        "Water": 4180,
        "Ice": 2100,
        "Aluminium": 900,
        "Iron": 450,
        "Copper": 385,
        "Lead": 130,
        "Air": 1000,
        "Wood": 1700,
        "Wax": 2931,
    }
    print("Typical values for c [J/(kg*K)]:")
    for substance, value in specific_heat_values.items():
        print(f"  {substance:<12} = {value}")
    print("")

    target = input("What are you looking for? (Q, m, c or ΔT): ").strip().lower()

    if target == "q":
        c = read_float("Specific heat capacity c (J/(kg*K)): ")
        mass = read_float("Mass m (kg): ")
        delta_t = read_float("Temperature change ΔT (K or °C): ")
        heat = c * mass * delta_t
        print(f"Q = {c} J/(kg*K) * {mass} kg * {delta_t} K")
        print(f"Q = {heat:.2f} J")

    elif target == "m":
        heat = read_float("Heat energy Q (J): ")
        c = read_float("Specific heat capacity c (J/(kg*K)): ")
        delta_t = read_float("Temperature change ΔT (K or °C): ")
        try:
            mass = heat / (c * delta_t)
            print(f"m = {heat} J / ({c} J/(kg*K) * {delta_t} K)")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("c * ΔT must not be 0!")

    elif target == "c":
        heat = read_float("Heat energy Q (J): ")
        mass = read_float("Mass m (kg): ")
        delta_t = read_float("Temperature change ΔT (K or °C): ")
        try:
            c = heat / (mass * delta_t)
            print(f"c = {heat} J / ({mass} kg * {delta_t} K)")
            print(f"c = {c:.2f} J/(kg*K)")
        except ZeroDivisionError:
            print("m * ΔT must not be 0!")

    elif target in {"t", "delt", "dt"}:
        heat = read_float("Heat energy Q (J): ")
        mass = read_float("Mass m (kg): ")
        c = read_float("Specific heat capacity c (J/(kg*K)): ")
        try:
            delta_t = heat / (mass * c)
            print(f"ΔT = {heat} J / ({mass} kg * {c} J/(kg*K))")
            print(f"ΔT = {delta_t:.2f} K")
        except ZeroDivisionError:
            print("m * c must not be 0!")

    else:
        error_message()


def melting_heat_calculator():
    print("Formula: Qs = qs * m")
    print("------------------------\n")
    target = input("What are you looking for? (Qs, m or qs): ").strip().lower()

    if target == "qs":
        specific_heat = read_float("Specific melting heat qs (J/kg): ")
        mass = read_float("Mass m (kg): ")
        heat = specific_heat * mass
        print(f"Qs = {specific_heat} J/kg * {mass} kg")
        print(f"Qs = {heat:.2f} J")

    elif target == "m":
        heat = read_float("Melting heat Qs (J): ")
        specific_heat = read_float("Specific melting heat qs (J/kg): ")
        try:
            mass = heat / specific_heat
            print(f"m = {heat} J / {specific_heat} J/kg")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("The specific melting heat must not be 0!")

    elif target == "qs":
        heat = read_float("Melting heat Qs (J): ")
        mass = read_float("Mass m (kg): ")
        try:
            specific_heat = heat / mass
            print(f"qs = {heat} J / {mass} kg")
            print(f"qs = {specific_heat:.2f} J/kg")
        except ZeroDivisionError:
            print("The mass m must not be 0!")
    else:
        error_message()


def vaporization_heat_calculator():
    print("Formula: Qv = qv * m")
    print("------------------------\n")
    target = input("What are you looking for? (Qv, m or qv): ").strip().lower()

    if target == "qv":
        specific_heat = read_float("Specific vaporization heat qv (J/kg): ")
        mass = read_float("Mass m (kg): ")
        heat = specific_heat * mass
        print(f"Qv = {specific_heat} J/kg * {mass} kg")
        print(f"Qv = {heat:.2f} J")

    elif target == "m":
        heat = read_float("Vaporization heat Qv (J): ")
        specific_heat = read_float("Specific vaporization heat qv (J/kg): ")
        try:
            mass = heat / specific_heat
            print(f"m = {heat} J / {specific_heat} J/kg")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("The specific vaporization heat must not be 0!")

    elif target == "qv":
        heat = read_float("Vaporization heat Qv (J): ")
        mass = read_float("Mass m (kg): ")
        try:
            specific_heat = heat / mass
            print(f"qv = {heat} J / {mass} kg")
            print(f"qv = {specific_heat:.2f} J/kg")
        except ZeroDivisionError:
            print("The mass m must not be 0!")

    else:
        error_message()


def steam_heating_calculator():
    print("Formula: Q = c * m * ΔT")
    print("------------------------\n")

    specific_heat_values = {
        "Steam": 2010,
        "Air": 1000,
        "Nitrogen steam": 1040,
        "Oxygen steam": 918,
        "Carbon dioxide steam": 839,
        "Hydrogen steam": 14300,
        "Helium steam": 5193,
    }
    print("Typical values for c [J/(kg*K)]:")
    for substance, value in specific_heat_values.items():
        print(f" {substance:<18} = {value}")
    print("")

    target = input("What are you looking for? (Q, m, c or ΔT): ").strip().lower()

    if target == "q":
        c = read_float("Specific heat capacity c (J/(kg*K)): ")
        mass = read_float("Mass m (kg): ")
        delta_t = read_float("Temperature change ΔT (K or °C): ")
        heat = c * mass * delta_t
        print(f"Q = {c} J/(kg*K) * {mass} kg * {delta_t} K")
        print(f"Q = {heat:.2f} J")

    elif target == "m":
        heat = read_float("Heat energy Q (J): ")
        c = read_float("Specific heat capacity c (J/(kg*K)): ")
        delta_t = read_float("Temperature change ΔT (K or °C): ")
        try:
            mass = heat / (c * delta_t)
            print(f"m = {heat} J / ({c} J/(kg*K) * {delta_t} K)")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("c * ΔT must not be 0!")

    elif target == "c":
        heat = read_float("Heat energy Q (J): ")
        mass = read_float("Mass m (kg): ")
        delta_t = read_float("Temperature change ΔT (K or °C): ")
        try:
            c = heat / (mass * delta_t)
            print(f"c = {heat} J / ({mass} kg * {delta_t} K)")
            print(f"c = {c:.2f} J/(kg*K)")
        except ZeroDivisionError:
            print("m * ΔT must not be 0!")

    elif target in {"t", "delt", "dt"}:
        heat = read_float("Heat energy Q (J): ")
        mass = read_float("Mass m (kg): ")
        c = read_float("Specific heat capacity c (J/(kg*K)): ")
        try:
            delta_t = heat / (mass * c)
            print(f"ΔT = {heat} J / ({mass} kg * {c} J/(kg*K))")
            print(f"ΔT = {delta_t:.2f} K")
        except ZeroDivisionError:
            print("m * c must not be 0!")

    else:
        error_message()


def velocity_calculator():
    print("Formula: v = s / t")
    print("------------------------\n")
    target = input("What are you looking for? (v, s or t): ").strip().lower()

    if target == "v":
        distance = read_length("Distance s (m): ")
        time_value = read_float("Time t (s): ")
        try:
            velocity = distance / time_value
            print(f"v = {distance} m / {time_value} s")
            print(f"v = {velocity:.2f} m/s")
        except ZeroDivisionError:
            print("The time t must not be 0!")

    elif target == "s":
        velocity = read_speed("Velocity v (m/s): ")
        time_value = read_float("Time t (s): ")
        distance = velocity * time_value
        print(f"s = {velocity} m/s * {time_value} s")
        print(f"s = {distance:.2f} m")

    elif target == "t":
        velocity = read_speed("Velocity v (m/s): ")
        distance = read_length("Distance s (m): ")
        try:
            time_value = distance / velocity
            print(f"t = {distance} m / {velocity} m/s")
            print(f"t = {time_value:.2f} s")
        except ZeroDivisionError:
            print("The velocity v must not be 0!")

    else:
        error_message()


def acceleration_calculator():
    print("Formula: a = Δv / Δt")
    print("------------------------\n")
    target = input("What are you looking for? (a, dv or dt): ").strip().lower()

    if target == "a":
        delta_v = read_speed("Velocity change Δv (m/s): ")
        delta_t = read_float("Time change Δt (s): ")
        try:
            acceleration = delta_v / delta_t
            print(f"a = {delta_v} m/s / {delta_t} s")
            print(f"a = {acceleration:.2f} m/s^2")
        except ZeroDivisionError:
            print("The time change must not be 0!")

    elif target == "dv":
        acceleration = read_float("Acceleration a (m/s^2): ")
        delta_t = read_float("Time change Δt (s): ")
        delta_v = acceleration * delta_t
        print(f"Δv = {acceleration} m/s^2 * {delta_t} s")
        print(f"Δv = {delta_v:.2f} m/s")

    elif target == "dt":
        acceleration = read_float("Acceleration a (m/s^2): ")
        delta_v = read_speed("Velocity change Δv (m/s): ")
        try:
            delta_t = delta_v / acceleration
            print(f"Δt = {delta_v} m/s / {acceleration} m/s^2")
            print(f"Δt = {delta_t:.2f} s")
        except ZeroDivisionError:
            print("The acceleration a must not be 0!")

    else:
        error_message()


def uniformly_moving_distance_calculator():
    print("Formula: s = v * t")
    print("------------------------\n")
    target = input("What are you looking for? (s, v or t): ").strip().lower()

    if target == "s":
        velocity = read_speed("Velocity v (m/s): ")
        time_value = read_float("Time t (s): ")
        distance = velocity * time_value
        print(f"s = {velocity} m/s * {time_value} s")
        print(f"s = {distance:.2f} m")

    elif target == "v":
        distance = read_length("Distance s (m): ")
        time_value = read_float("Time t (s): ")
        try:
            velocity = distance / time_value
            print(f"v = {distance} m / {time_value} s")
            print(f"v = {velocity:.2f} m/s")
        except ZeroDivisionError:
            print("The time t must not be 0!")

    elif target == "t":
        velocity = read_speed("Velocity v (m/s): ")
        distance = read_length("Distance s (m): ")
        try:
            time_value = distance / velocity
            print(f"t = {distance} m / {velocity} m/s")
            print(f"t = {time_value:.2f} s")
        except ZeroDivisionError:
            print("The velocity v must not be 0!")

    else:
        error_message()


def force_calculator():
    print("Formula: F = m * a")
    print("------------------------\n")
    target = input("What are you looking for? (F, m or a): ").strip().lower()

    if target == "f":
        mass = read_float("Mass m (kg): ")
        acceleration = read_float("Acceleration a (m/s^2): ")
        force = mass * acceleration
        print(f"F = {mass} kg * {acceleration} m/s^2")
        print(f"F = {force:.2f} N")

    elif target == "m":
        force = read_float("Force F (N): ")
        acceleration = read_float("Acceleration a (m/s^2): ")
        try:
            mass = force / acceleration
            print(f"m = {force} N / {acceleration} m/s^2")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("The acceleration a must not be 0!")

    elif target == "a":
        mass = read_float("Mass m (kg): ")
        force = read_float("Force F (N): ")
        try:
            acceleration = force / mass
            print(f"a = {force} N / {mass} kg")
            print(f"a = {acceleration:.2f} m/s^2")
        except ZeroDivisionError:
            print("The mass m must not be 0!")

    else:
        error_message()


def weight_force_calculator():
    print("Formula: Fg = m * g")
    print("------------------------\n")

    g_values = {
        "Earth": 9.81,
        "Moon": 1.62,
        "Mars": 3.71,
        "Jupiter": 24.79,
    }
    print("Typical values for g [m/s^2]:")
    for planet, value in g_values.items():
        print(f"{planet:<10} = {value} m/s^2")
    print("")

    target = input("What are you looking for? (Fg, m or g): ").strip().lower()

    if target == "fg":
        mass = read_float("Mass m (kg): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        force = mass * g
        print(f"Fg = {mass} kg * {g} m/s^2")
        print(f"Fg = {force:.2f} N")

    elif target == "m":
        weight_force = read_float("Weight force Fg (N): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        try:
            mass = weight_force / g
            print(f"m = {weight_force} N / {g} m/s^2")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("The gravitational acceleration g must not be 0!")

    elif target == "g":
        weight_force = read_float("Weight force Fg (N): ")
        mass = read_float("Mass m (kg): ")
        try:
            g = weight_force / mass
            print(f"g = {weight_force} N / {mass} kg")
            print(f"g = {g:.2f} m/s^2")
        except ZeroDivisionError:
            print("The mass m must not be 0!")

    else:
        error_message()


def spring_force_calculator():
    print("Formula: F = D * s")
    print("------------------------\n")
    target = input("What are you looking for? (F, D or s): ").strip().lower()

    if target == "f":
        spring_constant = read_float("Spring constant D (N/m): ")
        displacement = read_length("Displacement s (m): ")
        force = spring_constant * displacement
        print(f"F = {spring_constant} N/m * {displacement} m")
        print(f"F = {force:.2f} N")

    elif target == "d":
        force = read_float("Spring force F (N): ")
        displacement = read_length("Displacement s (m): ")
        try:
            spring_constant = force / displacement
            print(f"D = {force} N / {displacement} m")
            print(f"D = {spring_constant:.2f} N/m")
        except ZeroDivisionError:
            print("The displacement s must not be 0!")

    elif target == "s":
        spring_constant = read_float("Spring constant D (N/m): ")
        force = read_float("Spring force F (N): ")
        try:
            displacement = force / spring_constant
            print(f"s = {force} N / {spring_constant} N/m")
            print(f"s = {displacement:.2f} m")
        except ZeroDivisionError:
            print("The spring constant D must not be 0!")
    else:
        error_message()


def work_calculator():
    print("Formula: W = F * s")
    print("------------------------\n")

    target = input("What are you looking for? (W, F or s): ").strip().lower()

    if target == "w":
        force = read_float("Force F (N): ")
        distance = read_length("Distance s (m): ")
        work = force * distance
        print(f"W = {force} N * {distance} m")
        print(f"W = {work:.2f} J")

    elif target == "f":
        work_value = read_float("Work W (J): ")
        distance = read_length("Distance s (m): ")
        try:
            force = work_value / distance
            print(f"F = {work_value} J / {distance} m")
            print(f"F = {force:.2f} N")
        except ZeroDivisionError:
            print("The distance s must not be 0!")

    elif target == "s":
        force = read_float("Force F (N): ")
        work_value = read_float("Work W (J): ")
        try:
            distance = work_value / force
            print(f"s = {work_value} J / {force} N")
            print(f"s = {distance:.2f} m")
        except ZeroDivisionError:
            print("The force F must not be 0!")

    else:
        error_message()


def kinetic_energy_calculator():
    print("Formula: Ek = 1/2 * m * v^2")
    print("------------------------\n")
    target = input("What are you looking for? (Ek, m or v): ").strip().lower()

    if target == "ek":
        mass = read_float("Mass m (kg): ")
        velocity = read_speed("Velocity v (m/s): ")
        kinetic_energy = 0.5 * mass * velocity ** 2
        print(f"Ek = 0.5 * {mass} kg * ({velocity} m/s)^2")
        print(f"Ek = {kinetic_energy:.1f} J")

    elif target == "m":
        kinetic_energy = read_float("Kinetic energy Ek (J): ")
        velocity = read_speed("Velocity v (m/s): ")
        try:
            mass = (2 * kinetic_energy) / velocity ** 2
            print(f"m = (2 * {kinetic_energy} J) / ({velocity} m/s)^2")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("The velocity v must not be 0!")

    elif target == "v":
        kinetic_energy = read_float("Kinetic energy Ek (J): ")
        mass = read_float("Mass m (kg): ")
        try:
            velocity = (2 * kinetic_energy / mass) ** 0.5
            print(f"v = sqrt((2 * {kinetic_energy} J) / {mass} kg)")
            print(f"v = {velocity:.2f} m/s")
        except ZeroDivisionError:
            print("The mass m must not be 0!")

    else:
        error_message()


def potential_energy_calculator():
    print("Formula: Ep = m * g * h")
    print("------------------------\n")
    target = input("What are you looking for? (Ep, m, g or h): ").strip().lower()

    g_values = {
        "Earth": 9.81,
        "Moon": 1.62,
        "Mars": 3.71,
        "Jupiter": 24.79,
    }
    print("Typical values for g [m/s^2]:")
    for planet, value in g_values.items():
        print(f"{planet:<10} = {value} m/s^2")
    print("")

    if target == "ep":
        mass = read_float("Mass m (kg): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        height = read_float("Height h (m): ")
        potential_energy = mass * g * height
        print(f"Ep = {mass} kg * {g} m/s^2 * {height} m")
        print(f"Ep = {potential_energy:.2f} J")

    elif target == "m":
        potential_energy = read_float("Potential energy Ep (J): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        height = read_float("Height h (m): ")
        try:
            mass = potential_energy / (g * height)
            print(f"m = {potential_energy} J / ({g} m/s^2 * {height} m)")
            print(f"m = {mass:.4f} kg")
        except ZeroDivisionError:
            print("g * h must not be 0!")

    elif target == "g":
        potential_energy = read_float("Potential energy Ep (J): ")
        mass = read_float("Mass m (kg): ")
        height = read_float("Height h (m): ")
        try:
            g = potential_energy / (mass * height)
            print(f"g = {potential_energy} J / ({mass} kg * {height} m)")
            print(f"g = {g:.2f} m/s^2")
        except ZeroDivisionError:
            print("m * h must not be 0!")

    elif target == "h":
        potential_energy = read_float("Potential energy Ep (J): ")
        mass = read_float("Mass m (kg): ")
        g = read_float("Gravitational acceleration g (m/s^2): ")
        try:
            height = potential_energy / (mass * g)
            print(f"h = {potential_energy} J / ({mass} kg * {g} m/s^2)")
            print(f"h = {height:.2f} m")
        except ZeroDivisionError:
            print("m * g must not be 0!")

    else:
        error_message()


def power_calculator():
    print("Formula: P = W / t")
    print("------------------------\n")
    target = input("What are you looking for? (P, W or t): ").strip().lower()

    if target == "p":
        work_value = read_float("Work W (J): ")
        time_value = read_float("Time t (s): ")
        try:
            power = work_value / time_value
            print(f"P = {work_value} J / {time_value} s")
            print(f"P = {power:.2f} W")
        except ZeroDivisionError:
            print("The time t must not be 0!")

    elif target == "w":
        power = read_float("Power P (W): ")
        time_value = read_float("Time t (s): ")
        work_value = power * time_value
        print(f"W = {power} W * {time_value} s")
        print(f"W = {work_value:.2f} J")

    elif target == "t":
        power = read_float("Power P (W): ")
        work_value = read_float("Work W (J): ")
        try:
            time_value = work_value / power
            print(f"t = {work_value} J / {power} W")
            print(f"t = {time_value:.2f} s")
        except ZeroDivisionError:
            print("The power P must not be 0!")

    else:
        error_message()


# Backward-compatible aliases for the original German function names.
def fehler():
    error_message()


def dicht_rechner():
    density_calculator()


def druck_rechner():
    pressure_calculator()


def waerme_rechner():
    heat_calculator()


def schmelz_rechner():
    melting_heat_calculator()


def verdampfungs_rechner():
    vaporization_heat_calculator()


def dampferwaermung_rechner():
    steam_heating_calculator()


def geschwindigkeit_rechner():
    velocity_calculator()


def beschleunigung_rechner():
    acceleration_calculator()


def weg_gleichmäßig_bewegung_rechner():
    uniformly_moving_distance_calculator()


def kraft_rechner():
    force_calculator()


def gewichts_kraft_rechner():
    weight_force_calculator()


def federkraft_rechner():
    spring_force_calculator()


def arbeit_rechner():
    work_calculator()


def kinetische_energie_rechner():
    kinetic_energy_calculator()


def potentielle_energie_rechner():
    potential_energy_calculator()


def leistung_rechner():
    power_calculator()


def geschwindigkeit_check(var, prompts):
    if ask_yes_no(f"Is {var} given in km/h? (j/n): "):
        return kmh_to_ms(read_float(prompts[var]))
    return read_float(prompts[var])
