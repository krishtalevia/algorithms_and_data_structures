class Calculator:

    def add(self, value_left, value_right) -> float:
        if not value_left == float and value_right == float: raise TypeError
        return value_left + value_right

    def subtract(self, value_left, value_right) -> float:
        return value_left - value_right

    def multiply(self, value_left, value_right) -> float:
        return value_left * value_right

    def divide(self, value_left, value_right) -> float:
        return value_left / value_right