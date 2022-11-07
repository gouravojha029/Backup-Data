price = int(input("enter the price"))
if price < 500:
    print("i will be able to by something")
    if price < 400:
        print("i will be able to buy a jacket")
    elif price < 300:
        print(" i will be able to buy a jacket")
        if price < 200:
            print("i wont like to do something")
    else:
        print("i wont be able to buy anything")
else:
    print("i wont be able to buy anything with this price tag")
if price > 500:
    print("lets try something else")