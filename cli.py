import operator
import sys
import argparse

from objects import Rectangle


parser = argparse.ArgumentParser(description='Calculate land and sea')
parser.add_argument('-v', '--verbose', help='verbose', action="store_true")
args = parser.parse_args()


def get_input(text):  # pragma: no cover
    return input(text if args.verbose else '')


def main():
    rectangles = {}
    count_map = {}
    count = get_input("Enter the number of rectangles: ")
    try:
        count = int(count)
    except ValueError:
        print(f"Provided input is not a number: {count}")
        return 1

    for i in range(count):
        rectangle = Rectangle(get_input(">> "))
        for rec in rectangles.values():
            if rec.do_overlap(rectangle):
                print(f"Rectangles are overlapping: {rectangle}, {rec}")
                return 1
        rectangles[i] = rectangle

    for key, value in rectangles.items():
        inside = 0
        for rec in rectangles.values():
            if rec == value:
                continue
            if value.has_inside(rec):
                inside += 1
        count_map[key] = inside

    rectangle_id, max_count = max(count_map.items(), key=operator.itemgetter(1))

    print(max_count)
    if args.verbose:
        print(rectangles[rectangle_id])
    return 0


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
