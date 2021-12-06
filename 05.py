import re
from collections import defaultdict

matcher = re.compile(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")


def part1(data: str):
    lines = data.split("\n")

    ocean_floor = OceanFloor(1000, 1000)

    for line in lines:
        try:
            ocean_floor.add_line(line)
        except NotImplementedError:
            print("%s is not a straight line!" % line)

    return len(ocean_floor.intersection_points)


def part2(data: str):
    lines = data.split("\n")

    ocean_floor = OceanFloor(1000, 1000, include_diagonals=True)

    for line in lines:
        ocean_floor.add_line(line)

    return len(ocean_floor.intersection_points)


class OceanFloor:
    def __init__(self, max_x: int = 9, max_y: int = 9, include_diagonals: bool = False):
        self._points = defaultdict(int)
        self.max_x = max_x
        self.max_y = max_y
        self.include_diagonals = include_diagonals

    def add_line(self, line: str):
        groups = matcher.match(line).groups()

        start_x = int(groups[0])
        start_y = int(groups[1])
        end_x = int(groups[2])
        end_y = int(groups[3])

        x = start_x
        y = start_y

        if not (start_x == end_x or start_y == end_y) and not self.include_diagonals:
            raise NotImplementedError("Only handling straight lines!")

        while not (x == end_x and y == end_y):
            self._points[(x, y)] += 1

            if x != end_x:
                x = x + 1 if end_x > x else x - 1
            if y != end_y:
                y = y + 1 if end_y > y else y - 1

        self._points[(end_x, end_y)] += 1

    @property
    def intersection_points(self):
        return [k for k, v in self._points.items() if v > 1]

    def __str__(self):
        s = ""
        for i in range(self.max_x + 1):
            for j in range(self.max_y + 1):
                s += str(self._points.get((i, j), "."))
                s += "\t"
            s += "\n"
        return s
