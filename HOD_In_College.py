

# Design a class Teacher with attributes name and subject. Create subclass HeadOfDepartment with additional responsibilities. 
# Implement methods to display details.

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class HeadOfDepartment(Teacher):
    def __init__(self, name, subject, responsibilities):
        super().__init__(name,subject)
        self.responsibilities = responsibilities  # List or string

    def display_details(self):
        print("TeacherName is:",self.name)
        print("Subject is:",self.subject)
        print("Responsibilities:",self.responsibilities)
HOD=HeadOfDepartment("Vishnu","Maths","Manage Department")
HOD.display_details()       

    
# Output:
# TeacherName is: Vishnu
# Subject is: Maths
# Responsibilities: Manage Department

    
    