class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_annual_salary(self):
        annual_salary = self.salary * 12
        return annual_salary

    def raise_salary(self, salary_raise):
        self.salary += salary_raise
        return self.salary