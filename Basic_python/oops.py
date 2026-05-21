class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.id}")

    
class manager(employee):
    def __init__(self, name , id , department):
        self.department = department
        super().__init__(name, id)

    def display(self):
        super().display()
        print(f"Department: {self.department}")

emp1=manager("John Doe", 12345, "Sales")
emp1.display()
