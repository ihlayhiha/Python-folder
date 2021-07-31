# a = 12
# b = 20
# print(a + b)
# print(a.__add__(b))
# print( 1 +  2)
# print( a.__add__(100))


class Kettle(object):       # class is basically a template for creating objects

    power_source = "electricity"    # adding a class attribute that every instance of the class will share

    def __init__(self, make, price):    # called the constructor. Provides default values when instances are created later.
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# object is an instance of a class
# objects created using the same class will have the same characteristics
# instantiate is the term used to define creating an instance of a class
# method is a function that's bound to an instance of a class
# method is a function  defined in a class
# attribute is a variable bound to a variable in the class

kenwood = Kettle("Kenwood", 9.88)       # creating an instance/object of the Kettle class
print(kenwood.price)
print(kenwood.make)
kenwood.price = 14.99
print(kenwood.price)

hamilton = Kettle("Hamilton", 10.55)    # creating another instance/object of the Kettle class
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# when a  variable is bound to an instance of a class, it's referred to as a data attribute or fields, data members etc

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)      # checking the attribute of kenwood
hamilton.switch_on()    # using an instance of Kettle to call  a method. Doesn't need to mention 'self' parameter
print(hamilton.on)

print()
Kettle.switch_on(kenwood)   # using the class(Kettle) to call a method. So it requires u to specify the  instance.
print(kenwood.on)


print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)   # we haven't added power attribute to hamilton instance. It shows error

print("Switch class to Atomic Power")
Kettle.power_source = "Atomic"
print(Kettle.power_source)
print("Switch Kenwood to Gas")
kenwood.power_source = 'Gas'    # adds a new local attribute for kenwood
print(kenwood.power_source)     # checks for attribute of this instance. If it doesn't find any, it checks for the attribute in this class.
print(hamilton.power_source)

print("*" * 80)
print(Kettle.__dict__)      # accessing the namespace and their attributes via the __dict__
print(kenwood.__dict__)
print(hamilton.__dict__)
