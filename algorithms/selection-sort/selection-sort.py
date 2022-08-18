from array import array
from random import randint


def selectionSort(arrayToSort:array)-> array:
    prefix:int = 0
    suffix:int = len(arrayToSort)
    
    while suffix > 0:
        toMove = getMin(arrayToSort[prefix:len(arrayToSort)]) + prefix
        print(f"min {toMove}")
        tmp:int = arrayToSort[toMove]
        arrayToSort[toMove] = arrayToSort[prefix]
        arrayToSort[prefix] = tmp
        suffix-=1
        prefix+=1
        print(f"sorted step {arrayToSort}")
    
    return arrayToSort

def getMin(source:array)-> int:
    minElem:int = source[0]
    minIndex:int = 0

    for indexElem in range(0, len(source)):
        if source[indexElem]<minElem:
            minElem = source[indexElem]
            minIndex = indexElem

    return minIndex;

listToSort:array = [None]*10;

# Populating array to sort
for i in range(0,10):
    randomCandidate:int = randint(0,100)
    if randomCandidate not in listToSort:
        listToSort[i] = randomCandidate
    else:
        while randomCandidate in listToSort:
            randomCandidate= randint(0,100)
            if randomCandidate not in listToSort:
                listToSort[i] = randomCandidate
                break
            

print(f"Elementi generati da sortare {listToSort}")

sortedArray = selectionSort(listToSort)
print(f"Elementi sortati: {sortedArray}")