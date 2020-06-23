from . import Node, Rectangle


class Tree:

    def __init__(self, root: Node):
        self.root = root

    def insert(self, active_node: Node, rectangle: Rectangle):
        # if active node contain the incoming rect, check if children contain the incoming rect
        if active_node.rectangle.has_inside(rectangle, active_node) and active_node.children:
            # case 1: one of the children of the active node contain the incoming rect
            #  - call insert function again, changing active node to that specific child
            # case 2: none of the children of the active node contain the incoming rect and
            #   incoming rect also doesnt contain any of the children
            # - add incoming rect as child of active node
            children: Node
            for children in active_node.children:
                # case 1
                if children.rectangle.has_inside(rectangle):
                    self.insert(children, rectangle)
                    return True
            # case 2
            active_node.children.append(Node(rectangle, active_node))
            return True
        # when active node contain the incoming rect but doesnt have any children
        #  - add incoming rect as children of active node
        elif active_node.rectangle.has_inside(rectangle, active_node):
            active_node.children.append(Node(rectangle, active_node))
            return True

    def get_land_count(self, node: Node):
        result = 0
        for child in node.children:
            result += self.get_land_count(child)
        return int(node.land) + result
