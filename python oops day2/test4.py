# since there are multiple classes in test3 file and i want to use not  all the class but a particular
# one
from test3 import person


class person1 :
    def __init__(self, name, surname, yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

sudh = person1("sudhanshu", "kumar", "1990")
print(sudh._name1)
print(sudh._person1__surname1)