"""
EXAMPLE: How to make a formula backend-ready.

This file uses the velocity formula (v = s / t) to demonstrate
the pattern for converting all formulas from funktionen.py.

The idea: separate pure math from I/O so the same formula
can be used by the CLI, a Flask API, or anything else.

Three layers:
    1. Pure formula    -> takes floats, returns float (or raises)
    2. CLI wrapper     -> prompts user, calls formula, prints result
    3. API wrapper     -> accepts dict, calls formula, returns dict
"""

import math


# =============================================================================
# 1. PURE FORMULAS (no input, no print, no side effects)
# =============================================================================
# These are the building blocks. They work in base SI units:
# distance in meters, time in seconds, velocity in m/s.
# Unit conversion happens OUTSIDE these functions (in the CLI/API layer).

def calc_velocity(distance, time):
    """v = s / t

    Args:
        distance: Distance in meters (m).
        time:     Time in seconds (s).

    Returns:
        Velocity in m/s.

    Raises:
        ZeroDivisionError: If time is 0.
    """
    if time == 0:
        raise ZeroDivisionError("Time must not be 0.")
    return distance / time


def calc_distance(velocity, time):
    """s = v * t

    Args:
        velocity: Velocity in m/s.
        time:     Time in seconds (s).

    Returns:
        Distance in meters (m).
    """
    return velocity * time


def calc_time(distance, velocity):
    """t = s / v

    Args:
        distance: Distance in meters (m).
        velocity: Velocity in m/s.

    Returns:
        Time in seconds (s).

    Raises:
        ZeroDivisionError: If velocity is 0.
    """
    if velocity == 0:
        raise ZeroDivisionError("Velocity must not be 0.")
    return distance / velocity


# =============================================================================
# 2. REFERENCE DATA (for the UI to display)
# =============================================================================
# Instead of printing these inside the formula, we store them as data.
# The CLI can print them, the web UI can render them as a table.

VELOCITY_FORMULA_INFO = {
    "name": "Velocity",
    "formula": "v = s / t",
    "description": "Calculates velocity from distance and time.",
    "variables": {
        "v": {"name": "Velocity",   "unit": "m/s",  "can_solve_for": True},
        "s": {"name": "Distance",    "unit": "m",    "can_solve_for": True},
        "t": {"name": "Time",        "unit": "s",    "can_solve_for": True},
    },
    "reference_values": {
        "Speed of sound": {"unit": "m/s", "value": 343},
        "Speed of light": {"unit": "m/s", "value": 299_792_458},
        "1 km/h":         {"unit": "m/s", "value": 1 / 3.6},
    },
}


# =============================================================================
# 3. CLI WRAPPER (interactive, same UX as original funktionen.py)
# =============================================================================
# This replaces the old velocity_calculator(). It reads user input,
# calls the pure formula, and prints the result.
# The CLI can live in main.py or a separate CLI module.

def read_float(prompt):
    """Read a float from the user, accepting comma as decimal separator."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Please enter a valid number.")


def kmh_to_ms(value):
    """Convert km/h to m/s."""
    return value / 3.6


def cm_to_m(value):
    """Convert cm to m."""
    return value / 100.0


def velocity_calculator_cli():
    """Interactive CLI for the velocity formula.

    This is equivalent to the old velocity_calculator() in funktionen.py.
    The only difference: it calls calc_velocity() instead of doing the math inline.
    """
    print("Formula: v = s / t")
    print("------------------------\n")

    target = input("What are you looking for? (v, s or t): ").strip().lower()

    if target == "v":
        distance = read_float("Distance s (m): ")
        time = read_float("Time t (s): ")
        try:
            result = calc_velocity(distance, time)
            print(f"v = {distance} m / {time} s")
            print(f"v = {result:.2f} m/s")
        except ZeroDivisionError as e:
            print(e)

    elif target == "s":
        velocity = read_float("Velocity v (m/s): ")
        time = read_float("Time t (s): ")
        result = calc_distance(velocity, time)
        print(f"s = {velocity} m/s * {time} s")
        print(f"s = {result:.2f} m")

    elif target == "t":
        velocity = read_float("Velocity v (m/s): ")
        distance = read_float("Distance s (m): ")
        try:
            result = calc_time(distance, velocity)
            print(f"t = {distance} m / {velocity} m/s")
            print(f"t = {result:.2f} s")
        except ZeroDivisionError as e:
            print(e)

    else:
        print("Invalid variable. Please enter v, s, or t.")


# =============================================================================
# 4. API WRAPPER (for Flask, returns dicts)
# =============================================================================
# This is what a Flask route would call. It takes already-parsed
# numbers and returns a dict that gets serialized to JSON.
# No Flask import needed here - the Flask app imports this function.

def velocity_api(solve_for, **kwargs):
    """Calculate velocity formula for a web API.

    Args:
        solve_for: Which variable to solve for ("v", "s", or "t").
        **kwargs:  The other variables as numbers.
                   E.g. velocity_api("v", s=100, t=9.5)

    Returns:
        dict with "success" key. On success:
            {"success": True, "result": float, "unit": str, "formula": str}
        On failure:
            {"success": False, "error": str}
    """
    try:
        if solve_for == "v":
            result = calc_velocity(kwargs["s"], kwargs["t"])
            unit = "m/s"
        elif solve_for == "s":
            result = calc_distance(kwargs["v"], kwargs["t"])
            unit = "m"
        elif solve_for == "t":
            result = calc_time(kwargs["s"], kwargs["v"])
            unit = "s"
        else:
            return {"success": False, "error": f"Unknown variable: {solve_for}"}

        return {
            "success": True,
            "result": round(result, 4),
            "unit": unit,
            "formula": VELOCITY_FORMULA_INFO["formula"],
        }

    except ZeroDivisionError as e:
        return {"success": False, "error": str(e)}
    except KeyError as e:
        return {"success": False, "error": f"Missing variable: {e}"}


# =============================================================================
# DEMO (run this file directly to see it in action)
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO: Velocity Formula - Backend Ready")
    print("=" * 60)

    # Demo 1: Pure formula
    print("\n--- Pure Formula ---")
    print(f"calc_velocity(100, 9.5) = {calc_velocity(100, 9.5):.2f} m/s")
    print(f"calc_distance(10.53, 9.5) = {calc_distance(10.53, 9.5):.2f} m")
    print(f"calc_time(100, 10.53) = {calc_time(100, 10.53):.2f} s")

    # Demo 2: API wrapper
    print("\n--- API Response (solving for v) ---")
    response = velocity_api("v", s=100, t=9.5)
    print(response)

    print("\n--- API Response (solving for s) ---")
    response = velocity_api("s", v=10.53, t=9.5)
    print(response)

    print("\n--- API Response (division by zero) ---")
    response = velocity_api("v", s=100, t=0)
    print(response)

    print("\n--- API Response (missing variable) ---")
    response = velocity_api("v", s=100)
    print(response)

    # Demo 3: Formula metadata
    print("\n--- Formula Metadata ---")
    print(f"Name: {VELOCITY_FORMULA_INFO['name']}")
    print(f"Formula: {VELOCITY_FORMULA_INFO['formula']}")
    for var, info in VELOCITY_FORMULA_INFO["variables"].items():
        print(f"  {var}: {info['name']} [{info['unit']}]")
