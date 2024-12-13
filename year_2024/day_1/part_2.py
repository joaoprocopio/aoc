import heapq
from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "input.txt"


left_heap: list[int] = []
right_heap_occurrences: dict[int, int] = {}


with open(file_path, "r") as file:
    for line in file:
        stripped_line: str = line.rstrip("\n")
        splitted_line = stripped_line.split("   ")

        left_value: int = int(splitted_line[0])
        right_value: int = int(splitted_line[1])

        left_heap.append(left_value)

        if right_value not in right_heap_occurrences:
            right_heap_occurrences[right_value] = 0

        right_heap_occurrences[right_value] += 1


heapq.heapify(left_heap)


total_distance = 0


while len(left_heap) > 0:
    left_heap_smallest = heapq.heappop(left_heap)

    if left_heap_smallest not in right_heap_occurrences:
        continue

    occurrences_count = right_heap_occurrences[left_heap_smallest]
    total_distance += left_heap_smallest * occurrences_count


print(total_distance)
