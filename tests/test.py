import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def testing_adding_succsses(self):
        assert self.calc.add(self, 1, 1) == 2

    def testing_multiply_succsses(self):
        assert self.calc.multiply(self, 1, 2) == 2

    def testing_division_succsses(self):
        assert self.calc.division(self, 4, 2) == 2

    def testing_substraction_succsses(self):
        assert self.calc.substraction(self, 4, 2) == 2

    def testing_adding_unsuccsses(self):
        assert self.calc.add(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')