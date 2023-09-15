# In chandrayaan3.py

class Chandrayaan_mission:
    def __init__(self):
        self.direction = 'N'  # Initial direction (N, S, E, W, U, D)
        self.prev = 'N'
        self.position = [0, 0, 0]

    def movement(self, command, dir):
        if command == 'f':
            if dir == 'N':
                self.position[1] += 1
            elif dir == 'S':
                self.position[1] -= 1
            elif dir == 'E':
                self.position[0] += 1
            elif dir == 'W':
                self.position[0] -= 1
            elif dir == 'U':
                self.position[2] += 1
            elif dir == 'D':
                self.position[2] -= 1
        elif command == 'b':
            if dir == 'N':
                self.position[1] -= 1
            elif dir == 'S':
                self.position[1] += 1
            elif dir == 'E':
                self.position[0] -= 1
            elif dir == 'W':
                self.position[0] += 1
            elif dir == 'U':
                self.position[2] -= 1
            elif dir == 'D':
                self.position[2] += 1

    def turning(self, command, dir):
        if command == 'l':
            if dir == 'N':
                self.direction = 'W'
            elif dir == 'S':
                self.direction = 'E'
            elif dir == 'E':
                self.direction = 'N'
            elif dir == 'W':
                self.direction = 'S'
            elif dir == 'U':
                self.turning(command, self.prev)  # Use previous direction
            elif dir == 'D':
                self.turning(command, self.prev)  # calling function with previous direction values
        elif command == 'r':
            if dir == 'N':
                self.direction = 'E'
            elif dir == 'S':
                self.direction = 'W'
            elif dir == 'E':
                self.direction = 'S'
            elif dir == 'W':
                self.direction = 'N'
            elif dir == 'U':
                self.turning(command, self.prev)
            elif dir == 'D':
                self.turning(command, self.prev)

    def tilted(self, command, dir):
        if command == 'u':
            if dir == 'N':
                self.prev = 'N'  # storing for turn purpose
                self.direction = 'U'
            elif dir == 'S':
                self.prev = 'S'
                self.direction = 'U'
            elif dir == 'E':
                self.prev = 'E'
                self.direction = 'U'
            elif dir == 'W':
                self.prev = 'W'
                self.direction = 'U'
            else:
                self.direction = 'U'
        elif command == 'd':
            if dir == 'N':
                self.prev = 'N'
                self.direction = 'D'
            elif dir == 'S':
                self.prev = 'S'
                self.direction = 'D'
            elif dir == 'E':
                self.prev = 'E'
                self.direction = 'D'
            elif dir == 'W':
                self.prev = 'W'
                self.direction = 'D'
            else:
                self.direction = 'D'

    def execute_orders(self, commands):
        for command in commands:
            if command in ('f', 'b'):
                self.movement(command, self.direction)
            elif command in ('l', 'r'):
                self.turning(command, self.direction)
            elif command in ('u', 'd'):
                self.tilted(command, self.direction)

    def getPos(self):
        return self.position

    def getDirection(self):
        return self.direction
