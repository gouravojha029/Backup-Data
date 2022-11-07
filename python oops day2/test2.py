class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

obj = person()
print(obj)

class employee(person):
    pass

obj1 = employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)

