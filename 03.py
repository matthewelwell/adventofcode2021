import typing
from collections import defaultdict


def part1(data):
    binary_numbers = data.split("\n")
    total = len(binary_numbers)

    positional_counts = defaultdict(int)

    for binary_number in binary_numbers:
        for i, bit in enumerate(binary_number):
            positional_counts[i] += int(bit)

    gamma_rate = ""
    epsilon_rate = ""

    for count in positional_counts.values():
        if count > total // 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(data):
    binary_numbers = data.split("\n")

    oxygen_generator_rating = _filter_values(binary_numbers)
    co2_scrubber_rating = _filter_values(binary_numbers, use_most_common=False)

    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


def _filter_values(
    values: typing.List[str], cursor: int = 0, use_most_common: bool = True
) -> str:
    ones = []
    zeroes = []

    for value in values:
        if value[cursor] == "1":
            ones.append(value)
        else:
            zeroes.append(value)

    if len(ones) > len(zeroes) or len(ones) == len(zeroes):
        new_values = ones if use_most_common else zeroes
    else:
        new_values = zeroes if use_most_common else ones

    if len(new_values) == 1:
        return new_values[0]

    return _filter_values(new_values, cursor + 1, use_most_common=use_most_common)
