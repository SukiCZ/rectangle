import argparse
import sys

from objects import Node, Rectangle, Tree

parser = argparse.ArgumentParser(description='Calculate land and sea')
args = parser.parse_args()


def get_input(text):  # pragma: no cover
    return input(text)


def main():
    rectangles = []
    count = get_input("Enter the number of rectangles: ")
    try:
        count = int(count)
    except ValueError:
        print(f"Provided input is not a number: {count}")
        return 1

    if count == 0:
        print(0)
        return 0

    for i in range(count):
        rectangle = Rectangle(get_input(">> "))
        for rec in rectangles:
            if rec.do_overlap(rectangle):
                print(f"Rectangles are overlapping: {rectangle}, {rec}")
                return 1
        rectangles.append(rectangle)

    # Sort rectangle by their size
    sorted_rectangles = sorted(
        rectangles,
        key=lambda x: (x.right - x.left) * (x.top - x.bottom), reverse=True
    )

    # Count max top/right, min bottom/left
    min_left = min([r.left for r in sorted_rectangles]) - 1
    min_bottom = min([r.bottom for r in sorted_rectangles]) - 1
    max_right = max([r.right for r in sorted_rectangles]) + 1
    max_top = max([r.top for r in sorted_rectangles]) + 1

    sea = Node(Rectangle(f"{min_left} {min_bottom} {max_right} {max_top}"))
    tree = Tree(sea)

    for rectangle in sorted_rectangles:
        tree.insert(sea, rectangle)
    else:
        print(tree.get_land_count(sea))
    return 0


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
