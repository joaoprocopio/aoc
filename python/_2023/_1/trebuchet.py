def trebuchet(lines: list[str]):
    total = 0

    for line in lines:
        numbers = []

        for char in line:
            if not char.isdigit():
                continue

            numbers.append(char)

        total += int(numbers[0] + numbers[-1])

    return total
