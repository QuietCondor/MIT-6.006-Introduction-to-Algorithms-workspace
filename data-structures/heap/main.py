from maxHeap import MaxHeap
from node import Node

#elements = [0,1,2,3,4,5,6,7,8,9]
elements = [5,7,3,1,9,4,6,2,0,8]
maxHeap = MaxHeap(elements)
results:list[Node] = maxHeap.heapSort();

resultString:str = "sorted elements "
for node in results:
    resultString+= f"{node.nodeValue}"
results+=" extracted"
print(resultString)
#maxHeap.printValues()

#maxHeap.maxHeapify(maxHeap.rawNodes[0])