class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self,current_year):
        return current_year - self.yob
    def __age(self,current_year):
        return current_year - self.yob


obj = person()
print(obj._age(2022))
print(obj._person__age(2022))

# so previously we were creating protected and private variables and now same for function and everything is same.

