def trebuchet_1(lines: list[str]):
    total: int = 0

    for line in lines:
        numbers: list[str] = []

        for char in line:
            if not char.isdigit():
                continue

            numbers.append(char)

        total += int(numbers[0] + numbers[-1])

    return total


def trebuchet_2(lines: list[str]):
    numbers: tuple[str] = (
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    total: int = 0

    for line in lines:
        digits: list[str] = []

        for char_index, char in enumerate(line):
            sub_string = line[char_index:]

            for digit_index, digit in enumerate(numbers):
                if sub_string.startswith(digit):
                    digits.append(str(digit_index + 1))

            if not char.isdigit():
                continue

            digits.append(char)

        total += int(digits[0] + digits[-1])

    return total
