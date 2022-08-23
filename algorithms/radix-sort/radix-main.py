from radixSort import RadixSort

matrix:list[list[int]]=[
    [3,4,6,8,4,7,3],
    [2,5,5,3,3,2,5],
    [9,7,7,9,6,0,5]
]

print("Matrice selezionata")

for i in range(0, len(matrix)):
    print(f"Actual Matrix: {RadixSort.getRow(matrix, i)}");