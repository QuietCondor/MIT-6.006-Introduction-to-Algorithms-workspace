class CountingSort:
    
    def countingSort(items:list[int], max:int)->list[int]:
        occurences:list[int] = [0]*(max+1)
        
        for item in items:
            occurences[item] += 1
        
        result:list[int] = []
        
        for i in range(0, max):
            occurence:int = occurences[i]
            if occurence == 0:
                occurences.pop(i)
            else:
                for c in range(0, occurence):
                    result.append(i)
        
        return result
    
    pass