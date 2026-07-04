import logging

# Habeynta Logging-ka si aad ula socoto xisaabta
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Calculator:
    """
    Calculator Class Professional ah oo qabta hawlaha xisaabinta 
    iyo ilaalinta qaladaadka.
    """

    def _validate(self, x, y):
        """Hubinta in x iyo y ay yihiin tirooyin sax ah."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            logger.error(f"Invalid input: {x}, {y}")
            raise TypeError("Labada qiime waa inay noqdaan tirooyin (int ama float).")

    def add(self, x: float, y: float) -> float:
        """Returns the sum of two numbers."""
        self._validate(x, y)
        result = float(x + y)
        logger.info(f"Adding {x} + {y} = {result}")
        return result

    def subtract(self, x: float, y: float) -> float:
        """Returns the difference of two numbers."""
        self._validate(x, y)
        result = float(x - y)
        logger.info(f"Subtracting {x} - {y} = {result}")
        return result

    def multiply(self, x: float, y: float) -> float:
        """Returns the product of two numbers."""
        self._validate(x, y)
        result = float(x * y)
        logger.info(f"Multiplying {x} * {y} = {result}")
        return result

    def divide(self, x: float, y: float) -> float:
        """
        Returns the division result of two numbers.
        Raises ValueError if division by zero is attempted.
        """
        self._validate(x, y)
        if y == 0:
            logger.warning("Attempted division by zero.")
            raise ValueError("Mathematical Error: Division by zero is not allowed.")
        
        result = float(x / y)
        logger.info(f"Dividing {x} / {y} = {result}")
        return result

# Example Usage
if __name__ == "__main__":
    calc = Calculator()
    try:
        print(f"Result: {calc.add(10, 5)}")
        print(f"Result: {calc.divide(10, 2)}")
    except (ValueError, TypeError) as e:
        print(f"Khalad: {e}")
