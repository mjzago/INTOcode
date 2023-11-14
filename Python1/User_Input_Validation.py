def get_valid_input(user_input):
    value = input(user_input)
    return value


if __name__ == "__main__":
    print("Enter two numbers to calculate their average.")
    num1 = get_valid_input("Enter the first number: ")
    num2 = get_valid_input("Enter the second number: ")

    try:
        average = (num1 + num2) / 2
        print(f"The average of {num1} and {num2} is: {average}")
    except ZeroDivisionError:
        print("Error: The second number cannot be zero. Please enter a non-zero value for the second number.")

# Aufgabe
# Modify the function get_valid_input() to handle and raise exceptions for incorrect input, such as strings, characters, or any unexpected errors. Once you've made the necessary changes, run the program to calculate the average of two numbers provided by the user, ensuring that the program does not crash even with invalid inputs, and displaying meaningful error messages for the user to correct their input.
