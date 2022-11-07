# multi level inheritence
class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show you account open status")
    def deposite(self):
        print("this will show your deposited amount")


class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icici through hdfc")

class icici(HDFC_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.deposite()
i.transaction()
i.account_opening()

# as we can see all four method (three in claas bank and one in HDFC_bank) are avaiable in class icici, we
# are able to perform multi level inheritence.