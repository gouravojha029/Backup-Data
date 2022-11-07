class person :

    def __init__(sudh,name,surname,emailid,year_of_birth):
        sudh.name1 = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def age(sudh , current_year):
        return current_year - sudh.year_of_birth


anuj_var = person("anuj", "bhandari", "anuj@gmail.com", 1994)
sudh = person("sudhanshu ", "kumar", "sudhanshu@gmail.com", 23424)
gargi = person("gargi", "xyz", "gargi@gmail.com", 234242)
print(sudh.age(2022))
print(anuj_var.age(2022))