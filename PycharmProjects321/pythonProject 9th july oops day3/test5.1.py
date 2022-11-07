# abstraction
class ineuron:
    __students = "data science"

    def students(self):
        print("print the class of students",ineuron.__students)

i = ineuron()
i.students()
i._ineuron__students

# we cannot access the variable of class directly, to do that we have to do by or via class it seems like
# data("data science)is hiden behind class and this is something called data abstraction.