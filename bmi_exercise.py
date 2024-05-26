def comparare(ob1, ob2):
    if ob1.Bmi() > ob2.Bmi():
        print(ob1.nume)
    elif ob1.Bmi() < ob2.Bmi():
        print(ob2.nume)
    else:
        print("Persoanele au acelasi BMI")


class Person():
    def __init__(self, nume, varsta, greutate, inaltime):
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
        self.inaltime = inaltime


    def __repr__(self):
        return "(" + self.nume + str(self.varsta) + str(self.greutate) + str(self.inaltime) + ")"


    def Bmi(self):
        bmi = self.greutate / (self.inaltime * self.inaltime)
        return bmi

    def __gt__(self,other):
        if self.Bmi()>other.Bmi():
            return True
        else:
            return False

if __name__ == "__main__":
    ob1 = Person("Cezar", 28, 85, 179)
    ob2 = Person("Carol", 29, 99, 184)
    print(ob1.Bmi())
    print(ob2.Bmi())
    # obiect.nume  obiect.metoda()  obiect.get_nume()

    comparare(ob1, ob2)
    print(ob1>ob2)