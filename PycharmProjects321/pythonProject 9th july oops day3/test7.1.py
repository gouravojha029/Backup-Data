#polymorphism
# here i have created two different classes
class ineuron:
    def students(self):
        print("print a students details ")

class class_type:
    def students(self):
        print("print the class type of students")

# now creating another funct(method) outside of classes which is not related to above classes
def ineuron_external(a):
    a.students()
i = ineuron()# object for class
j = class_type()# object for class
ineuron_external(i)
ineuron_external(j)

# so in the above we can see one single funct able to handle object(i and j) or class ineuron and class
# class_type which is printing different value for same funct.

# task
# for all the concepts that we have discussed in our class point by point you have to write atleast 10 eg.
# you have to make sure that use ineuron students, class type, number of courses, affiliates, blog, internship,
# job as a reference example.
