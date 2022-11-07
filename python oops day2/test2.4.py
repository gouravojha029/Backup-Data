class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self,current_year):
        return current_year - self.yob
    def __age1(self,current_year):
        return current_year - self.yob


obj = person()
print(obj._age(2022))
print(obj._person__age1(2022))

# now i will create another class and try to inherit the properties or funct from parent class that is person to child
# class employee.
class employee(person):
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991

obj1 = employee()
print(obj1._age(2022))
print(obj1._person__age1(2022))

# so we are able to call a function in same way we use to call class variable