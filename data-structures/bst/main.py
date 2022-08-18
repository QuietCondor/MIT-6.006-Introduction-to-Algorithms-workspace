from binarySearchTree import BinarySearchTree
from node import Node

elements = [5,7,3,1,9,4,6,2,0,8]
bst = BinarySearchTree(elements)
bst.printValues()

print(f"Nodo minore: {bst.findMin().nodeValue}")
print(f"Nodo maggiore: {bst.findMax().nodeValue}")

baseNode:Node = bst.findNodeByValue(3)
nextLarger:Node = bst.nextLarger(baseNode)
predecessor:Node = bst.nextShorter(baseNode)

if nextLarger != None:
    print(f"Next larger di {baseNode} : {nextLarger.nodeValue}")
else:
    print(f"Next larger di {baseNode} : Non trovato")

if predecessor != None:
    print(f"Predecessor di {baseNode} : {predecessor.nodeValue}")
else:
    print(f"Predecessor di {baseNode} : Non trovato")
