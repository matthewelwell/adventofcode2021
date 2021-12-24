from statistics import median

OPEN_CLOSE_MAP = {"(": ")", "{": "}", "[": "]", "<": ">"}
CLOSE_OPEN_MAP = {v: k for k, v in OPEN_CLOSE_MAP.items()}
PART_1_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
PART_2_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def part1(data: str):
    corrupted_lines = []
    exceptions = []

    for line in data.split("\n"):
        try:
            parse_line(line)
        except CorruptedError as e:
            corrupted_lines.append(line)
            exceptions.append(e)

    return sum([PART_1_SCORES[exception.illegal_char] for exception in exceptions])


def part2(data: str):
    completion_strings = []

    for line in data.split("\n"):
        try:
            completion_strings.append(get_completion_string(line))
        except CorruptedError:
            continue

    scores = [
        calculate_completion_string_score(completion_string)
        for completion_string in completion_strings
    ]
    return median(scores)


class CorruptedError(Exception):
    def __init__(self, *args, illegal_char: str, **kwargs):
        super(CorruptedError, self).__init__(*args, **kwargs)
        self.illegal_char = illegal_char


def parse_line(line: str):
    queue = []
    for char in line:
        if char in {"(", "<", "[", "{"}:
            queue.append(char)
        else:
            last_open = queue.pop()
            if last_open != CLOSE_OPEN_MAP[char]:
                raise CorruptedError(
                    f"Line is corrupted. Expected {CLOSE_OPEN_MAP[char]} got {char}",
                    illegal_char=char,
                )


def get_completion_string(line: str) -> str:
    queue = []
    for char in line:
        if char in {"(", "<", "[", "{"}:
            queue.append(char)
        else:
            last_open = queue.pop()
            if last_open != CLOSE_OPEN_MAP[char]:
                raise CorruptedError(
                    f"Line is corrupted. Expected {CLOSE_OPEN_MAP[char]} got {char}",
                    illegal_char=char,
                )

    return "".join([OPEN_CLOSE_MAP[c] for c in queue[::-1]])


def calculate_completion_string_score(completion_string: str) -> int:
    score = 0
    for char in completion_string:
        score *= 5
        score += PART_2_SCORES[char]
    return score
