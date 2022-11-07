# encapsulation: means u are not allowing user to directly change the value of variable
class ineuron1:
    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)
    def students_change(self): # this is actually called setter funct which actually sets the value of variable
        # via funct.
        self.__students1 = "big data by me"


i1 = ineuron1()
i1.students()
i1.students_change() # here i am calling the funct for change
i1.students()

# so in case of private variable it is not going to change the value directly(with the help of object) but it
# will change the value with class method(funct).
# directly we cannot reassign the data for that we need to use class method.
# the above phenomenon is called encapsulation