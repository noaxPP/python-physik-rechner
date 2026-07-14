from funktionen import *
import time


def main():
    while True:
        print("")
        print("Physics Calculator")
        print("-------------------------------")
        print("Which topic do you want to choose?")
        print("""
        1. Mechanics
        2. Work, Energy and Power
        3. Density and Pressure
        4. Heat
        """)

        try:
            choice = int(input("Menu number: "))
        except ValueError:
            error_message()
            time.sleep(1)
            continue

        if choice == 1:
            print("""
            1. Motion
            2. Forces
            """)
            selection = int(input("Menu number: "))
            if selection == 1:
                print("""
                1. Velocity
                2. Acceleration
                3. Distance in uniform motion
                """)
                formula_choice = int(input("Formula number: "))
                if formula_choice == 1:
                    velocity_calculator()
                elif formula_choice == 2:
                    acceleration_calculator()
                elif formula_choice == 3:
                    uniformly_moving_distance_calculator()
                else:
                    error_message()
            elif selection == 2:
                print("""
                1. Force
                2. Weight force
                3. Hooke's law (spring force)
                """)
                formula_choice = int(input("Formula number: "))
                if formula_choice == 1:
                    force_calculator()
                elif formula_choice == 2:
                    weight_force_calculator()
                elif formula_choice == 3:
                    spring_force_calculator()
                else:
                    error_message()
            else:
                error_message()

        elif choice == 2:
            print("""
            1. Work
            2. Energy
            3. Power
            """)
            selection = int(input("Menu number: "))
            if selection == 1:
                work_calculator()
            elif selection == 2:
                print("""
                1. Kinetic Energy
                2. Potential Energy
                """)
                formula_choice = int(input("Formula number: "))
                if formula_choice == 1:
                    kinetic_energy_calculator()
                elif formula_choice == 2:
                    potential_energy_calculator()
                else:
                    error_message()
            elif selection == 3:
                power_calculator()
            else:
                error_message()

        elif choice == 3:
            print("""
            1. Density
            2. Pressure
            """)
            selection = int(input("Menu number: "))
            if selection == 1:
                density_calculator()
            elif selection == 2:
                pressure_calculator()
            else:
                error_message()

        elif choice == 4:
            print("""
            1. Heat
            2. Melting heat
            3. Vaporization heat
            4. Steam heating
            """)
            selection = int(input("Menu number: "))
            if selection == 1:
                heat_calculator()
            elif selection == 2:
                melting_heat_calculator()
            elif selection == 3:
                vaporization_heat_calculator()
            elif selection == 4:
                steam_heating_calculator()
            else:
                error_message()

        else:
            error_message()

        time.sleep(1.5)


if __name__ == "__main__":
    main()