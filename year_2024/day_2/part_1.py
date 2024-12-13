from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "input.txt"


MIN_SAFE_VARIATION = 1
MAX_SAFE_VARIATION = 3
SAFE_VARIATION = range(MIN_SAFE_VARIATION, MAX_SAFE_VARIATION + 1)


with open(file_path, "r") as file:
    safe_reports = 0

    for report_index, report in enumerate(file):
        report = report.split(" ")

        last_visited_level = 0
        curr_report_variation = 0

        has_increased = False
        has_decreased = False

        for level_index, level in enumerate(report):
            level = int(level)

            if level_index == 0:
                # se for o primeiro `level` do `report`, não tem com o que parar pode pular
                last_visited_level = level
                continue

            curr_report_variation = last_visited_level - level

            # checa se a variação é negativa, e marca a flag
            if curr_report_variation < 0:
                has_decreased = True

            # checa se a variação é positiva, e marca a flag
            if curr_report_variation > 0:
                has_increased = True

            # se por acaso tiver uma variação positiva junto com uma negativa é unsafe também
            if has_decreased and has_increased:
                break

            # checa se a variação não está entre 1 e 3
            if abs(curr_report_variation) not in SAFE_VARIATION:
                break

            # agora que fizemos as comparações podemos comparar o `level` atual como visitado e ir pro próximo
            last_visited_level = level

            if level_index == len(report) - 1:
                safe_reports += 1

    print(safe_reports)
