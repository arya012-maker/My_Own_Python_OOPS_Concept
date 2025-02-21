## in simple terms same function name with different Behaviour or working.


class Cat:
    def sound(self):
        print("Meow Meow")

class Dog:
    def sound(self):
        print("Bark Bark")

def make_sound(animal):        #-->     # We don't care what type of animal it is,
                                        # we just call its sound() method.
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)      # Output: Bark Bark
make_sound(cat)      # Output: Meow Meow


# In the above example, we have two classes Cat and Dog with the same method name sound().
# The function make_sound() takes an object of any class and calls its sound() method.
# This is called Polymorphism. It allows us to perform a single action in different ways.

# Polymorphism is a key concept in OOP. It allows objects of different classes to be treated as objects of a common superclass.
# So like now we call the both function with the same name but output is different as different class has different behaviour.



