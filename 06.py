from collections import defaultdict


def part1(data: str):
    return _get_population_after_days(data)


def part2(data: str):
    return _get_population_after_days(data, days=256)


def _get_population_after_days(starting_timers: str, days: int = 80) -> int:
    timers = [int(v) for v in starting_timers.split(",")]
    shoal = defaultdict(int)

    for timer in timers:
        shoal[timer] += 1

    for _ in range(days):
        new_shoal = defaultdict(int)
        for key, value in shoal.items():
            if key == 0:
                new_shoal[6] += value
                new_shoal[8] += value
            else:
                new_shoal[key - 1] += value
        shoal = new_shoal

    return sum(shoal.values())
