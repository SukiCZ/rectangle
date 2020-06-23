import decimal


class Rectangle:
    def __init__(self, string: str):
        string = string.strip().split()
        assert len(string) == 4, "Rectangle has to be defined by 4 numbers"
        try:
            self.left = decimal.Decimal(string[0])
            self.bottom = decimal.Decimal(string[1])
            self.right = decimal.Decimal(string[2])
            self.top = decimal.Decimal(string[3])
            if self.bottom > self.top or self.left > self.right:
                raise ValueError("Rectangle is invalid")
        except decimal.InvalidOperation as e:
            raise ValueError(f"Provided input is not a number, {e}")

    def __str__(self):
        return f"Rectangle({self.left, self.bottom}{self.right, self.top})"

    def do_overlap(self, other):
        # If one rectangle is on left side of other
        if self.left > other.right or self.right < other.left:
            return False

        # If one rectangle is above other
        if self.top < other.bottom or self.bottom > other.top:
            return False

        return not self.has_inside(other)

    def has_inside(self, other: "Rectangle", active_node=None):

        return all([
            self.left < other.left,
            self.bottom < other.bottom,
            self.right > other.right,
            self.top > other.top,
        ]) or all([
            other.left < self.left,
            other.bottom < self.bottom,
            other.right > self.right,
            other.top > self.top,
        ])
