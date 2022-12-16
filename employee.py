class Employee():

    def __init__(self, first_name, last_name, anual_salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.anual_salary = anual_salary

    def give_raise(self, add=5000):
        self.anual_salary += add
        return self.anual_salary
