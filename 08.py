from collections import defaultdict

NUMBERS = {
    ("a", "b", "c", "e", "f", "g"): 0,
    ("c", "f"): 1,
    ("a", "c", "d", "e", "g"): 2,
    ("a", "c", "d", "f", "g"): 3,
    ("b", "c", "d", "f"): 4,
    ("a", "b", "d", "f", "g"): 5,
    ("a", "b", "d", "e", "f", "g"): 6,
    ("a", "c", "f"): 7,
    ("a", "b", "c", "d", "e", "f", "g"): 8,
    ("a", "b", "c", "d", "f", "g"): 9,
}


def part1(data: str):
    lines = data.split("\n")

    def easy_digit_filter(digit: str) -> bool:
        return len(digit.strip()) in {2, 3, 4, 7}

    easy_digits = []
    for line in lines:
        unique_signal_patterns, four_digit_output_values = line.split("|")

        easy_digits.extend(
            [
                v.strip()
                for v in four_digit_output_values.split()
                if easy_digit_filter(v)
            ]
        )

    return len(easy_digits)


def part2(data: str):
    lines = data.split("\n")

    sum_ = 0

    for line in lines:
        unique_signal_patterns, four_digit_output_values = line.split("|")

        scrambled_digits = [d.strip() for d in unique_signal_patterns.split()]

        by_length = defaultdict(list)
        for d in scrambled_digits:
            by_length[len(d)].append(set(d))

        digits = {
            1: by_length[2][0],
            4: by_length[4][0],
            7: by_length[3][0],
            8: by_length[7][0],
        }

        def filter_3(digit: set) -> bool:
            """
            3 can be found by using the fact that it's the 5 section digit that shares 2
            sections with 1 (the others are 2 and 5 which only share 1 each)
            """
            return len(digit.intersection(digits[1])) == 2

        digits[3] = next(filter(filter_3, by_length[5]))

        # 9 can be found by using the fact that it's the union of sections between 3 & 4
        digits[9] = digits[4].union(digits[3])

        def filter_5(digit: set) -> bool:
            """
            5 can be found as the only remaining 5 section digit that shares all it's
            sections with 9. Note this only works once we've found digit 3.
            """
            return len(digit.intersection(digits[9])) == 5 and digit != digits[3]

        digits[5] = next(filter(filter_5, by_length[5]))

        # 2 is the only remaining digit with 5 sections
        digits[2] = next(
            filter(lambda x: x not in (digits[5], digits[3]), by_length[5])
        )

        # 0 is all the sections (aka. 8) excluding section d (which can be found using
        # the intersection between digits 2, 4 and 5
        section_d = set.intersection(digits[2], digits[4], digits[5])
        digits[0] = digits[8].difference(section_d)

        # 6 is the only 6 section digit remaining
        digits[6] = next(
            filter(lambda x: x not in (digits[9], digits[0]), by_length[6])
        )

        assert all(x in digits for x in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

        # now that we've got all the digits we want to invert the mappings and then use
        # the inverted mappings to build the values as required
        inverted = {"".join(sorted(value)): key for key, value in digits.items()}

        # since we don't know what order the characters are in each digit, and we've
        # used a sorted string for the key of the inverted mappings dict, we need to
        # make sure the characters in each of the output values are sorted too
        sorted_output_values = [
            "".join(sorted(x)) for x in four_digit_output_values.split()
        ]

        output_value_string = "".join([str(inverted[x]) for x in sorted_output_values])
        sum_ += int(output_value_string)

    return sum_
