from countingSort.countingSort import CountingSort

class RadixSort(object):

    def __init__(self, asColumns:bool,  matrix:list[list[int]]) -> None:
        self.asColumns:bool = asColumns
        
        # If the matrix lists are intended as columns, transform them to rows
        # to ease the logic
        #if self.asColumns:           
        #    self.matrix:list[list[int]] = self.__convertToRowsVisual(matrix)
        #    return
        
        self.matrix:list[list[int]] = matrix
        pass

    def __convertToRowsVisual(self, matrix:list[list[int]]):
        """This method converts a matrix with lists intended as columns to a
        matrix with lists intended as rows

        Args:
            matrix (list[list[int]]): The matrix

        Returns:
            list[list[int]]: The matrix converted to rows perspective
        """
        result:list[list[int]]
        
        for i in range(0,len(matrix)):
            result[i] = self.getRow(matrix, i)
        
        return result;

    def getRow(self, heightIndex:int, matrix:list[list[int]] = None)->list[int]:
        if matrix!= None:
            self.matrix = matrix
        
        if self.asColumns==False:
            return self.matrix[heightIndex]
        
        result: list[int] = []

        for i in range(0, len(self.matrix)):
            result.append(self.matrix[i][heightIndex])

        return result
    
    def getColumn(self, colIndex)->list[int]:
        if self.asColumns:
            return self.matrix[colIndex]
        
        result:list[int] = []
        for i in self.matrix:
            result.append(i[colIndex])
        
        return result

    def radixSort(self, max:int, matrix:list[list[int]] = None)->None:
        """This method implements the radix sort algorithm given a bi-dimensional
        list and the maximum number it can have.

        Args:
            max (int): The maximum number the list can have
            matrix (list[list[int]], optional): The bidirectional array. Defaults to None.
        """
        if matrix != None:
            self.matrix = matrix
        
        # If the matrix is empty, return the same matrix
        if len(self.matrix) == 0:
            return self.matrix

        # Sort the matrix using radix sort algorithm
        i:int = len(self.matrix)-1
        while i>=0:
            self.matrix = CountingSort.matrixCountingSort(self.matrix, max, i)
            i-=1

        pass