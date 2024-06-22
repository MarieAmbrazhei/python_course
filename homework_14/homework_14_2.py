"""Homework_14_2: Writing and implementing programs."""

# Инженерный калькулятор

from decimal import Decimal, InvalidOperation


class SimpleCalculator:
    """ This class to represent a calculator."""

    def __init__(self):
        """Initialize the calculator with a menu number attribute."""
        self.menu_number = None

    def get_menu_number(self):
        """Prompt the user to select a menu number for
        the desired operation."""
        while True:
            try:
                self.menu_number = int(
                    input('Enter menu number of operation:\n'
                          '1 for summary\n'
                          '2 for subtraction\n'
                          '3 for multiplication\n'
                          '4 for division\n'
                          '5 for exponentiation\n'
                          '6 to input a whole expression\n'))
                if 1 <= self.menu_number <= 6:
                    return self.menu_number
                print('You might choose only 1 to 6')
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 6.')

    def expression(self, input_expr):
        """Evaluate a mathematical expression given as a string."""
        input_expr = input_expr.replace(' ', '').replace('**', '^')
        if input_expr.isdigit():
            return float(input_expr)

        for c in ('+', '-', '*', '/', '^'):
            parts = input_expr.rpartition(c)
            if parts[1] == '*':
                return self.expression(parts[0]) * self.expression(parts[2])
            if parts[1] == '/':
                return self.expression(parts[0]) / self.expression(parts[2])
            if parts[1] == '+':
                return self.expression(parts[0]) + self.expression(parts[2])
            if parts[1] == '-':
                return self.expression(parts[0]) - self.expression(parts[2])
            if parts[1] == '^':
                return self.expression(parts[0]) ** self.expression(parts[2])
        return None

    @staticmethod
    def summary(a, b):
        """Return the sum of two numbers."""
        return f'{a} + {b} = {a + b}'

    @staticmethod
    def subtraction(a, b):
        """Return the difference of two numbers."""
        return f'{a} - {b} = {a - b}'

    @staticmethod
    def multiplication(a, b):
        """Return the product of two numbers."""
        return f'{a} * {b} = {a * b}'

    @staticmethod
    def division(a, b):
        """Return the quotient of two numbers, or an error message
        if dividing by zero."""
        if b != 0:
            return f'{a} / {b} = {a / b}'
        return 'Error! Division by zero!'

    @staticmethod
    def exponentiation(a, b):
        """Return the result of raising a number
         to the power of another number."""
        return f'{a} ^ {b} = {a ** b}'

    def calc(self):
        """Perform the calculation based on the selected menu number."""
        if self.menu_number == 6:
            input_expr = input('Enter your expression here: ')
            result = self.expression(input_expr)
            print('Answer is:', result)
            return result
        while True:
            try:
                a = Decimal(input('Enter your first number: '))
                b = Decimal(input('Enter your second number: '))
            except InvalidOperation:
                print('Please enter only numbers, thank you')
                continue

            if self.menu_number == 1:
                print(self.summary(a, b))
            elif self.menu_number == 2:
                print(self.subtraction(a, b))
            elif self.menu_number == 3:
                print(self.multiplication(a, b))
            elif self.menu_number == 4:
                print(self.division(a, b))
            elif self.menu_number == 5:
                print(self.exponentiation(a, b))
            else:
                print("Wrong!")
            break
        return None


calculator = SimpleCalculator()
calculator.get_menu_number()
calculator.calc()
assert calculator.summary(Decimal('3'), Decimal('2')) == '3 + 2 = 5'
assert calculator.subtraction(Decimal('5'), Decimal('2')) == '5 - 2 = 3'
assert calculator.multiplication(Decimal('3'), Decimal('2')) == '3 * 2 = 6'
assert calculator.division(Decimal('3'), Decimal('2')) == '3 / 2 = 1.5'
assert calculator.division(Decimal('5'),
                           Decimal('0')) == 'Error! Division by zero!'
assert calculator.exponentiation(Decimal('2'), Decimal('3')) == '2 ^ 3 = 8'
assert calculator.expression('10-3+1') == 8
assert calculator.expression('2**3 -1') == 7
