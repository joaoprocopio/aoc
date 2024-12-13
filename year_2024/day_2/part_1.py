from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


MIN_SAFE_VARIATION = 1
MAX_SAFE_VARIATION = 3
SAFE_VARIATION = range(MIN_SAFE_VARIATION, MAX_SAFE_VARIATION + 1)


with open(file_path, "r") as file:
    for report_index, report in enumerate(file):
        last_visited_level = 0
        curr_report_variation = 0

        for level_index, level in enumerate(report.split(" ")):
            level = int(level)

            if level_index == 0:
                # se for o primeiro `level` do `report`, não tem com o que parar pode pular
                last_visited_level = level
                continue

            # só precisamos saber o tamanho da variação, independente se for uma variação positiva ou negativa
            curr_report_variation = abs(last_visited_level - level)

            if curr_report_variation not in SAFE_VARIATION:
                print(last_visited_level, level, curr_report_variation)
                break

            # agora que fizemos as comparações podemos comparar o `level` atual como visitado e ir pro próximo
            last_visited_level = level
