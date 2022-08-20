from countingSort.countingSort import CountingSort, countingSort

class RadixSort(object):

    def __getRow(matrix:list[list[int]], heightIndex:int)->list[int]:
        result: list[int] = []

        for i in range(0, len(matrix)):
            result.append(matrix[i][heightIndex])

        return result

    def radixSort(matrix:list[list[int]], max:int)->None:
        """
        
        """
        # If the matrix is empty, return the same matrix
        if len(matrix) == 0:
            return matrix

        # Sort the matrix using radix sort algorithm
        for i in reversed(matrix):
            sortedColumn:list[int] = CountingSort.preciseCountingSort(matrix[i], max)
            
            for cellIndex in range(0, len(sortedColumn)):
                currRow:list[int] = RadixSort.__getRow(matrix, cellIndex)


        pass