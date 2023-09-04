import random

class City:
    def __init__(self):
        self.name = "My City"
        self.money = 1000
        self.population = 10
        self.buildings = []

    def display_city_info(self):
        print(f"City: {self.name}")
        print(f"Money: ${self.money}")
        print(f"Population: {self.population}")
        print("Buildings:")
        for building in self.buildings:
            print(f"{building.name}: {building.count}")

    def build_building(self, building):
        if self.money >= building.cost:
            self.money -= building.cost
            self.buildings.append(building)
            print(f"Built {building.name}")
        else:
            print("Not enough money to build this building.")

class Building:
    def __init__(self, name, cost, income, capacity):
        self.name = name
        self.cost = cost
        self.income = income
        self.capacity = capacity
        self.count = 0

    def generate_income(self):
        return self.count * self.income

def main():
    my_city = City()

    # Define some buildings
    park = Building("Park", 100, 10, 50)
    apartment = Building("Apartment", 500, 50, 100)
    factory = Building("Factory", 1000, 100, 0)

    while True:
        my_city.display_city_info()

        # Display menu options
        print("\nMenu:")
        print("1. Build a Park")
        print("2. Build an Apartment")
        print("3. Build a Factory")
        print("4. End the Turn")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            my_city.build_building(park)
        elif choice == "2":
            my_city.build_building(apartment)
        elif choice == "3":
            my_city.build_building(factory)
        elif choice == "4":
            # Simulate a turn by generating income and updating population
            income = 0
            for building in my_city.buildings:
                income += building.generate_income()
            my_city.money += income
            my_city.population += random.randint(1, 5)
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
