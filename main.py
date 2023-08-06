class Warship:
    def __init__(self, name, coordinates):
        names = {"Aircraft Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
        self.name = name
        self.length = names[name]
        self.coordinates = coordinates
        self.destroyed = []

    def is_destroyed(self):
        return sorted(self.coordinates) == sorted(self.destroyed)


class Board:
    def __init__(self):
        self.y = "ABCDEFGHIJ"
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.missed_shots = []
        self.made_shots = []
        self.ships = []
        self.destroyed_ships = []

    def register_ship(self, ship):
        self.ships.append(ship)

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
                    if ship.is_destroyed:
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




