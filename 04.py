import typing


def part1(data: str):
    lines = data.split("\n")
    numbers_to_call = [int(value) for value in lines.pop(0).split(",")]
    boards = _get_boards(lines)

    for number in numbers_to_call:
        for i, board in enumerate(boards):
            board.mark_value(number)
            if board.is_complete():
                return number * board.unmarked_values_sum


def part2(data: str):
    lines = data.split("\n")
    numbers_to_call = [int(value) for value in lines.pop(0).split(",")]
    boards = _get_boards(lines)
    completed_board_ids = set()

    for number in numbers_to_call:
        for i, board in enumerate(boards):
            board.mark_value(number)
            if board.is_complete() and board.id not in completed_board_ids:
                if len(boards) - len(completed_board_ids) == 1:
                    return board.unmarked_values_sum * number
                completed_board_ids.add(board.id)


def _get_boards(lines: typing.List[str]) -> typing.List["Board"]:
    boards = []
    current_board_rows = []

    cursor = 0

    for row in lines[1:]:  # skip the first blank row
        if row.strip() == "":
            boards.append(Board(cursor, tuple(current_board_rows)))
            current_board_rows.clear()
            cursor += 1
            continue

        current_board_rows.append(tuple(int(value) for value in row.split()))

    return boards


class Board:
    def __init__(self, id_: int, rows: typing.Tuple[typing.Tuple[int, ...], ...]):
        self.id = id_
        self._rows = rows
        if len(rows) != 5 or not all(len(row) == 5 for row in rows):
            raise ValueError("Board must be 5 x 5 grid.")

        self._value_map = {}
        for i, row in enumerate(rows):
            for j, element in enumerate(row):
                self._value_map[element] = (i, j)

        self.marked_elements = set()

    @property
    def unmarked_values_sum(self):
        sum_ = 0
        for value, position in self._value_map.items():
            if position not in self.marked_elements:
                sum_ += value
        return sum_

    def mark_value(self, value: int):
        if value in self._value_map:
            self.marked_elements.add(self._value_map[value])

    def is_complete(self):
        if not self.marked_elements:
            return False

        row_hits, column_hits = zip(*self.marked_elements)

        for i in range(5):
            if row_hits.count(i) == 5 or column_hits.count(i) == 5:
                return True

        return False

    def __str__(self):
        s = f"Board {self.id}\n"
        for i, row in enumerate(self._rows):
            for j, element in enumerate(row):
                element = str(element)
                if (i, j) in self.marked_elements:
                    element += "*"
                element += "\t"
                s += element
            s += "\n"
        return s
