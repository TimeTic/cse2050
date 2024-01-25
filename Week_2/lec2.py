 
# Example codes for implementing CLASSES

class Student:
    def __init__(self, name, age, graduating_class, courses=()):
        self.name = name
        self.age = age
        self.graduating_class = graduating_class
        self._courses = [i for i in courses]

def __str__(self):
    return f"student: {self.name} (Class of {self.graduating_class})"

tim  = Student("Z", 19, 2027, ["CSE 2050", "CALC 1" "Public Policy", "English"])
print(tim)


#----------------------------
#-----thunder eidtion------
# def __add__(self, other):
#   new_x = self.x + other.x
# new_y = slef.y + other.y
#return Vector(new_x, new_Y)
# to define other functions

#--------------------

# There are 4 fundemnetal patterns
# Abstraction >>>>  
# encapsulation, 
#inhertince, 