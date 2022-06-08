from abc import ABC, abstractmethod


class Geometry(ABC):
    """Abstract class (Blueprint) for 4 sided Geometry"""

    def __init__(self, name: str, length: float, breadth: float):
        """Abstract class for 4 Sided Geometry

        Args:
            name (str): Name of the shape
            length (float): Length of the shape
            breadth (float): Breadth of the shape
        """
        self.name = name
        self.length = length
        self.breadth = breadth

    @property
    def describe(self):
        """Describes the geometry

        Returns:
            str: information
        """
        return f"Geometry is {self.name} with length {self.length} and breadth {self.breadth}."

    @abstractmethod
    def area(self):
        """Return area of the geometry"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of the geometry"""
        pass


class Rectangle(Geometry):
    """Rectangle Geometry Class"""

    def __init__(self, length, breadth):
        """Initiate rectangle shape

        Args:
            length (float): length of the rectangle
            breadth (float): breadth of the rectangle
        """
        super().__init__("rectangle", length, breadth)

    def area(self):
        print(f"area of {self.name} is {self.length*self.breadth}")

    def perimeter(self):
        print(f"perimeter of {self.name} is {self.length * 2+self.breadth*2}")


class Square(Geometry):
    """Square Geometry Class"""

    def __init__(self, length):
        """Initiate square shape

        Args:
            length (float): length of square
        """
        super().__init__("square", length, length)

    def area(self):
        print(f"area of {self.name} is {self.length**2}")

    def perimeter(self):
        print(f"perimeter of {self.name} is {self.length * 4}")
