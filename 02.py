from collections import defaultdict


def part1(data):
    commands = data.split("\n")

    d = defaultdict(int)

    for command in commands:
        direction, magnitude = command.split()
        d[direction] += int(magnitude)

    return d["forward"] * (d["down"] - d["up"])


def part2(data):
    commands = data.split("\n")

    aim = 0
    horizontal_position = 0
    depth = 0

    for command in commands:
        direction, magnitude = command.split()
        if direction == "up":
            aim -= int(magnitude)
        elif direction == "down":
            aim += int(magnitude)
        else:
            depth += aim * int(magnitude)
            horizontal_position += int(magnitude)

    return depth * horizontal_position
