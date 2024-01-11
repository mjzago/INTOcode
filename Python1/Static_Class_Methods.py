# Class and Static Methods
# Class methods are bound to the class and can access class-level attributes, while static methods are independent of the class and do not require access to class-level attributes


# Class Method:
class Calculator:
    PI = 3.14159  # Class-level attribute

    @classmethod
    def add_pi(self, number):
        return number + self.PI

    @classmethod
    def multiply_pi(self, number):
        return number * self.PI


# Using the class method
result_add = Calculator.add_pi(5)
result_multiply = Calculator.multiply_pi(10)

print(result_add)  # Output: 8.14159 (5 + 3.14159)
print(result_multiply)  # Output: 31.4159 (10 * 3.14159)


# Static Method:
class Calculator:
    @staticmethod
    def square(number):
        return number ** 2

    @staticmethod
    def cube(number):
        return number ** 3


# Using the static method
result_square = Calculator.square(4)
result_cube = Calculator.cube(3)

print(result_square)  # Output: 16 (4 squared)
print(result_cube)    # Output: 27 (3 cubed)





# Aufgabe 1: Class and Static Methods
# In this assignment, you will create a class TemperatureConverter with two static methods celsius_to_fahrenheit and fahrenheit_to_celsius to convert temperatures between Celsius and Fahrenheit.

# Instructions:

# Create a class TemperatureConverter.
# Implement the static methods celsius_to_fahrenheit(cls, celsius) and fahrenheit_to_celsius(cls, fahrenheit).
# The celsius_to_fahrenheit method should convert a temperature from Celsius to Fahrenheit using the formula (C * 9/5) + 32.
# The fahrenheit_to_celsius method should convert a temperature from Fahrenheit to Celsius using the formula (F - 32) * 5/9