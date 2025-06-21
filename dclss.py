
# Importing dataclass to simplify class creation
from dataclasses import dataclass
# Importing ClassVar to define class-level (static) variables
from typing import ClassVar

# Define a data class named Pakistani
@dataclass
class Pakistani:
    # Instance variables (each object will have its own values so we dont have to writee __init__by using dataclass)
    name: str
    age: int
    weight: float
    liked_food:str
    # Class variable (shared among all instances, not passed to constructor)
    national_food:ClassVar[str]="Biryani"
    national_language: ClassVar[str] = "Urdu"

    # Instance method: operates on individual object (needs 'self')
    def info(self):
        return f"A citizen{self.name} having age {self.age} years have {self.weight} kg likes {Pakistani.national_food}"
    def eat(self):
        return f"{self.name} is eating {self.liked_food}"

    # Instance method: accessing class variable using class name
    def speak(self):
        return f"{self.name} is speaking {Pakistani.national_language}"
#to use static variable we use class name as we defined it as language variable in line 9
# as static variable is shared by all instances of the class and not need to be defined below 
# @staticmethod
# def language():
#         return "English"


    # Static method: does not access 'self' or 'cls'; independent of any instance
    @staticmethod
    def country_language():
        return Pakistani.national_language

    def __call__(self):
        print (f"if dont want to write print(ali()) u can write print not return while calling instance ")
        return f"Hello ur instance/object is called"



# Creating an instance (object) of Pakistani class
ali = Pakistani("Mustafa", 20, 35,"Pizza")

# Printing the instance using auto-generated __repr__ method from @dataclass
print(ali.name)
# Calling static method using class name to get country language
print(ali.age)
print(ali.weight)
print(Pakistani.national_language)
print(ali) 


# Calling instance method 'eat' on ali
print(ali.eat())  # Output: Ali is eating
print(ali.info())

# Calling instance method 'speak' on ali, which uses the static 'language' variable
print(ali.speak())  # Output: Ali is speaking Urdu

print(Pakistani.country_language())  # Output: Urdu

#if want to make the instance of class pakistani callable we write __call__ function
print(ali())