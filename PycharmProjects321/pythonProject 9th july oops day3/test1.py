class car :

    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre


    def milage(self):
        print("this is milage of car")

c = car("solid","v6","radial")
print(c)

class tata(car):
    pass

t= tata("solid1", "v8","radial1" )
print(t)
print(t.milage())

# so now there is no error as we have provided the required argument.
# so in case of inheritence operation it will behave in the same way as in parent class