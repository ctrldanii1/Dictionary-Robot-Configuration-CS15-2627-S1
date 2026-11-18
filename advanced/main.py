robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

while True:
    print("\nMenu")
    print("\n1. View All Settings ")
    print("2. Look Up A Setting")
    print("3. Change A Setting")
    print("4. Add A Setting")
    print("5. Exit")

    choice = int(input("Enter an option (1-5): "))

    if choice == 1:
        print("View All Settings")
        for key, value in robot.items():
            print(key, ":", value)

    elif choice == 2:
        print("Look Up A Setting")
        lookup = input("Enter a lookup key:")
        value = robot.get(lookup, "Setting not found")
        print(value)

    elif choice == 3:
        print("Change A Setting")
        key_change = input("Enter a key to change:")
        if key_change in robot:
            robot[key_change] = input("Enter new value:")
            print("Key has been updated")
        else:
            print("Key not found")

    elif choice == 4:
        print("Add A Setting")
        add_key = input("Enter a key to add:")
        new_value = input("Enter new value:")
        robot[add_key] = new_value
        print("Key has been added")

    elif choice == 5:
        print("Exiting Menu")
        break
    else:
        print("Invalid option. Please choose between 1-5")
