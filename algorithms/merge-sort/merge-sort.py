from array import array
from random import randint


'''
    Effettua il merge tra due liste ordinate.
    Il merge viene effettuato usando uno scorrimento con due indici e
    continua fin quando la lista minore non viene esaurita.
    All'interno del ciclo, si aggiunge l'elemento minore ad una lista di result
    
    Appena viene esaurita la lista minore, il rimanente viene inserito nella
    lista di result in quanto già sortata.
    
    O(firstList+secondList) = O(secondList) = O(n) lunghezza lista maggiore
'''
def merge(firstList:array, secondList:array)->array:
    result:array = []
    firstIndex:int = 0
    secondIndex:int= 0
    
    while firstIndex<len(firstList) and secondIndex<len(secondList):
        if firstList[firstIndex] < secondList[secondIndex]:
            result.append(firstList[firstIndex])
            firstIndex+=1
        else:
            result.append(secondList[secondIndex])
            secondIndex+=1
    
    while firstIndex < len(firstList):
        result.append(firstList[firstIndex])
        firstIndex+=1
        
    while secondIndex < len(secondList):
        result.append(secondList[secondIndex])
        secondIndex+=1
    
    return result

def mergeSort(startingList:array)->array:
    length:int = len(startingList) 
    
    if length == 0:
        return []
    elif length == 1:
        return startingList
    else:
        # main impl.
        middleIndex:int = length // 2
        leftList:array = mergeSort(startingList[0: middleIndex])
        rightList:array = mergeSort(startingList[middleIndex:length])
        
        return merge(leftList, rightList)



# Populating array to sort
listToSort:array = [None]*10;
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

sortedArray = mergeSort(listToSort)
print(f"Elementi sortati: {sortedArray}")