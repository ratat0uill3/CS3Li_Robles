def calculate_fuel(cargo_weight):
    total_weight = cargo_weight + 50000
    fuel = total_weight * 3
    return fuel

total_cargo_weight = 0

while True:
    cargos = input("Enter the cargo type satellite/rover/supplies. (Type launch to deploy): ")
    if cargos == "launch":
        break

    if cargos == "satellite":
        total_cargo_weight = total_cargo_weight + 1000
    elif cargos == "rover":
        total_cargo_weight = total_cargo_weight + 2500
    elif cargos == "supplies":
        total_cargo_weight = total_cargo_weight + 500
    else:
        print("Invalid cargo type.")

    if total_cargo_weight > 10000:
        print("MAX WEIGHTREACHED")
        break

print("Total cargo weight:", total_cargo_weight, "kg")
print("Fuel needed:", calculate_fuel(total_cargo_weight), "liters")
