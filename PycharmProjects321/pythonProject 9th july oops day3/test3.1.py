class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show you account open status")
    def deposite(self):
        print("this will show your deposited amount")
    def test(self):
        print("this is a test form of bank class")


class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icici through hdfc")
    def test(self):
        print("this is a test form of hdfc_bank class")

class ineuron_bank:
    def account_status_icici(self):
        print("print a account status in icici")

class icici(bank,HDFC_bank,ineuron_bank):
    pass

i = icici()
i.transaction()
i.hdfc_to_icici()
i.account_opening()
i.deposite()
i.test()
i.account_status_icici()

# so in the line 8 and in line 15 both are having funct with same variable so the funct which will print
# in console will depend upon position of class iheritred(as in class icici bank is at first and hdfc_bank
# is at second therefore priorty is given to funct(test) of class bank as it is a first positon).
# if order is reversed then priority will also reversed.
# we can inherit any number of classes .