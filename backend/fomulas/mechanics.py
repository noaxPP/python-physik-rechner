from helpers import *
#velocity, accelaration, force, etc.
# VELOCITY

def calc_velocity(distance, time):
    """Formula: v = s / t

    Args:
        distance: Distance in meters (m).
        time: Time in seconds (s).

    Return:
        Velocity in m/s.

    Raises:
        ZeroDivisionError: if time is 0.
    """
    if time == 0:
        raise ZeroDivisionError("Time must not be 0.")
    return distance / time

def calc_distance(velocity, time):
    """Formula: s = v * t

    Args:
        velocity: Velocity in m/s (m/s).
        time: Time in seconds (s).
    
    Return:
        Distance in meters (m).
    """
    return velocity * time

def calc_time(velocity, distance):
    """Formula: t = s / v

    Args:
        velocity: Velocity in m/s (m/s).
        distance: Distande in meters (m).

    Return:
        Time in seconds (s).

    Raises:
        ZeroDivisionError: if velocity is 0.
    """
    if velocity == 0:
        raise ZeroDivisionError("Velocity must not be 0.")
    return distance / velocity
 
VELOCITY_FORMULA_INFO = {
    "name": "Velocity",
    "formula": "v = s / t",
    "description": "Calculates Velocity from Distance and Time",
    "history": {
        "scientists": [
            "Galileo Galilei",
            "Isaac Newton"
        ],
        "summary": "The mathematical study of motion started with Galileo Galilei, who investigated how objects move. Isaac Newton later developed the laws of motion that describe movement using forces."
    },
    "learning": {
        "remember": "Think: How far did something travel and how long did it take? Velocity tells you the distance covered per unit of time.",
        "important": "Velocity describes how fast an object moves and includes direction in physics. The SI unit is meters per second (m/s)."
    },
    "variables": {
        "v": {"name": "Velocity", "unit": "m/s", "can_solve_for": True},
        "s": {"name": "Distance", "unit": "m", "can_solve_for": True},
        "t": {"name": "Time", "unit": "s", "can_solve_for": True}
    },
    "reference_values": {
        "Speed of sound": {"unit": "m/s", "value": 343},
        "Speed of light": {"unit": "m/s", "value": 299_792_458},
        "Walking speed": {"unit": "m/s", "value": 1.4},
        "car speed": {"unit": "m/s", "value": 13.9},
        "1 km/h": {"unit": "m/s", "value": 1 / 3.6}
    }
}   

def velocity_api(solve_for, **kwargs):
    """Calc velocity formula for web API.

    Args:
        solve_for: Which variable to solve for ("v", "s" or "t")
        **kwargs: The other variables as numbers.
                  E.g velocity_api("v", s=100, t=9.5)
        
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
            return {"success": False, "error": f"Unknown variable {solve_for}"}
        
        return {
            "success": True,
            "result": round(result, 4),
            "unit": unit,
            "formula": VELOCITY_FORMULA_INFO["formula"] 
        }

    except ZeroDivisionError as e:
        return {"success": False, "error": str(e)}
    except KeyError as e:
        return {"success": False, "error": f"Missing variable: {e} "}
#------------------------------------------------------------ 
# ACCELERATION

def calc_acceleration(delta_velocity, delta_time):
    
    """Formula: a = ∆v / ∆t

    Args:
        delta_velocity: Velocity change in m/s.
        delta_time: Time change in s.

    Return:
        Acceleration in m/s^2}

    Raises:
        ZeroDivisionError: if ∆t is 0.
    """
    if delta_time == 0:
        raise ZeroDivisionError("∆t must not be 0.")
    return delta_velocity / delta_time

def calc_delta_velocity(acceleration, delta_time):
    """Formula: ∆v = a * ∆t

    Args:
        accelaration: Accelaration in m/s^2.
        delta_time: Time change in s.

    Return:
        Velocity change in m/s.
    """
    return acceleration * delta_time

def calc_delta_time(acceleration, delta_velocity):
    """Formula: ∆t = a / ∆v
    
    Args:
        acceleration: Acceleration in m/s^2.
        delta_velocity: Velocity change in m/s.

    Return:
        Time change in s.

    Raises:
        ZeroDivisionError: if ∆v is 0.
    """
    if delta_velocity == 0:
        raise ZeroDivisionError("∆v must not be 0.")
    return acceleration / delta_velocity

ACCELERATION_FORMULA_INFO = {
    "name": "Acceleration",
    "formula": "a = ∆v / ∆t",
    "description": "Calculates Acceleration from the change of Velocity and Time.",
    "history": {
        "scientists": [
            "Isaac Newton",
            "Galileo Galilei"
        ],
        "summary": "The understanding of acceleration developed through studies of motion. Newton explained that forces cause changes in motion, creating the foundation of classical mechanics."
    },
    "learning": {
        "remember": "Acceleration means a change in velocity. A car accelerating is not only getting faster; changing direction is also acceleration.",
        "important": "Acceleration describes how quickly velocity changes. The SI unit is meters per second squared (m/s²)."
    },
    "variables": {
        "a": {"name": "Acceleration", "unit": "m/s²", "can_solve_for": True},
        "∆v": {"name": "Change in Velocity", "unit": "m/s", "can_solve_for": True},
        "∆t": {"name": "Time interval", "unit": "s", "can_solve_for": True}
    },
    "reference_values": {
        "Earth gravity": {"unit": "m/s²", "value": 9.81},
        "Car from 0-100 in 4 sec": {"unit": "m/s²", "value": 25}
    }   
}

def acceleration_api(solve_for, **kwargs):
    """Calc acceleration formula for web api.
    
    Args:
        solve_for: Which variable to solve for ("a", "∆v" or "∆t")
        **kwargs: The other variables as numbers.
                  E.g acceleration_api("a", ∆v=3, ∆t=9)
                
    Returns:
        dict with "success2 key.
        On success: {"success": True, "result": float, "unit": str, "formula": str}
        On failure: {"success": False, "error": str}
    """
    try:
        if solve_for == "a":
            result = calc_acceleration(kwargs["∆v"], kwargs["∆t"])
            unit = "m/s²"
        elif solve_for == "dt":
            result = calc_delta_time(kwargs["a"], kwargs["∆v"])
            unit = "s"
        elif solve_for == "dv":
            result = calc_delta_velocity(kwargs["a"], kwargs["∆t"])
            unit = "m/s"
        else:
            return {"success": False, "error": f"Unknown variable {solve_for}."}

        return {
            "success": True,
            "result": round(result, 4),
            "unit": unit,
            "formula": ACCELERATION_FORMULA_INFO["formula"]
        }
    except ZeroDivisionError as e:
        return {"success": False, "error": str(e)}
    except KeyError as e:
        return {"success": False, "error": f"Missing variable: {e}"}
#------------------------------------------------------------
# FORCE

def calc_force(mass, acceleration):
    """Formula: F = m * a
    
    Args:
        mass: Mass m in kg.
        acceleration: Acceleration a in m/s².

    Return:
        Force in N
    """
    return mass * acceleration

def calc_mass(force, acceleration):
    """Formula: m = F / a

    Args:
        force: Force F in N
        acceleration: Acceleration a in m/s²
    
    Return:
        Mass in kg

    Raises:
        ZeroDivisionError: if acceleration is 0.
    """
    if acceleration == 0:
        raise ZeroDivisionError("a must not be 0.")
    return force / acceleration

def calc_acceleration_from_force(mass, force):
    """Formula: a = m / F

    Args:
        mass: Mass m in kg.
        force: Force F in N.

    Return:
        Acceleration a in m/s²

    Raises:
        ZerodivisionError: if force is 0.
    """
    if force == 0:
        raise ZeroDivisionError("f must not be 0.")
    return mass / force

FORCE_FORMULA_INFO = {
    "name": "Force",
    "formula": "f = m * a",
    "description": "Calculates force from mass and acceleration.",
    "history": {
        "scientists": [
            "Isaac Newton"
        ],
        "summary": "Isaac Newton introduced the relationship between force, mass and acceleration in his second law of motion, published in 1687."
    },
    "learning": {
        "remember": "Force describes a push or pull. A heavier object or a stronger acceleration requires more force.",
        "important": "Force is measured in Newtons (N). One Newton is the force needed to accelerate one kilogram by one meter per second squared."
    },
    "variables": {
        "F": {"name": "Force", "unit": "N", "can_solve_for": True},
        "m": {"name": "Mass", "unit": "kg", "can_solve_for": True},
        "a": {"name": "Acceleration", "unit": "m/s²", "can_solve_for": True}
    },
    "reference_values": {
        "Gravity force of a 1kg objekt": {"unit": "N", "value": 9.81},
    }
}

def force_api(solve_for, **kwargs):
    """Calc force formula for web api.
    
    Args:
        solve_for: Which variable to solve for ("a", "F" or "m")
        **kwargs: The other variables as numbers.
                  E.g force_api("F", m=3, a=9)
                
    Returns:
        dict with "success2 key.
        On success: {"success": True, "result": float, "unit": str, "formula": str}
        On failure: {"success": False, "error": str}
    """
    try:
        if solve_for == "f":
            result = calc_force(kwargs["m"], kwargs["a"])
            unit = "N"
        elif solve_for == "m":
            result = calc_mass(kwargs["f"], kwargs["a"])
            unit = "kg"
        elif solve_for == "a":
            result = calc_acceleration_from_force(kwargs["m"], kwargs["f"])
            unit = "m/s²"
        else:
            return {"success": False, "error": f"Unknown variable: {solve_for}."}
        
        return {
            "success": True,
            "result": round(result, 4),
            "unit": unit,
            "formula": FORCE_FORMULA_INFO["formula"]
            }
    except ZeroDivisionError as e:
        return {"success": False, "error": str(e)}
    except KeyError as e:
        return {"success": False, "error": f"Missing variable: {e}"}