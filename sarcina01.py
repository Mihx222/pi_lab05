class BankAccount:
    def __init__(self, name="Dupont", balance=1000):
        self.name = name
        self.balance = balance

    def depozit(self, suma):
        self.balance += suma

    def retragerea(self, suma):
        if self.balance <= suma:
            self.balance = 0
        else:
            self.balance -= suma

    def sold(self):
        print(self.name + " - " + str(self.balance) + " lei")


account1 = BankAccount()
account1.sold()
account2 = BankAccount("Mihai", 1000000)
account2.sold()
account2.depozit(1000000)
account2.retragerea(500000)
account2.sold()
