from abc import ABC, abstractmethod

# Abstract class representing a Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Concrete subclass Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Client code
if __name__ == "__main__":
    # Try to create an instance of the abstract class Shape (will raise an error)
    try:
        s = Shape()
    except TypeError as e:
        print(f"Error: {e}")
    
    # Create instances of concrete subclasses
    circle = Circle(5)
    square = Square(4)

    # Calculate and print the area and perimeter of each shape
    print("Circle:")
    print(f"Area: {circle.area()}")
    print(f"Perimeter: {circle.perimeter()}")

    print("\nSquare:")
    print(f"Area: {square.area()}")
    print(f"Perimeter: {square.perimeter()}")


# Aufgabe 1
# In this assignment, you will create an abstract class Database with abstract methods connect() and query(). The connect() method should represent connecting to a database, and the query() method should represent executing a query on the database.

# Next, create two concrete subclasses MySQLDatabase and PostgreSQLDatabase, each representing a specific type of database (MySQL and PostgreSQL). Implement the connect() and query() methods for each subclass to simulate connecting to the respective databases and executing queries.

# Finally, create instances of MySQLDatabase and PostgreSQLDatabase, and call their connect() and query() methods to ensure they work as expected.