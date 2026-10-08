# Week 1.2, Session 2: Task 6


def evaluate_temperature(temperature):
    if temperature > 80:
        print("TEMPERATURE TOO HIGH! Shut down this machine now.")
        return True
    elif temperature > 50:
        print("Temperature is ok. No further action is needed.")
    else:
        print("Temperature is low. No further action is needed.")
    return False

def evaluate_pressure(pressure):
    if pressure > 100:
        print("PRESSURE TOO HIGH! Begin maintenance.")
        return True
    elif pressure > 50:
        print("Pressure is ok. No further action is needed.")
    else:
        print("Pressure is low. No further action is needed.")
    return False

def evaluate_machine(status, temperature, pressure):
    if status:
        tempUnsafe = evaluate_temperature(temperature)
        pressUnsafe = evaluate_pressure(pressure) # have to put both in their own bools to force both of them to run. 
        if pressUnsafe or tempUnsafe:
            print("Unsafe conditions detected: please shut down this machine and perform advised maintenance.")
        else:
            print("The machine is currently working as expected.")
    else:
        print("The machine has shut down and no further action is required.")

print("Welcome to the factory program.")

temperature = float(input("Enter temperature (C): "))
pressure = float(input("Enter pressure (PSI): "))
status = (input("Enter operational status (1 for on and 0 for off): ")) == "1" 

evaluate_machine(status, temperature, pressure)