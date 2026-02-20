class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object
x = Person("John", "Doe")
x.printname()


# Create a Child Class
class Student(Person):
    pass

# Use the Student class
x = Student("Mike", "Olsen")
x.printname()


# Add the __init__() Function (overriding parent)
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

