# now i want to use the code that has been written in the file test1
import test1
print(test1)
# can you create a obj of class person1 here in test3 file
obj3 = test1.person1("sudhanshu", "kumar", 1994)
print(obj3.yob1)
# so click contrl button and hover your mouse on the class u will see a defenation and if click on the class u will
# directly reach there.
print(obj3._name1)
print(obj3._person1__surname1)

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
