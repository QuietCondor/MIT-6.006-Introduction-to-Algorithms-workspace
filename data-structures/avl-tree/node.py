class Node(object):
    def __init__(self, nodeValue:int, leftChild:int=None, rightChild:int=None, parentNode=None) -> None:
        self.nodeValue:int = nodeValue
        self.leftChild:Node = None
        self.rightChild:Node = None
        self.parentNode:Node = None
        self.tallestChildren:Node = None
        self.height:int = 0
        
        if leftChild != None:
            self.leftChild = Node(leftChild)
        
        if rightChild != None:
            self.rightChild = Node(rightChild)
            
        if parentNode != None:
            self.parentNode = parentNode
        pass        

    def __str__(self) -> str:
        return self.nodeValue.__str__()
