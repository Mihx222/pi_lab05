class Car:
    def __init__(self, marca="Ford", culoarea="rosu"):
        self.marca = marca
        self.culoarea = culoarea
        self.sofer = "persoana"
        self.viteza = 0

    def alege_sofer(self, name):
        self.sofer = name

    def accelerare(self, rata, durata):
        if not self.sofer == "":
            self.viteza = rata * durata
        else:
            print("Accelerarea nu este posibila fara sofer!")

    def afiseaza_tot(self):
        print("Masina: " + self.marca + "\nCuloarea: " + self.culoarea +
              "\nNume sofer: " + self.sofer + "\nViteza: " + str(self.viteza) + " km/h")


defaultCar = Car()
defaultCar.afiseaza_tot()
print("")

newCar = Car("Mazda", "Alb")
newCar.alege_sofer("Mihai")
newCar.accelerare(1.5, 30)
newCar.afiseaza_tot()
