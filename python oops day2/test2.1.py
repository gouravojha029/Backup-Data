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
print(obj1._person__surname)

# as we can see the difference yob and _name (public and protected) both are printing with new data but the
# private has not changed it is taking data from person class only.
# because private variable is associated with with particular classes.