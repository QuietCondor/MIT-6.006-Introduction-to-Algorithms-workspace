from radixSort import RadixSort

matrix:list[list[int]]=[
    [3,4,6,8,4,7,3],
    [2,5,5,3,3,2,5],
    [9,7,7,9,6,0,5]
]

#matrix:list[list[int]]=[
#    [3,2,9],
#    [4,5,7],
#    [6,5,7],
#    [8,3,9],
#    [4,3,6],
#    [7,2,0],
#    [3,5,5]
#]

r:RadixSort = RadixSort(True, matrix)

print("Matrice selezionata")

for i in range(0, len(matrix[0])):
    print(f"Row {i+1}: {r.getRow(i)}");
    
r.radixSort(9)

print("Matrice sorted")

for i in range(0, len(matrix[0])):
    print(f"Row {i+1}: {r.getRow(i)}");