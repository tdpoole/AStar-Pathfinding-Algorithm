from boardclass import Board
from prioritylist import PriorityList

directions = ["NORTH", "SOUTH", "EAST", "WEST"]
direction_shifts = {"NORTH": (0, 1), "SOUTH": (0, -1), "EAST": (1, 0), "WEST": (-1, 0)}


def invert_direction(direction):
    if direction == "NORTH":
        r = "SOUTH"
    if direction == "SOUTH":
        r = "NORTH"
    if direction == "EAST":
        r = "WEST"
    if direction == "WEST":
        r = "EAST"
    return r


def a_star_pathfind(grid_to_pathfind):
    # input()

    board = Board(grid_to_pathfind)

    # input()

    open_nodes = PriorityList()
    destination_reached = False
    open_nodes.add_node(board.initial_node)

    while not destination_reached:
        # input()

        open_nodes.sort()

        checking_node = open_nodes.next()
        checking_node.close()
        # Have we reached the end?
        if checking_node.isend:
            destination_reached = True

        else:  # Open Neighbours

            checking_from = checking_node.position
            for checking_direction in directions:
                xcheck = checking_from[0] + direction_shifts[checking_direction][0]
                ycheck = checking_from[1] + direction_shifts[checking_direction][1]
                space_to_check = (xcheck, ycheck)

                node_to_check = board.get_node_at_position(space_to_check[0], space_to_check[1])

                if node_to_check != None:

                    #                    if node_to_check.state == "closed" and node_to_check.steps_from_start < checking_node.steps_from_start:
                    #                        node_to_check.steps_from_start = checking_node.steps_from_start + 1
                    #                        node_to_check.re_evaluate()
                    #                        node_to_check.parent_direction = invert_direction(checking_direction)
                    #
                    #                    elif node_to_check.state == "open" and checking_node.steps_from_start < node_to_check.steps_from_start:
                    #                        node_to_check.steps_from_start = checking_node.steps_from_start + 1
                    #                        node_to_check.re_evaluate()
                    #                        node_to_check.parent_direction = invert_direction(checking_direction)
                    #
                    if node_to_check.state == "empty":
                        node_to_check.open(checking_node.steps_from_start, board.endposition)
                        node_to_check.parent_direction = invert_direction(checking_direction)
                        open_nodes.add_node(node_to_check)

                board.set_node_at_position(node_to_check, space_to_check[0], space_to_check[1])

        board.set_node_at_position(checking_node, checking_from[0], checking_from[1])

    # Trace the path back!
    result = []
    for y, row in enumerate(board.board):
        row_to_add = []
        for x, node in enumerate(row):
            if node.state == "block":
                row_to_add.append("🟥")
            else:
                row_to_add.append("⬜")
        result.append(row_to_add)

    start_unreached = True
    looking_at_node_at_pos = board.endposition
    while start_unreached:
        # input("==========\n==========")
        result[looking_at_node_at_pos[1]][looking_at_node_at_pos[0]] = "⬛"
        looking_at_node = board.get_node_at_position(looking_at_node_at_pos[0], looking_at_node_at_pos[1])

        if looking_at_node.isstart:
            start_unreached = False

        else:
            direction_to_travel_in = looking_at_node.parent_direction
            new_node_position = ((looking_at_node_at_pos[0] + direction_shifts[direction_to_travel_in][0]), (looking_at_node_at_pos[1] + direction_shifts[direction_to_travel_in][1]))
            looking_at_node_at_pos = new_node_position

    print("====================\nFINISHED:")
    for row in result:
        for node in row:
            print(node, end="")
        print()


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    a_star_pathfind(grid)
