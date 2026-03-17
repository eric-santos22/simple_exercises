from datetime import date, datetime

class Person:

    def __init__(self, name: str, country: str, birthdate: date):
        self.name:str = name
        self.country:str = country
        self.birthdate:date = birthdate

    def get_person_age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if today < date(today.year, self.birthdate.month, self.birthdate.day):
            age -=1        
        return age

    def plot_info(self):
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Birthdate: {self.birthdate}")
        print(f"Age: {self.get_person_age}")

if __name__ == "__main__":

    eu = Person("Eric Santos", "Brasil",date(2004,10,30))
    eu.plot_info()