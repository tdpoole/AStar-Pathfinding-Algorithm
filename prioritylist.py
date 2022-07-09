from nodeclass import Node


class PriorityList:
    def __init__(self):
        self.main_list = []

    def add_node(self, item: Node):
        self.main_list.append(item)

    def sort(self):
        self.main_list.sort(key=lambda x: x.total_cost)  # Will only be in here if opened

    def next(self) -> Node:
        if self.main_list == []:
            return "empty"
        else:
            toreturn = self.main_list[0]
            self.main_list.pop(0)
            return toreturn
