from unicodedata import name
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
    board = Board(grid_to_pathfind)
    open_nodes = PriorityList()
    destination_reached = False
    open_nodes.add_node(board.initial_node)

    while not destination_reached:
        board.string()

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

                print(f"Checking {space_to_check} from {checking_from}")

                node_to_check = board.get_node_at_position(space_to_check[0], space_to_check[1])

                if node_to_check != None:

                    if node_to_check.state == "closed" and node_to_check.steps_from_start < checking_node.steps_from_start:
                        node_to_check.steps_from_start = checking_node.steps_from_start + 1
                        node_to_check.re_evaluate()
                        node_to_check.parent_direction = invert_direction(checking_direction)

                    elif node_to_check.state == "open" and checking_node.steps_from_start < node_to_check.steps_from_start:
                        node_to_check.steps_from_start = checking_node.steps_from_start + 1
                        node_to_check.re_evaluate()
                        node_to_check.parent_direction = invert_direction(checking_direction)

                    elif node_to_check.state == "empty":
                        node_to_check.open(checking_node.steps_from_start, board.endposition)
                        open_nodes.add_node(node_to_check)

                board.set_node_at_position(node_to_check, space_to_check[0], space_to_check[1])

        board.set_node_at_position(checking_node, checking_from[0], checking_from[1])


if __name__ == "__main__":
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    a_star_pathfind(grid)
