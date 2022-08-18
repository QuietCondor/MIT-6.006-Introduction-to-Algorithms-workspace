from array import array
from node import Node
import math

class BinarySearchTree(object):
    def __init__(self, nodes:list[int] ) -> None:
        self.nodesLength:int = len(nodes)
        assert self.nodesLength > 0
        
        # Se c'è solo 1 elem, assegnare tutte le variabili fondamentali
        # O(1)
        self.nodeRoot = Node(nodes[0])
        
        if self.nodesLength == 1:
            self.rawNodes:list[Node] = [Node(nodes[0])]
            self.levels = 1
            self.endNode = self.rawNodes[0]
            pass
        
        # Altrimenti, popolare i nodi dal nodo padre e calcolane i livelli
        # O(2n+log n)
        self.rawNodes:list[Node] = self.populateRawNodes(nodes)
        
        self.initializeBST()
        self.levels = self.nodeRoot.depth +1
        pass

    def populateRawNodes(self, nodes:list[int])-> list[Node]:
        """Crea una lista copia della lista in esame avvolgendo i valori in Node

        Args:
            nodes (list[int]): la lista originale da avvolgere

        Time Complexity:
            O(n) in cui n è la lista di partenza (nodes)

        Returns:
            list[Node]: la lista composta
        """
        result:list[Node] = []
        
        for node in nodes:
            result.append( Node(node) )        
        
        return result

    def initializeBST(self)-> None:
        currentParent:Node = self.nodeRoot
        nodeIndex:int = 1
        
        while nodeIndex< self.nodesLength:
            firstCurrentNode:Node = self.rawNodes[nodeIndex]
            self.insertNodes(firstCurrentNode,currentParent)
            
            nodeIndex+=1            
        pass

    def insertNodes(self, nodeToInsert:Node, baseNode:Node):        
        nodeValue: int = nodeToInsert.nodeValue
        
        # Se il nodo padre non ha figli a destra e il valore del nodo da inserire è maggiore
        if baseNode.rightChild==None and nodeValue > baseNode.nodeValue:
            # Allora va inserito il nodo come figlio a destra del nodo padre
            baseNode.rightChild = nodeToInsert
            nodeToInsert.parentNode = baseNode
            # E va aggiornata la profondità del nodo
            self.updateWholeDepth(nodeToInsert.parentNode)
            return
        elif nodeValue > baseNode.nodeValue:
            # Altrimenti, se il nodo ha già il figlio a destra, va ri-eseguito l'inserimento 
            # con nodo padre il figlio a destra del nodo padre attuale
            self.insertNodes(nodeToInsert, baseNode.rightChild)
            return
        
        # Se il nodo padre non ha figli a sinistra e il valore del nodo da inserire è minore    
        if baseNode.leftChild==None and nodeValue < baseNode.nodeValue:
            # Allora va inserito il nodo come figlio a sinistra del nodo padre
            nodeToInsert.parentNode = baseNode
            baseNode.leftChild = nodeToInsert
            # E va aggiornata la profondità
            self.updateWholeDepth(nodeToInsert.parentNode)
            return
        elif nodeValue < baseNode.nodeValue:
            # Altrimenti, se si ha già il figlio a sinistra, va ri-eseguito l'inserimento
            # con nodo padre il figlio a sinistra del nodo padre attuale
            self.insertNodes(nodeToInsert, baseNode.leftChild)
        pass

    def updateWholeDepth(self, node:Node):
        while node != None:
            self.updateDepth(node)
            node = node.parentNode
        
        pass

    def updateDepth(self, parent:Node):
        assert parent.rightChild != None or parent.leftChild != None
        
        if parent.rightChild == None:
            parent.depth = parent.leftChild.depth + 1
            return    
        
        if parent.leftChild == None:
            parent.depth = parent.rightChild.depth + 1
            return
        
        if parent.rightChild.depth > parent.leftChild.depth:
            parent.depth = parent.rightChild.depth + 1
            return
        
        parent.depth = parent.leftChild.depth + 1
        pass

    def getIndexesForLevel(self, level:int)->list[int]:
        """Questo metodo deduce gli indici da stampare per un determinato livello di una

        Args:
            level (int): Il numero di livello

        Time Complexity:
            O(log n) In cui n è il numero totale dei nodi.
            In questo caso l'iterazione viene fatta sui livelli equivalenti alla traversata più lunga 

        Returns:
            list[int]: la lista contenente gli indici per il determinato livello
        """
        
        # Basecase, solo livello root.
        if level == 1:
            return [0]
        
        # ALtrimenti, ricava il numero di nodi usando la formula
        # elementi = 2^(numero_livello-1)
        numberOfElements:int = 2**(level-1)
        indexStart:int = -1 # -1 per ovviare al livello 1 in cui c'è solo 1 elemento
        
        for levelNum in range(1,level):
            indexStart=indexStart + 2**(levelNum-1)
        

        result:array = range(indexStart+1, math.floor(indexStart+numberOfElements+1))
        
        return result

    def getChildNodeProvenience(self, node:Node, parentNode:Node)->bool:
        result:bool = None

        if parentNode.leftChild!=None and node.nodeValue == parentNode.leftChild.nodeValue:
            result = True
        elif parentNode.rightChild!=None and node.nodeValue == parentNode.rightChild.nodeValue:
            result = False

        return result

    def findMin(self, startingNode:Node = None)-> Node:
        """
        This method returns the mimimum element int the BST
        by going all the way to the left.

        Parameters:
            - startingNode:Node: The starting node, if not defined 
                it will contain None and then the nodeRoot

        Time Complexity:
            O(h): In which h is the height of the BST.
            It can be n or log n if the BST is balanced or unbalanced.

        Returns:
            Node: The min value node.
        """        
        
        if startingNode == None:
            startingNode = self.nodeRoot
        
        while startingNode.leftChild != None:
            startingNode = startingNode.leftChild
        
        return startingNode

    def findMax(self, startingNode:Node = None)->Node:
        """
        This method returns the maximum element int the BST
        by going all the way to the right.

        Parameters:
            - startingNode:Node: The starting node, if not defined 
                it will contain None and then the nodeRoot

        Time Complexity:
            O(h): In which h is the height of the BST.
            It can be n or log n if the BST is balanced or unbalanced.

        Returns:
            Node: The node with the biggest value.
        """
        
        if startingNode == None:
            startingNode:Node = self.nodeRoot
        
        while startingNode.rightChild != None:
            startingNode = startingNode.rightChild
        
        return startingNode

    def nextLarger(self, startingNode:Node)->Node:
        # Basecase: il nodo è il root e non ha figli a destra
        if startingNode == self.nodeRoot and startingNode.rightChild == None:
            return None
        
        
        # Se il nodo ha un figlio a destra
        # andare su di esso e poi tutto a sinistra
        
        rightChild:Node = startingNode.rightChild
        
        if rightChild != None:
            return self.findMin(rightChild)
        
        # Se il nodo non ha un figlio a destra
        # andare in alto fin quando 
        # - si proviene da sinistra verso destra e non si ha un figlio a destra
        # - si proviene da destra verso sinistra e si trova un padre a destra
        parent:Node = startingNode.parentNode
        doMinSearch:bool = False
        getParentResult:bool = False
        
        while parent != None:
            provenience:bool = self.getChildNodeProvenience(startingNode, parent)
            
            # Da sinistra
            if provenience == True and parent.rightChild != None:
                doMinSearch = True
                break
            if provenience == False and parent.parentNode != None and self.getChildNodeProvenience(parent, parent.parentNode) == True:
                getParentResult = True
                break                
            
            startingNode = parent
            parent = startingNode.parentNode
            
        if doMinSearch:
            return self.findMin(parent.rightChild)
        if getParentResult:
            return parent.parentNode
        
        return None

    def nextShorter(self, startingNode:Node)->Node:
        # Basecase: il nodo è il root e non ha figli a destra
        if startingNode == self.nodeRoot and startingNode.leftChild == None:
            return None
        
        
        # Se il nodo ha un figlio a destra
        # andare su di esso e poi tutto a sinistra
        
        leftChild:Node = startingNode.leftChild
        
        if leftChild != None:
            return self.findMax(leftChild)
        
        # Se il nodo non ha un figlio a destra
        # andare in alto fin quando 
        # - si proviene da sinistra verso destra e non si ha un figlio a destra
        # - si proviene da destra verso sinistra e si trova un padre a destra
        parent:Node = startingNode.parentNode
        doMinSearch:bool = False
        getParentResult:bool = False
        
        while parent != None:
            provenience:bool = self.getChildNodeProvenience(startingNode, parent)
            
            if provenience == True and parent.leftChild != None:
                doMinSearch = True
                break
            if provenience == False and parent.parentNode != None and self.getChildNodeProvenience(parent, parent.parentNode) == True:
                getParentResult = True
                break                
            
            startingNode = parent
            parent = startingNode.parentNode
            
        if doMinSearch:
            return self.findMin(parent.leftChild)
        if getParentResult:
            return parent.parentNode
        
        return None
    
    def findNodeByValue(self, nodeVaule:int, node:Node = None)->Node:
        if node == None:
            node = self.nodeRoot
        
        hasNotChildren:bool = node.leftChild==None and node.rightChild == None
        if hasNotChildren and node.nodeValue != nodeVaule:
            return None    
        elif node.nodeValue == nodeVaule:
            return node
        else:
            if node.nodeValue> nodeVaule:
                return self.findNodeByValue(nodeVaule, node.leftChild)
            else:
                return self.findNodeByValue(nodeVaule, node.rightChild)

    # Utilities
    def printValues(self)->None:    
        """
        Questo metodo stampa gli elementi della coda

        Time Complexity:
            O( (log n)*(2+log n) ) = log n^2 In cui n è il numero totale dei nodi.
            In questo caso viene richiamato getIndexesForLevel che è già log n dentro i livelli
            che sono log n

        """        
        for level in range(1, self.levels+1):
            tabs:str = ""
            for index in range(0, self.levels-level):
                tabs= tabs+"\t"
                
            
            indexes:list[int] = self.getIndexesForLevel(level)
            row:str = "";
            for index in indexes:
                if index >= self.nodesLength:
                    break
                
                row += f"{self.rawNodes[index].nodeValue}\t\t";
            print(f"{tabs}{row}")
        pass
    
    def __testPrint(self)-> None:
        for index in range(0, self.nodesLength):
            print(f"Node: {self.rawNodes[index]}. \n\t Left child: {self.rawNodes[index].leftChild} \n\t Right child: {self.rawNodes[index].rightChild}")
        pass
