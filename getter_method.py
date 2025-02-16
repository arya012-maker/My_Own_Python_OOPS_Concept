# # We can access the private methods throught 
# Two ways by 
#            1-> the getter method with "get" keyword. 
#            2-> by using @property decorator to access the privaye method.


# We see how is it done by #            
# 1-> the getter method with "get" keyword. 

class Toy : 
    def __init__(self):
        self.__engine = "Vrom vrom!!!!"
    
    def get_engine_sound(self):
        return self.__engine

car = Toy()
print(car.get_engine_sound()) # Works fine! ✅

print(car.__engine) # # ERROR! ❌ You can't access directly

# Exlanation:
# Now you see the difference the method "  "get"_engine_sound  " this is getter method that allow us to access the private method.

# That is declared by the  ".__engine" keyword and thats why when we print the  "car.__engine" directly it will throw the error 
# as we cannot access it directlty its like you cannot see the engine but only hear the sound of the engine to to access the sound of the engine 
# we use getter method to access the Private thingss

# Explnation in Formal way :-
# __engine is private (hidden, like the car’s engine).
# get_engine_sound() is a getter method, which allows you to access the engine sound safely without modifying it directly.





# 2-> by using @property decorator to access the private method.

class Toy : 
    def __init__(self):
        self.__engine = "Vrom vrom!!!!"  # Hidden (private)
    

    @property
    def engine_sound(self):     # Getter method 
        return self.__engine    # Allows safe access

car = Toy()


print(car.engine_sound) # <-- now we are not calling this method because it is declared with the "@property Keyword".
# as it will directly call that method without implicitly call it manually by us.

print(car.__engine)  # <-- Now this will throw some error becasue we cannot access the Private method directly as it is protected.




