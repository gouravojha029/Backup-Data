# data abstraction or hiding operation
class ineuron:
    __students = "data science"

    def students(self):
        print("print the class of students",ineuron.__students)

i = ineuron()
i.students()
# now i am trying to accesess the __students(variable)directly present  inside class ineuron,but i will not
# be able to access it.
i.__students()
# to access it i have to go via class