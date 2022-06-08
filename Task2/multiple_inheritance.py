class Addition:
    """Addition"""

    def add(self, a, b):
        """add two numbers"""
        return a + b


class Subtraction:
    """Subtraction"""

    def subtract(self, a, b):
        """subtract two numbers"""
        return a - b


class Multiplication:
    """Multiplication"""

    def multiply(self, a, b):
        """multiply two numbers"""
        return a * b


class Division:
    """Division"""

    def divide(self, a, b):
        """divide two numbers"""
        return a / b


class Calc(Addition, Subtraction, Multiplication, Division):
    """Derived class"""

    pass


c = Calc()
print(f"Addition: {c.add(5, 6):.2f}")  # Addition: 11.00
print(f"Subtraction: {c.subtract(5, 6):.2f}")  # Subtraction: -1.00
print(f"Multiplication: {c.multiply(5, 6):.2f}")  # Multiplication: 30.00
print(f"Division: {c.divide(5, 6):.2f}")  # Division: 0.83
