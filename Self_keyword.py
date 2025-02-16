class Car :
    def __init__(self , name , brand):
        self.name = name
        self.brand = brand

my_car = Car("grand Vitara" , "maruti")
print(my_car)


# if we print my_car directly it will give us a whole object rather than the brand and name 
# but if we print like "my_car.brand" or "my_car.name"
# then it will give us resul maruti or grand vitara because we are using the self keyword that act like a wirinf between the two 
# keywords and help us to connect with them like telephinic wire like yes we are refering this paticular 
# keyword with that paticular argument 