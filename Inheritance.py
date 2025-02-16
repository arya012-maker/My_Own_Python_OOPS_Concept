# # //Defination//
# Like children inherit properties from their parents 
# its same like that 
# we make classes to inherit properties from other classes and we can also overwrite them according to Us
class Animal:
    def __init__(self , name , voice):
        self.name = name
        self.voice = voice
    
    def sound(self):
        print(f"{self.name} sounds like {self.voice}")

class Dog(Animal):
    def __init__(self , name):
        super().__init__(name , "bark")
        


class Cat(Animal):
    def __init__(self , name):
        super().__init__(name , "Meow")

my_dog = Dog("Aryamann")
my_dog.sound()

my_cat = Cat("Ashika")
my_cat.sound()

# Explantion - 

# now here the person or the animals are inherting the properties of class animal from the base class 
# and these tow are children (DOG AND CAT)

# and so basically we are using the super() keyword to call the constructor of the parents class or the base class here that is Animal.
# It is used to access the attirbuts and methods of the base class thats why we are able to call the innit method and the sound method too.





