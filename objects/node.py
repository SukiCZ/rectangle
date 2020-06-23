from . import Rectangle


class Node:
    def __init__(self, r: Rectangle, parent: "Node" = None, children: ["Node"] = None, land=True):
        self.rectangle = r
        self.children: [Node]
        self.children = children or []
        self.land = land

        if parent is None or parent.land:
            self.land = False
