import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Joe', 'Silva', 23000)
        

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.anual_salary, 28000)

    def test_give_custom_raise(self):
        self.employee.give_raise(7000)
        self.assertEqual(self.employee.anual_salary, 30000)


unittest.main()
