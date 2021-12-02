def part1(data):
    measurements = [int(measurement) for measurement in data.split("\n")]

    previous_measurement = measurements[0]

    increases = 0

    for measurement in measurements[1:]:
        if measurement > previous_measurement:
            increases += 1
        previous_measurement = measurement

    return increases


def part2(data):
    measurements = [int(measurement) for measurement in data.split("\n")]
    num_measurements = len(measurements)

    previous_group = measurements[:3]

    increases = 0

    for start_position, value in enumerate(measurements[1:], start=1):
        if num_measurements < (start_position + 3):
            break

        current_group = measurements[start_position:start_position + 3]

        if sum(current_group) > sum(previous_group):
            increases += 1

        previous_group = current_group

    return increases
