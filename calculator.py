class Calculator:
    """
    A professional calculator class that handles basic arithmetic 
    operations with error validation.
    """

    def add(self, x: float, y: float) -> float:
        """Returns the sum of two numbers."""
        return float(x + y)

    def subtract(self, x: float, y: float) -> float:
        """Returns the difference of two numbers."""
        return float(x - y)

    def multiply(self, x: float, y: float) -> float:
        """Returns the product of two numbers."""
        return float(x * y)

    def divide(self, x: float, y: float) -> float:
        """
        Returns the division result of two numbers.
        Raises ValueError if division by zero is attempted.
        """
        if y == 0:
            raise ValueError("Mathematical Error: Division by zero is not allowed.")
        return float(x / y)

# Tijaabada Professional-ka ah (Example Usage)
if __name__ == "__main__":
    calc = Calculator()
    
    try:
        print(f"Addition: {calc.add(10, 5)}")
        print(f"Division: {calc.divide(10, 2)}")
        # Tijaabinta khalad-qabashada
        print(calc.divide(10, 0))
    except ValueError as e:
        print(e)
