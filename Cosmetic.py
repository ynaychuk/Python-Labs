class Cosmetic:
    name = "Cream"
    cost, weight, expiration_date, quantity = 00.00, 00, 00.0000, 00
    total_quantity = 0

    def __init__(self, name="cream", cost=00.00, weight=0, expiration_date=00.0000, quantity=00):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.expiration_date = expiration_date
        self.quantity = quantity
        Cosmetic.total_quantity += self.quantity

    def to_string(self):
        print("Name: " + self.name + ", cost:" + str(self.cost)
              + ", weight" + str(self.weight) + ", expiration date"
              + str(self.expiration_date) + ", quantity" + str(self.quantity))

    def print_sum(self):
            print("A cosmetic called" + self.name + " has quantity" + str(self.quantity))

    @staticmethod
    def print_static_sum():
        print("Total quantity for all cosmetics = " + str(Cosmetic.total_quantity))

if  __name__ == "__main__":
    cream = Cosmetic()
    pomade = Cosmetic("Pomade", 15.25, 20, 10.2021, 80)
    hair_dye = Cosmetic("Hair dye", 63.50, 250, 07.2025, 75)
    cream.to_string()
    pomade.to_string()
    hair_dye.to_string()
    Cosmetic.print_static_sum()
    pomade.print_sum()
    hair_dye.print_sum()