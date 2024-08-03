def get_number(prompt):
    while True:
        try:
            # Prompt the user for input and try to convert it to a float
            return float(input(prompt))
        except ValueError:
            # Handle the case where the input is not a number
            print("Invalid input. Please enter a valid number.")

def divide_numbers():
    while True:
        try:
            # Get the two numbers from the user
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            # Perform the division
            result = num1 / num2
            
            # Display the result
            print(f"The result of dividing {num1} by {num2} is {result}")
            break
        except ZeroDivisionError:
            # Handle division by zero error
            print("Error: Cannot divide by zero. Please try again.")

# Run the division function
divide_numbers()