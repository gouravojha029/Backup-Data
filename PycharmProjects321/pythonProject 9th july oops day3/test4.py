# method overridding

class ineuron:
    def student(self):
        print("print the details of all the students")
    def achivers(self):
        print("print the list of all the achivers")
    def hall_of_fame(self):
        print("print everyone from hall of fame")

class ineuron_vision(ineuron):
    # here i am redefining the student funct(method) in present in class ineuron
    def student(self):
        print("these are the filters student list")

iv = ineuron_vision()
iv.student()

# so in the above we can see that i have redefine the student method and in console it will  print that one
