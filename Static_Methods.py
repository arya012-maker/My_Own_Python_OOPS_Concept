## what is Static methods in Python?
## Proper Defination - A static method is a method in a class that does not depend on an instance (object) of the class. 
                       # It belongs to the class itself and can be called without creating an object.

# In simple terms, a static method in Python is a method that knows nothing about the class or instance

## In Simple Terms - 
## Imagine a box full of toys.Sometimes you have specia instructions  that doesnt need to know which is inside the box --- its just works on its own.
## So, static methods are like that. They dont need to know about the class or instance.
## SO in Python Static methods are special instructions . Its live inside the BOX(CLASS) but doesnt care about the indiviual toys(objects).

# Example:

class Maths_help:
    @staticmethod ##--> here we use static method decoartor to define the static method.
    def add(x, y):
        return x + y

result = Maths_help.add(5, 10) #--> # We call the add() method on the class itself, not on an object.
print(result)       # Output: 15


## key points:
# 1. Static methods are defined using the @staticmethod decorator.
# 2.  No Special "Toy" Needed: Unlike regular methods that need a toy (or object) to work on, 
# 3.  A static method works without knowing anything about a specific toy.
# 4.  Helper Function: It’s like a helper that just does its job without looking at the rest of the toys.
# 5.  Static methods can be called on the class itself without creating an object.

