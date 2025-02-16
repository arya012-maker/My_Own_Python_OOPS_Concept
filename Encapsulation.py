# Alright! Imagine you have a toy car. 
# You love playing with it, but inside the car, there are tiny parts like an engine and wires that make it move.
#  You don’t need to open the car and touch those parts—you just press a button to make it go!

class Toy:
    def __init__(self):
        self.__engine = "vrom vrom !!!!"  # <-- you seeing self.__engine(this is a private method that we cannot access it deirectly)(Its is become hidden or private)
        

    def press_button(self):
        return self.__engine # <-- now here we are accessing that hiden method and we are withut showing whats actually in that method exactly 

car = Toy()
print(car.press_button())
print(car.__engine)


# More Explantion-
# Now so here to make anything private we use ".__" this makes our method private and we cannot access it directly.
# 
# Here, __engine is hidden inside the class, and you can only use it through press_button(). 
# That’s encapsulation!
# 
