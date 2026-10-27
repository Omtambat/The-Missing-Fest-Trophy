class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def collect(self, item):
        if item in self.bag:
            print("You already have the", item)
        else:
            self.bag.append(item)
            print("You collected:", item)

    def show_bag(self):
        if len(self.bag) == 0:
            print("Your bag is empty.")
        else:
            print("Your bag:", self.bag)


class Place:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def visit(self):
        print("\nYou visit the", self.name)
        print(self.description)


class LockedPlace(Place):
    def __init__(self, name, description, required_item):
        super().__init__(name, description)
        self.required_item = required_item
        self.locked = True

    def visit(self):
        if self.locked:
            print("\nThe", self.name, "is locked.")
            print("You need a", self.required_item, "to enter.")
        else:
            print("\nYou enter the", self.name)
            print(self.description)

    def unlock(self, player):
        if self.required_item in player.bag:
            self.locked = False
            print("The door unlocks!")
        else:
            print("You do not have the", self.required_item)


class Chest:
    def __init__(self, required_code):
        self.required_code = required_code
        self.opened = False

    def open(self, player):
        if self.opened:
            print("The chest is already open.")
        elif self.required_code in player.bag:
            self.opened = True
            print("\nThe code works!")
            print("The chest opens...")
            print("Congratulations! You found the missing fest trophy!")
        else:
            print("\nThe chest is locked.")
            print("You need the secret code.")


# -----------------------------
# Create objects
# -----------------------------

player = Player("Om")

canteen = Place(
    "Canteen",
    "A busy canteen. You notice a small key hidden under a table."
)

lab = LockedPlace(
    "Computer Lab",
    "Inside the lab, you find a secret code written on the computer.",
    "key"
)

stage = Place(
    "Main Stage",
    "The main stage has a large trophy chest."
)

chest = Chest("4821")


# -----------------------------
# Failed route
# -----------------------------

print("========== FAILED ROUTE ==========")

stage.visit()
chest.open(player)

lab.visit()

player.show_bag()


# -----------------------------
# Winning route
# -----------------------------

print("\n========== WINNING ROUTE ==========")

canteen.visit()

player.collect("key")

# Try collecting the same item again
player.collect("key")

player.show_bag()

lab.visit()

lab.unlock(player)
lab.visit()

# Collect the secret code
player.collect("4821")

player.show_bag()

stage.visit()

chest.open(player)