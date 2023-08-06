class Warship:
    def __init__(self, name, starting_coordinate, direction):
        x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        y = "ABCDEFGHIJ"
        names = {"Aircraft Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
        self.name = name
        self.length = names[name]
        self.coordinates = [starting_coordinate]
        self.destroyed = []
        self.is_valid = True

        for _ in range(self.length-1):
            current_last_coordiante = self.coordinates[-1]
            index_of_y = y.index(current_last_coordiante[0])
            index_of_x = x.index(current_last_coordiante[1])
            if direction.upper() == "D":
                index_of_y += 1
            elif direction.upper() == "U":
                index_of_y -= 1
            elif direction.upper() == "L":
                index_of_x -= 1
            elif direction.upper() == "R":
                index_of_x += 1

            if (index_of_y > 9 or index_of_y < 0) or (index_of_x > 9 or index_of_x < 0):
                self.is_valid = False

            self.coordinates.append(f"{y[index_of_y]}{x[index_of_x]}")

        # A5 DOW
    def is_destroyed(self):
        return sorted(self.coordinates) == sorted(self.destroyed)


class Board:
    def __init__(self):
        self.missed_shots = []
        self.made_shots = []
        self.ships = []
        self.destroyed_ships = []

    def register_ship(self, ship):
        for existing_ship in self.ships:
            for coordinate in ship.coordinates:
                if coordinate in existing_ship.coordinates:
                    return False
        self.ships.append(ship)
        return True

    def all_ships_destroyed(self):
        return sorted(self.ships) == sorted(self.destroyed_ships)

    def shoot(self, coordinate):
        is_missed = True
        for ship in self.ships:
            if coordinate in ship.coordinates:
                if coordinate not in ship.destroyed:
                    is_missed = False
                    self.made_shots.append(coordinate)
                    ship.destroyed.append(coordinate)
                    print("Ship was hit")
                    if ship.is_destroyed():
                        print(f"{ship.name} is destroyed")
                        self.destroyed_ships.append(ship)
                    return True
                else:
                    print("Can not shoot to the same place twice, you already destroyed this part of the ship")
                    return False

        if is_missed:
            self.missed_shots.append(coordinate)
            print('Ya missed Pirate')
            return True


# ship = Warship("Aircraft Carrier", "A1", "D")
# print(ship.coordinates)
# board = Board()
# board.register_ship(ship)
# board.shoot("A1")
# board.shoot("A2")
# board.shoot("A3")
# board.shoot("A4")
# board.shoot("A5")
# print(board.destroyed_ships)


# print(ship.is_destroyed())
# Setup the board
# Play

# Setup random board from PC

print('Hello Sir, setup your board')

ship_names = ["Aircraft Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
user_board = Board()

for ship in ship_names:
    status_of_regsitration = False
    while not status_of_regsitration:
        warship = Warship(ship, "A1", "U")
        while not warship.is_valid:
            starting_coordinate = input(f"Provide starting coordinate(A-J, 1-10) for the ship: {ship}")

            direction = input("L - LEFT, R - RIGTH, U - UP, D - DOWN")
            warship = Warship(ship, starting_coordinate, direction)

        status_of_regsitration = user_board.register_ship(warship)
        if not status_of_regsitration:
            print("The Warships can not overlap, try again..")

print("---------------- The Board is now setup, the game may start --------------------")


