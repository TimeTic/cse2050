#Inheritance allows us to define child classes that inherit attributes and methods forom a parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        """Prints the name of an animal."""
        print("My name is {}".format(self.name))
    
class Dog(Animal):
    def __inint__(self, name, fur_colors):
        super().__init__(name)  # Calling the constructor of the parent class
        self.fur_colors = fur_colors
        
        def bark(self):
        print("Woof")

    def print_name(self):
        print(f"Hi, I'm{self.name} and I'm a dog")
    
    def printer(ab):
        obj.print_name()

    class Cat(Animal):
        def meow(self):
            print("Meow")

# Creating objects from each class
if __name__ == "__main__":
    tim = Animal('Tim')
    my_dog = Dog("Bobby", ["brown"])
    # my_cat = my_dog.Cat("Whiskers", ["black"])
    my_dog.print_name()   # Outputs: My name is Bobby
    # my_dog.bark()        # Outputs: Woof
    # my_cat.meow()        # Outputs: Meow

    print(tim)
    print(my_dog)


    #-----------------------------------------------------------------------
    

#Polymorphism
    "describe patterns where object share a method name, but have diff implementations for that mehtod"

# Inheritance is one way to achieve this
    
#Pythin has a built-in (parametritc) polymorphism, basesd on the idead of duck typing

#---------------------------------------
    
#Composition
    """Another common OOP pattern.
    the pattern where a class stores an istance of another class
    Composition refers to a "has a" relationship

    """

#
    
def EvenList(sefl):
    self.list=[]
    def add(self,x):
        if x%2==0:
            self.list.append(x)
            def remove(self,x):
        