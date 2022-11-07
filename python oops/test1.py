class person :

    def __init__(self,name,surname,emailid,year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var = person("anuj","bhandari","anuj@gmail.com",1994)
sudh = person("sudhanshu","kumar","sudhanshu@gmail.com",23424)
gargi = person("gargi","xyz","gargi@gmail.com",234242)
print(anuj_var.name)
print(sudh.name)
print(gargi.name)
print(type(sudh))