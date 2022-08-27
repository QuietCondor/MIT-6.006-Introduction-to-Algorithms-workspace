class CountingSort:
    
    def __calculateOccurences(items:list[int], max:int)->list[int]:
        occurences:list[int] = [0]*(max+1)
        
        for item in items:
            occurences[item] += 1
        
        return occurences

    def countingSort(items:list[int], max:int)->list[int]:
        occurences:list[int] = CountingSort.__calculateOccurences(items, max)

        result:list[int] = []
        
        for i in range(0, max):
            occurence:int = occurences[i]
            if occurence == 0:
                occurences.pop(i)
            else:
                for c in range(0, occurence):
                    result.append(i)
        
        return result

    def preciseCountingSort(items:list[int], max:int)->list[int]:
        occurences:list[int] = CountingSort.__calculateOccurences(items, max)

        sum:int=len(items)
        second:list[int] = [None]*len(occurences)
        result:list[int] = [None]*len(items)

        # populating the second array

        i:int = len(second)-1
        while i>=0:
            sum = sum - occurences[i]
            second[i] = sum
            i-=1

        # accessing the values in the second array to determine
        # the exact order

        for itemIndex in range(0,len(items)):
            itemValue:int = items[itemIndex]

            position:int = second[itemValue]
            second[itemValue]+=1
            result[position] = itemValue

        return result
    
    def matrixCountingSort(matrix:list[list[int]], max:int)->list[list[int]]:
        
        
        return []