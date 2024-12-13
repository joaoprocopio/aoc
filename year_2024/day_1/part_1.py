import heapq
from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "input.txt"


left_heap: list[int] = []
right_heap: list[int] = []


with open(file_path, "r") as file:
    for line in file:
        stripped_line: str = line.rstrip("\n")
        left_value, right_value = stripped_line.split("   ")
        left_heap.append(int(left_value))
        right_heap.append(int(right_value))

heapq.heapify(left_heap)
heapq.heapify(right_heap)


total_distance = 0

while len(left_heap) > 0 and len(right_heap) > 0:
    left_heap_smallest = heapq.heappop(left_heap)
    right_heap_smallest = heapq.heappop(right_heap)

    min_distance = min(left_heap_smallest, right_heap_smallest)
    max_distance = max(left_heap_smallest, right_heap_smallest)
    total_distance += max_distance - min_distance

print(total_distance)
