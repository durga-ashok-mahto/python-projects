print("1 KM to Miles")
print("2 KG to Pounds")

choice = input("Choose option: ")

if choice == "1":
    km = float(input("Enter KM: "))
    print("Miles:", km * 0.621371)

elif choice == "2":
    kg = float(input("Enter KG: "))
    print("Pounds:", kg * 2.20462)
