import heapq
from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "input.txt"


left_heap: list[int] = []
left_heap_occurrences: dict[int, int] = {}

right_heap: list[int] = []
right_heap_occurrences: dict[int, int] = {}


with open(file_path, "r") as file:
    for line in file:
        stripped_line: str = line.rstrip("\n")
        splitted_line = stripped_line.split("   ")

        left_value: int = int(splitted_line[0])
        right_value: int = int(splitted_line[1])

        left_heap.append(left_value)
        right_heap.append(right_value)

        if left_value not in left_heap_occurrences:
            left_heap_occurrences[left_value] = 0

        if right_value not in right_heap_occurrences:
            right_heap_occurrences[right_value] = 0

        left_heap_occurrences[left_value] += 1
        right_heap_occurrences[right_value] += 1


heapq.heapify(left_heap)
heapq.heapify(right_heap)


total_distance = 0


while len(left_heap) > 0 and len(right_heap) > 0:
    left_heap_smallest = heapq.heappop(left_heap)
    right_heap_smallest = heapq.heappop(right_heap)

    min_distance = min(left_heap_smallest, right_heap_smallest)
    max_distance = max(left_heap_smallest, right_heap_smallest)

    distance_diff = max_distance - min_distance
    total_distance = total_distance + distance_diff


print(total_distance)
