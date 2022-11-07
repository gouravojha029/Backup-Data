class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

obj = person()
print(obj)

class employee(person):
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1992


obj1 = employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._employee__surname)

# because private variable is associated with with particular classes.
# therefore changing the class name in print will bring the change and you  will see in console