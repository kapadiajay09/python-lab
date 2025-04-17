def convert_length():
    conversions = [
        ("inches", 12),
        ("yards", 1/3),
        ("miles", 1/5280),
        ("millimeters", 304.8),
        ("centimeters", 30.48),
        ("meters", 0.3048),
        ("kilometers", 0.0003048)
    ]
    
    feet = input("Enter the length in feet: ")
    feet = int(feet)

    print("Choose a conversion operation:")
    for i, (unit, _) in enumerate(conversions, start=1):
        print(f"{i}. Convert to {unit}")

    choice = input("Enter the number of your choice: ")
    choice = int(choice)

    unit, factor = conversions[choice - 1]
    result = feet * factor
    print(f"{feet} feet is equal to {result} {unit}.")
    
convert_length()



