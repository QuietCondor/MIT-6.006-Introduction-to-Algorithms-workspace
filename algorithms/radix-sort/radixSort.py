from countingSort.countingSort import CountingSort

class RadixSort(object):

    def getRow(matrix:list[list[int]], heightIndex:int)->list[int]:
        result: list[int] = []

        for i in range(0, len(matrix)):
            result.append(matrix[i][heightIndex])

        return result

    def __swapRows(matrix:list[list[int]], indexFrom:int, indexTo:int)->None:
        for i in range(0, len(matrix)):
            tmp:int = matrix[i][indexFrom]
            matrix[i][indexFrom] = matrix[i][indexTo]
            matrix[i][indexTo] = tmp

        pass

    def radixSort(matrix:list[list[int]], max:int)->None:
        """
        
        """
        # If the matrix is empty, return the same matrix
        if len(matrix) == 0:
            return matrix

        # Sort the matrix using radix sort algorithm
        i:int = len(matrix)-1
        while i>=0:
            sortedColumn:list[int] = CountingSort.preciseCountingSort(matrix[i], max)
            
            for cellIndex in range(0, len(sortedColumn)):
                if matrix[i][cellIndex] != sortedColumn[cellIndex]:
                    RadixSort.__swapRows(matrix,matrix[i].index(matrix[i][cellIndex]), matrix[i].index(sortedColumn[cellIndex]))
                     

            i-=1
                


        pass