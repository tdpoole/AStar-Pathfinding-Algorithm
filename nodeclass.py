class Node:
    def __init__(self, startingstate, position, isstart=False, isend=False):
        self.state = startingstate
        self.position = position
        self.isstart = isstart
        self.isend = isend
        self.total_cost = None  # Evaluated when opened
        self.parent_direction = None  # Evaluated whe opened

        if isstart:
            self.steps_from_start = 0

    def close(self):
        self.state = "closed"

    def open(self, steps_taken, end_position):
        self.state = "open"
        self.steps_from_start = steps_taken + 1

        x_dist_from_end = self.position[0] - end_position[0]
        y_dist_from_end = self.position[1] - end_position[1]

        if x_dist_from_end < 0:
            x_dist_from_end *= -1
        if y_dist_from_end < 0:
            y_dist_from_end *= -1

        self.dist_from_end = ((x_dist_from_end**2) + (y_dist_from_end**2)) ** 0.5
        self.total_cost = self.dist_from_end + self.steps_from_start

    def re_evaluate(self):
        self.total_cost = self.dist_from_end + self.steps_from_start

    def string(self):
        if self.state == "empty":
            print("0", end=", ")
        if self.state == "open":
            print("1", end=", ")
        if self.state == "closed":
            print("2", end=", ")
        if self.state == "block":
            print("3", end=", ")
