from avlTree import AvlTree
from node import Node

def printMenu()->None:
    print("Choose an option")
    print("1. Prepopulate the AVL")
    print("2. Insert an Element")
    print("3. Find the Next Larger")
    print("4. Find the Predecessor")
    print("5. Delete an element")
    print("6. Print the AVL")
    print("7. Controlla bilanciamento")
    print("0. Exit")
    pass

def prepopulateAVL()->AvlTree:
    return AvlTree()
    
def delete(value:int)->None:
    pass

exitPrg:bool = False

avl:AvlTree = AvlTree()
while exitPrg==False:
    printMenu()
    choice:int = int(input())
    
    match choice:
        case 1:
            avl = prepopulateAVL()
        case 2:
            toInsert:int = int(input("Insert a value."))
            avl.insert(toInsert)
        case 3:
            nextLargVal:int = int(input("Insert the node value used as base for the Next Larger"))
            nextLarger:Node = avl.nextLarger(avl.findNodeByValue(nextLargVal))
            if nextLarger != None:
                print(f"The next larger node of {nextLargVal} is {nextLarger.nodeValue}")
            else:
                print(f"The next larger node of {nextLargVal} doesn't exist")
        case 4:
            predecVal:int = int(input("Insert the node value used as base for the Next Larger"))
            predecessor:Node = avl.nextLarger(avl.findNodeByValue(predecVal))
            if predecessor != None:
                print(f"The next larger node of {predecVal} is {predecessor.nodeValue}")
            else:
                print(f"The next larger node of {predecVal} doesn't exist")
        case 5:
            valToDel:int = int(input("Insert the node value to delete."))
        case 6:
            avl.printValues()
        case 7:
            avl.checkForUnbalance()
        case 0:
            exitPrg = True
        case _:
            print("Unexpected value. Try something else")
    pass



