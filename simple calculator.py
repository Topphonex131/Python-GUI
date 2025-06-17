# Define a function named calculator to hold the main loop logic
def calculator():
    # Start an infinite loop so the calculator keeps running until the user quits
    while True:
        # Ask the user to enter the first number or type 'quit' to exit
        user_input = input("Enter your first number (or type 'q' to exit): ")
        
        # Check if the user wants to quit the calculator
        if user_input.lower() == "q":
            # If yes, print an exit message
            print("Exiting calculator.")
            # Exit the while loop to stop the program
            break

        # Use try-except to catch any errors from converting input to float
        try:
            # Convert the first input to a float number
            num1 = float(user_input)
            # Ask the user to enter the second number and convert it to float
            num2 = float(input("Enter second number: "))
            # Ask the user to choose an operator for the calculation
            operator = input("Enter the operator (+, -, *, /): ")

            # If the operator is '+', add the two numbers and print the result
            if operator == "+":
                print(f"Result: {num1 + num2}")
            # If the operator is '-', subtract the second number from the first and print the result
            elif operator == "-":
                print(f"Result: {num1 - num2}")
            # If the operator is '*', multiply the two numbers and print the result
            elif operator == "*":
                print(f"Result: {num1 * num2}")
            # If the operator is '/', check for division by zero
            elif operator == "/":
                # Division by zero is not allowed, so handle that case
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    # If safe, divide the first number by the second and print the result
                    print(f"Result: {num1 / num2}")
            else:
                # If the user entered an invalid operator, notify them
                print("Invalid operator. Try again.")
        except ValueError:
            # If converting input to float fails, show an error message
            print("Invalid input. Please enter numbers.")

# Call the calculator function to run the program
calculator()
