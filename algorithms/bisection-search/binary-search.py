from array import array


def binarySearch(elementToFind:int, collection:array)-> int : 
    
    colLength: int = len(collection)
    
    # Base case cases:
    if colLength == 0:
        return -1 # Element not found
    elif colLength == 1 and elementToFind == collection[0]:
        return 0 # Element is the first
    else:
        # Main logic
        midIndex:int = colLength//2
        midElem:int  = collection[midIndex] 
        if midElem == elementToFind:
            return midIndex
        elif elementToFind < midElem:
            return binarySearch(elementToFind, collection[0:midIndex])
        else:
            return binarySearch(elementToFind, collection[midIndex:colLength])
    


someElements = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
elemToFind = 1
indexOfElem = binarySearch(elemToFind, someElements)

if indexOfElem == -1:
    print('Elemento non trovato')
else:
    print(f'Elemento trovato in posizione {indexOfElem} elementi: {someElements}')