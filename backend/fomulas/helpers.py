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