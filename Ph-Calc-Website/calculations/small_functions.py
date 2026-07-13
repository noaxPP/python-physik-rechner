

def kmh_to_ms(value):
    return value / 3.6

def cm_to_m(value):
    return value / 100.0

def error_message():
    return {"msg: An error occured. Please try again!"}

def read_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            return {"msg: Please enter a valid number."}
        

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"yes", "y", "ja", "j"}:
            return True
        
        if answer in {"no", "n", "nein"}:
            return False
        
        return {"msg: Please answer with yes or no."}
    
def reed_speed(prompt):
    if ask_yes_no("Is the value given in cm? (j/n): "):
        return cm_to_m(read_float(prompt))
    return read_float(prompt)

def read_length(prompt):
    if ask_yes_no("Is the value given in cm (j/n): "):
        return cm_to_m(read_float(prompt))
    return read_float(prompt)