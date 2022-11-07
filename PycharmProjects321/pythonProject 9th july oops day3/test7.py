# polymorphism
def test(a,b):
    return a+b
print(test(3,4))
print(test("sudhanshu ", "kumar"))
# as we can see when value given is int type it is performing addition operation and when value is str type
# it is performing concatenation operation. so funct is same but behaving differently in different situation
# with different data.
# this phenomenon of one object with different behaviour is called polymorphism.