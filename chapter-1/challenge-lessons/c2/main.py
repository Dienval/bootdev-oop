class Employee:
    company_name = "Age of Dragons, Inc."
    total_employees = 0

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1
        
        print(f"Adding new employee - new total employees: {Employee.total_employees}")

    def get_name(self):
        self.full_name = f"{self.first_name}" + " " + f"{self.last_name}"
        print(f"New employee name: {self.full_name}")
        return self.full_name
