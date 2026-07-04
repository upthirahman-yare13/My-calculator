import logging

# Habeynta Logging-ka si aad ula socoto xisaabta
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Calculator:
    """Class-ka xisaabinta ee xirfadda leh."""

    def _validate(self, x, y):
        """Hubinta in x iyo y ay yihiin tirooyin sax ah."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            logger.error(f"Invalid input provided: {x}, {y}")
            raise TypeError("Fadlan geli tirooyin sax ah (int ama float).")

    def add(self, x: float, y: float) -> float:
        self._validate(x, y)
        result = float(x + y)
        logger.info(f"Operation: {x} + {y} = {result}")
        return result

    def subtract(self, x: float, y: float) -> float:
        self._validate(x, y)
        result = float(x - y)
        logger.info(f"Operation: {x} - {y} = {result}")
        return result

    def multiply(self, x: float, y: float) -> float:
        self._validate(x, y)
        result = float(x * y)
        logger.info(f"Operation: {x} * {y} = {result}")
        return result

    def divide(self, x: float, y: float) -> float:
        self._validate(x, y)
        if y == 0:
            logger.warning("Attempted division by zero.")
            raise ValueError("Khalad: Qaybinta eber ma suurtowdo.")
        result = float(x / y)
        logger.info(f"Operation: {x} / {y} = {result}")
        return result
