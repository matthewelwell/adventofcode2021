import statistics


def part1(data: str):
    crab_positions = [int(p) for p in data.split(",")]

    def calc_distances(x: int):
        return sum(abs(x - i) for i in crab_positions)

    median = statistics.median(crab_positions)
    return calc_distances(median)


def part2(data: str):
    crab_positions = [int(p) for p in data.split(",")]

    def calc_fuel_cost(x: int) -> int:
        current_fuel_cost = 0
        for position in crab_positions:
            current_fuel_cost += sum(range(1, abs(position - x) + 1))
        return current_fuel_cost

    mid_point = 0
    fuel_cost = calc_fuel_cost(0)

    max_position = max(crab_positions)
    for i in range(1, max_position + 1):
        new_fuel_cost = calc_fuel_cost(i)
        if new_fuel_cost > fuel_cost:
            break

        mid_point = i
        fuel_cost = new_fuel_cost

    return mid_point, fuel_cost

