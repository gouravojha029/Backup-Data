# inheritance
# when ever we want to re utilize the code from parent to child class inheritance comes into the pict.
class car :

    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre


    def milage(self):
        print("this is milage of car")


class tata(car):
    pass

t= tata()
print(t)


# we are getting the error because class tata(child) has inherited from class car(parent) and it is expecting
# some data from user as funct(__init__) has been used which take data from user.
