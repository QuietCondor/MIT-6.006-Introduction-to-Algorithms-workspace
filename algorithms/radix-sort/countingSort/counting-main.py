from countingSort import CountingSort

elements:list[int] = [1,7,8,4,0,1,6,5]

print(f"Elements in exam {elements}")

result:list[int] = CountingSort.countingSort(elements, 8)

print(f"Elements sorted with simple method: {result}")

complexResult:list[int] = CountingSort.preciseCountingSort(elements, 8)
print(f"Elements sorted with complex method: {complexResult}")
