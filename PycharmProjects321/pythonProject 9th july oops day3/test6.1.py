#encpasulation
class ineuron:
    def __init__(self):
        self.students1 = "data science"

    def students(self):
        print(self.students1)

# i is the variable(method) of class
i= ineuron()
i.students()
# here i am calling same class variable via a object, because via object i will able to print variable as
# well as funct
i.students1 = "data analytics"
i.students()# again i am calling the funct
# this time "data analytics" will be printed, i am trying to over write a value of variable in run time.


class ineuron1:
    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)
i1 = ineuron1()
i1.students()
# here i am trying the same obove operation on private data
i1.__students1 = "big data"
i1.students()
# this time the change has not taken place although error is also not there
# lets try to change the private value on run time in another file