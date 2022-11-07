# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test1():
    print("this is first time i am using pycharm")

def genfib(n):
    a=1
    b=1
    l=[]
    for i in range(n):
        l.append(a)
        a,b=b,a+b
    return l

test1()
a=genfib(10)
print(a)
print()

