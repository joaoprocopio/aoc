def trebuchet(lines: list[str]):
    total: int = 0

    for line in lines:
        numbers: list[str] = []

        for char in line:
            if not char.isdigit():
                continue

            numbers.append(char)

        total += int(numbers[0] + numbers[-1])

    return total
