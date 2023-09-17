# classes

class Person:
    def __init__(self, username, clan):
        self.fullname = username
        self.clan = clan

    def getPerson(self):
        return self.fullname


person1 = Person("Wandera Moses", "Baise Mukose")
print(person1.getPerson())


class Child(Person):
    def __init__(self, username, clan, childname):
        super().__init__(username, clan)
        self.childname = childname
        self.kids = 0

    def getPerson(self):
        parent = super().getPerson()
        return f"Hello {self.childname} Your parent is {parent}"

    def getChildKids(self, kids):
        self.kids = kids
        return self.kids


child1 = Child("Wandera Moses", "Baise Mukose", "Wandera Rogers")
print(child1.getPerson())
print(child1.getChildKids(1))
