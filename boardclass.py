from nodeclass import Node


class Board:
    def __init__(self, startlist):

        endindplaced = False
        startingplaced = False
        self.board = startlist

        for y, row in enumerate(startlist):
            for x, obj in enumerate(row):

                # Blank Node
                if obj == 0:
                    self.board[y][x] = Node("empty", (x, y))

                # Block Node
                elif obj == 1:
                    self.board[y][x] = Node("block", (x, y))

                # Start Node
                elif obj == 2:
                    if startingplaced:
                        print(f"({x},{y})    More than one start node has been found. Only the first one will be counted.")
                        self.board[y][x] = Node("empty", (x, y))
                    else:
                        startingplaced = True
                        self.board[y][x] = Node("open", (x, y), isstart=True)
                        self.initial_node = self.board[y][x] = Node("open", (x, y), isstart=True)

                # End Node
                elif obj == 3:
                    if endindplaced:
                        print(f"({x},{y})    More than one end node has been found. Only the first one will be counted.")
                        self.board[y][x] = Node("empty", (x, y))
                    else:
                        endindplaced = True
                        self.board[y][x] = Node("empty", (x, y), isend=True)
                        self.endposition = (x, y)

                else:
                    print(f"({x},{y})    Node code invalid. Adding blank node.")
                    self.board[y][x] = Node("empty", (x, y))

        self.initial_node.open(-1, self.endposition)

    def get_node_at_position(self, x, y) -> Node:
        xval = x
        yval = y

        if xval < 0 or yval < 0:
            return

        try:
            return self.board[yval][xval]
        except IndexError:
            return None

    def set_node_at_position(self, val, x, y):
        xval = x
        yval = y

        if xval < 0 or yval < 0:
            return

        try:
            self.board[yval][xval] = val
        except IndexError:
            return

    def string(self):
        print("\n\n==========BOARD:")
        for row in self.board:
            for obj in row:
                obj.string()
            print("\n")
