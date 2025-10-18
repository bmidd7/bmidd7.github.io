AcceptableYesResponses = ["y", "yes"]
AcceptableNoResponses = ["n", "no"]

AcceptableGramsUnits = ["g", "grams", "gram"]
AcceptableKilogramsUnits = ["k", "kg", "kilo", "kilos", "kilograms", "kilogram"]
AcceptableMTonnesUnits = ["mt", "tonnes", "metric tonnes", "tonne", "metric tonne"]

AcceptableOunceUnits = ["o", "oz", "ounces", "ounce"]
AcceptablePoundUnits = ["l", "lb", "lbs", "pounds", "pound"]
AcceptableTonsUnits = ["t", "tons", "ton"]

AcceptableMetricMassUnits = (
    AcceptableGramsUnits + AcceptableKilogramsUnits + AcceptableMTonnesUnits
)
AcceptableImperialMassUnits = (
    AcceptableOunceUnits + AcceptablePoundUnits + AcceptableTonsUnits
)
AcceptableMassUnits = AcceptableMetricMassUnits + AcceptableImperialMassUnits

Acceptable=1


AcceptableChemistryResponses = ["c", "chemistry", "chem", "acp"]
AcceptableEngineeringResponses = ["e", "engineering", "eng", "pltw", "poe", "p"]

AcceptableOtherResponses = ["o", "other", "oth"]

AcceptableEnergyResponses = ["e", "energy", "eng"]
AcceptableLeverResponses = ["l", "lever", "lev"]

import os


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("Invalid operating system. Please use Windows, Mac, or Linux")

def get_single_value(Unit_Power):
    while True:
        U = input(f"Enter the amount of {Unit_Power}, then press enter\n").strip()
        if U == "":
            U = None
            return None
        try:
            return float(U)
        except ValueError:
            input("Please don't enter units, other letters, or symbols, just numbers. Press enter to try again.""\n""Remember, you can use a decimal point, if needed.")
            clear_screen()

def get_single_unit(Unit_Name):
    while True:
        U = input(f"Enter the unit for {Unit_Name}, then press enter\n").lower().strip()
        if U == "":
            return None
        elif U in AcceptableMassUnits:
            return U
        else:
            input("Invalid mass unit, please try again. Press enter to try again.""\n""Acceptable units are: g, kg, t, oz, lb, or tn")
            clear_screen()

# return raw string inputs (empty string if blank) .isdigit()
def get_all_values():
    global inputWatt, inputMassUnit, inputMass, inputVolt, inputAmp, inputNewton, inputDistance, inputAcceleration, inputSecond
    inputWatt = get_single_value("Watts")
    inputMassUnit = get_single_unit("Mass")
    if inputMassUnit is not None:
        inputMass = get_single_value("Mass")
    inputVolt = get_single_value("Volts (V)")
    inputAmp = get_single_value("Amperes (Amps)")
    inputNewton = get_single_value("Newtons")
    inputDistance = get_single_value("Distance")
    inputAcceleration = get_single_value("Acceleration")
    inputSecond = get_single_value("Seconds")

def turn_input_mass_unit_to_g():
    global MassUnit
    if inputMassUnit not in AcceptableMassUnits:
        print("Invalid mass unit, please try again")
        MassUnit = None
    elif inputMassUnit in AcceptableGramsUnits:
        MassUnit = "g"
    elif inputMassUnit in AcceptableKilogramsUnits:
        MassUnit = "kg"
    elif inputMassUnit in AcceptableMTonnesUnits:
        MassUnit = "t"
    elif inputMassUnit in AcceptableOunceUnits:
        MassUnit = "oz"
    elif inputMassUnit in AcceptablePoundUnits:
        MassUnit = "lb"
    elif inputMassUnit in AcceptableTonsUnits:
        MassUnit = "tn"


def convert_mass_amount_to_g():
    global Mass_in_Grams
    if MassUnit is None:
        Mass_in_Grams = None
    if MassUnit == "g":
        Mass_in_Grams = inputMass
    elif MassUnit == "kg":
        Mass_in_Grams = inputMass * 1000.0
    elif MassUnit == "t":
        Mass_in_Grams = inputMass * 1_000_000.0
    elif MassUnit == "oz":
        # 1 oz = 28.349523125 g
        Mass_in_Grams = inputMass * 28.349523125
    elif MassUnit == "lb":
        # 1 lb = 453.59237 g
        Mass_in_Grams = inputMass * 453.59237
    elif MassUnit == "tn":
        # short ton = 907184.74 g (907.18474 kg)
        Mass_in_Grams = inputMass * 907184.74
    return None

def print_current_values(inputWatt, mass_in_grams, inputVolt, inputAmp, inputNewton, inputDistance, inputAcceleration, inputSecond):
    print("Current values are:")
    print("Power (W):", inputWatt)
    if inputMassUnit is None:
        print("Weight (Unknown Unit): ", mass_in_grams)
    else:
        print(f"Weight ({inputMassUnit}):", mass_in_grams)
    print("Voltage (V):", inputVolt)
    print("Current (A):", inputAmp)
    print("Force (N):", inputNewton)
    print("Distance (m):", inputDistance)
    print("Acceleration (m/s/s):", inputAcceleration)
    print("Time (s):", inputSecond)
    print()

def find_joules_f_d(n, distance):
        global inputDistance, joule
        if n is None:
            print("Cannot compute Joules from force and distance: missing force.")
            inputnewtonsYorN = input("Would you like to input newtons (i), calculate newtons (n), calculate joules using Power and Time (p), or return to menu (r)? (y/n)")
            if inputdistanceYorN in AcceptableYesResponses:
                inputDistance = get_single_value("Distance")
        if distance is None:
            print("Cannot compute Joules from force and distance: missing distance.")
            inputdistanceYorN = input("Would you like to input distance? (y/n)\n")
            if inputdistanceYorN in AcceptableYesResponses:
                inputDistance = get_single_value("Distance")
        joule = n * distance


def find_joules_p_t(power, seconds):
    if power is None or seconds is None:
        print("Cannot compute Joules from power and time: missing power or time.")
        return None
    return power * seconds


def energy_calculator():
    clear_screen()
    print("Welcome to the Energy Calculator!")
    print("For the following questions, if you do not have the value, just press enter, otherwise, enter the value and press enter\n")

    get_all_values()

    # normalize unit and convert mass to grams
    turn_input_mass_unit_to_g()
    convert_mass_amount_to_g()

    clear_screen()
    print_current_values(inputWatt, Mass_in_Grams, inputVolt, inputAmp, inputNewton, inputDistance, inputAcceleration, inputSecond)


    Solvefor = input("What do you want to solve for? (Joules (J), Amps (A), Watts (W), Volts (V), or Newtons (N)), then press enter\n").lower().strip()
    if Solvefor not in ["j", "a", "w", "v", "n"]:
        print("Invalid input, please try again")
        return

    if Solvefor == "j":
        whichJoule = input("Do you want to use force and distance (f) or power and time (p)?\n").lower().strip()
        if whichJoule == "f":
            joules = find_joules_f_d(inputNewton, inputDistance)
        elif whichJoule == "p":
            joules = find_joules_p_t(inputWatt, inputSecond)
        else:
            print("Invalid selection for Joules calculation.")
            return
        if joules is not None:
            print("The energy is", joules, "J")

    elif Solvefor == "a":
        if inputWatt is None or inputVolt is None or inputVolt == 0:
            print("Cannot compute Amps: need power (W) and voltage (V) (voltage must be non-zero).")
        else:
            amps = inputWatt / inputVolt
            print("The current in amps is", amps, "A")

    elif Solvefor == "w":
        whichWatt = input("Do you want to use volts and amps (e) or force, distance, & time (f)? (e/n)\n").lower().strip()
        if whichWatt == "e":
            if inputVolt is None or inputAmp is None:
                print("Cannot compute Watts: need voltage and current.")
            else:
                watt = inputVolt * inputAmp
                print("The power in watts is", watt, "W")
        elif whichWatt == "f":
            # power = work / time = (force * distance) / time
            if inputNewton is None or inputDistance is None or inputSecond is None or inputSecond == 0:
                print("Cannot compute Watts from force/distance/time: need force, distance and non-zero time.")
            else:
                watt = (inputNewton * inputDistance) / inputSecond
                print("The power in watts is", watt, "W")
        else:
            print("Invalid selection for Watts calculation.")

    elif Solvefor == "v":
        if inputWatt is None or inputAmp is None or inputAmp == 0:
            print("Cannot compute Volts: need power (W) and current (A) (current must be non-zero).")
        else:
            volt = inputWatt / inputAmp
            print("The voltage in volts is", volt, "V")

    elif Solvefor == "n":
        use_mass_only = input("Do you want to use only mass to calculate newtons? (y/n)\n").lower().strip()
        if use_mass_only in AcceptableYesResponses:
            if Mass_in_Grams is None:
                print("Cannot compute Newtons from mass: missing mass or unit.")
            else:
                mass_kg = Mass_in_Grams / 1000.0
                newton = mass_kg * 9.81
                print("The force in newtons is", newton, "N")
        elif use_mass_only in AcceptableNoResponses:
            # attempt to compute force from energy/time or other provided inputs — here use: F = (work / distance) if possible
            if inputWatt is not None and inputSecond is not None and inputDistance is not None and inputDistance != 0:
                # Work = Power * time, Force = Work / distance
                work = inputWatt * inputSecond
                newton = work / inputDistance
                print("The force in newtons is", newton, "N (computed from power * time / distance)")
            else:
                print("Cannot compute Newtons using non-mass method: need power, time and distance.")
        else:
            print("Invalid response, please try again")

def MainMenu():
    while True:
        clear_screen()
        ClassEquationChoice = input(
                "Enter what class you need this for?"
                "\nChemisty (c), Engineering (e), or Other (o)?"
                "\nType your answer, then press enter\n"
            ).lower().strip()
        if ClassEquationChoice in AcceptableChemistryResponses:
            input("Chemistry calculations are not implemented yet. Try a different option. Press enter to continue.")
        elif ClassEquationChoice in AcceptableEngineeringResponses:
            MainPLTW()
        elif ClassEquationChoice in AcceptableOtherResponses:
            input("Other calculations are not implemented yet. Try a different option. Press enter to continue.")
        elif ClassEquationChoice == "":
            energy_calculator()

def MainPLTW():
    clear_screen()
    PLTWEquationType = input(
                            "Which of the following is your problem?"
                            "\nEnergy-Related (e), Lever-Related (l), or Other (o)?"
                            "\nType your answer, then press enter\n"
    ).lower().strip()
    if PLTWEquationType in AcceptableEnergyResponses:
        energy_calculator()
    elif PLTWEquationType in AcceptableLeverResponses:
        print("You just wasted your time. Kinda. Lever calculations are not implemented yet.\nTry a different option. Please🥺")


if __name__ == "__main__":
    MainMenu()
