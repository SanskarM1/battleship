class Ship:
    def __init__(self, position, direction, syze):
        """
        Creates a new Battleship.

        :param position: a tuple[int, int] containing the row/col of the back end of the ship
        :param direction: a str indicating the direction the ship is facing
        :param syze: Sanskar's amazing integer indicating the length of this ship
        """
        self.position = position
        self.direction = direction
        self.size = syze

        self.positions = []
        for i in range(self.size):
            if self.direction == 'up':
                self.positions.append((self.position[0], self.position[1] - i))
            elif self.direction == 'down':
                self.positions.append((self.position[0], self.position[1] + i))
            elif self.direction == 'right':
                self.positions.append((self.position[0] + i, self.position[1]))
            elif self.direction == 'left':
                self.positions.append((self.position[0] - i, self.position[1]))