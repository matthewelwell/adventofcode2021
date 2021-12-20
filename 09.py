import typing
from functools import reduce


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


def part1(data: str):
    lines = data.split("\n")
    map_ = get_map(lines)
    low_points = get_low_points(map_, max_x=len(lines[0]), max_y=len(lines))
    return sum([1 + map_[low_point] for low_point in low_points])


def part2(data: str):
    lines = data.split("\n")
    map_ = get_map(lines)
    low_points = get_low_points(map_, max_x=len(lines[0]), max_y=len(lines))

    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(calculate_basin_size(map_, low_point))

    return reduce(lambda x, y: x * y, sorted(basin_sizes, reverse=True)[:3])


def get_low_points(
    map_: typing.Dict[Point, int], max_x: int, max_y: int
) -> typing.List[Point]:
    low_points = []
    for point, height in map_.items():
        adjacent_heights = []
        if point.x - 1 >= 0:
            adjacent_heights.append(map_[Point(point.x - 1, point.y)])
        if point.x + 1 < max_y:
            adjacent_heights.append(map_[Point(point.x + 1, point.y)])
        if point.y - 1 >= 0:
            adjacent_heights.append(map_[Point(point.x, point.y - 1)])
        if point.y + 1 < max_x:
            adjacent_heights.append(map_[Point(point.x, point.y + 1)])

        if all(adjacent_height > height for adjacent_height in adjacent_heights):
            low_points.append(point)

    return low_points


def get_basin_points(map_: typing.Dict[Point, int], centre: Point) -> typing.Set[Point]:
    direction_vectors = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]
    basin_points = {centre}
    for direction_vector in direction_vectors:
        adjacent_point = centre + direction_vector
        adjacent_height = map_.get(adjacent_point)
        if adjacent_height and map_[centre] < adjacent_height < 9:
            basin_points.add(adjacent_point)
            basin_points.update(get_basin_points(map_, adjacent_point))

    return basin_points


def calculate_basin_size(map_: typing.Dict[Point, int], centre: Point) -> int:
    basin_points = get_basin_points(map_, centre)
    return len(basin_points)


def get_map(lines: typing.List[str]) -> typing.Dict[Point, int]:
    return {
        Point(i, j): int(value)
        for i, line in enumerate(lines)
        for j, value in enumerate(line)
    }
