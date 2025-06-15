def weight_converter():
    # Conversion to kg from each unit
    to_kg = {
        "pg": 1e-12,
        "ng": 1e-9,
        "ug": 1e-6,
        "mg": 1e-3,
        "g": 1e-3,
        "kg": 1,
        "t": 1e3
    }

    # Conversion from kg to each unit
    from_kg = {
        "pg": 1e12,
        "ng": 1e9,
        "ug": 1e6,
        "mg": 1e3,
        "g": 1e3,
        "kg": 1,
        "t": 1e-3
    }

    while True:
        # Step 1: Get the weight
        weight_input = input("Enter weight (or type 'quit' to exit): ").strip()
        if weight_input.lower() == "quit":
            print("Exiting weight converter")
            break

        try:
            weight = float(weight_input)
            if weight <= 0:
                print("Weight must be a positive number.")
                continue
        except ValueError:
            print("Invalid weight. Please enter a number.")
            continue

        # Step 2: Get the user_input unit
        user_input_unit = input("Enter the unit you're converting **from** (pg, ng, ug, mg, g, kg, t): ").strip().lower()
        if user_input_unit not in to_kg:
            print("Invalid user_input unit.")
            continue

        # Step 3: Get the converter unit
        converter_unit = input("Enter the unit you're converting **to** (pg, ng, ug, mg, g, kg, t): ").strip().lower()
        if converter_unit not in from_kg:
            print("Invalid converter unit.")
            continue

        # Step 4: Convert user_input to kg, then to converter
        weight_in_kg = weight * to_kg[user_input_unit]
        converted_weight = weight_in_kg * from_kg[converter_unit]

        # Step 5: Display result
        print(f"{weight} {user_input_unit} = {converted_weight} {converter_unit}\n")

# Run the converter
weight_converter()
