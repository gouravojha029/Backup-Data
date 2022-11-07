# multiple inheritence
# note- there is a difference b/w multi level and multiple inheritence
class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show you account open status")
    def deposite(self):
        print("this will show your deposited amount")


class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icici through hdfc")

class icici(bank,HDFC_bank):
    pass

i = icici()
i.transaction()
i.hdfc_to_icici()
i.account_opening()
i.deposite()
