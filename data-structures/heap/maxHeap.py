from array import array
from turtle import right
from typing import Tuple
from unittest import result
from node import Node
import math

class MaxHeap(object):
    def __init__(self, nodes:list[int] ) -> None:
        self.nodesLength:int = len(nodes)
        assert self.nodesLength > 0
        
        # Se c'è solo 1 elem, assegnare tutte le variabili fondamentali
        # O(1)
        if self.nodesLength == 1:
            self.rawNodes:list[Node] = [Node(nodes[0])]
            self.levels = 1
            self.nodeRoot = self.rawNodes[0]
            self.endNode = self.rawNodes[0]
            pass
        
        # Altrimenti, popolare i nodi dal nodo padre e calcolane i livelli
        # O(2n+log n)
        self.rawNodes:list[Node] = self.populateRawNodes(nodes)
        
        (self.nodeRoot, self.endNode) = self.initializeHeap(self.rawNodes)
        self.levels = self.calculateLevel(self.endNode)
        self.buildMaxHeap()
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

    def initializeHeap(self, nodes:list[Node])-> Tuple[Node, Node]:
        """Inizializza la coda prendendo i vari nodi e rendendoli nested dal nodo padre

        Args:
            nodes (list[Node]): la lista di nodi da innestare

        Time Complexity:
            O(n) in cui n si intende la lista di nodi di partenza (nodes)

        Returns:
            Tuple[Node, Node]: la lista di risultato
        """
        rootNode:Node
        endNode:Node
        
        # Per ogni elemento nella lista
        for nodeIndex in range(0, self.nodesLength):
            isRootNode:bool = nodeIndex == 0
            
            # Trasforma l'elemento corrente in un nodo
            currentNode:Node = nodes[nodeIndex]
            
            if isRootNode:
                rootNode = currentNode
            
            # Funzionamento right / left child
            # Se l'elemento è il root ( indice 0 ), viene preso il 2 elem 
            # Altrimenti il doppio dell'indice
            # Se l'elemento esiste ( minore della lunghezza totale ) viene preso e aggiunto come figlio
            leftChildIndex:int = nodeIndex+1 if isRootNode else (nodeIndex+1)*2-1

            if leftChildIndex < self.nodesLength:
                leftChild:Node = nodes[leftChildIndex]
                leftChild.parentNode = currentNode
                currentNode.leftChild = leftChild
            
            rightChildIndex:int = nodeIndex+2 if isRootNode else (nodeIndex+1)*2
            if rightChildIndex < self.nodesLength:
                rightChild:Node = nodes[rightChildIndex]
                rightChild.parentNode = currentNode
                currentNode.rightChild = rightChild

            if nodeIndex == self.nodesLength-1:
                endNode = currentNode
        
        return (rootNode,endNode)

    def calculateLevel(self, startingNode:Node)-> int:
        """Dato un nodo di partenza, calcola il numero di nodi
        cercando sempre il parent.

        Args:
            startingNode (Node): Il nodo di partenza

        Time Complexity:
            O(log n) in cui n si intende il numero di nodi dell'Heap.
            In questo caso è log perché si esegue una traversata verticale
            evitando potenziali nodi superflui. 

        Returns:
            int: Il numero di livelli
        """
        currentNode:Node = startingNode
        levels:int = 1
        while currentNode.parentNode != None:
            currentNode = currentNode.parentNode
            levels+=1
        
        return levels

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

    def extractNode(self, node:Node)->Node:
        parentNode:Node = node.parentNode
        
        
        return node

    def getChildNodeProvenience(self, node:Node, parentNode:Node)->bool:
        result:bool = None

        if parentNode.leftChild!=None and node.nodeValue == parentNode.leftChild.nodeValue:
            result = True
        elif parentNode.rightChild!=None and node.nodeValue == parentNode.rightChild.nodeValue:
            result = False

        return result

    def heapSort(self)->list[Node]:
        result:list[Node] = []
        
        while len(self.rawNodes)>0:
            result.append(self.heapPop())
        
        return result

    def heapPop(self)->Node:
        """
        This method swap the max node with the min node and then removes it
        it also calls max_heapify to check for the rep invariant compliance
        
        Time Complexity:
            O(log n) -> Because it calls the max_heapify when done. 
                        The other instructions are O(1)
                        
        Returns:
            Node: The max node
        """
        
        # Basecase: se c'è solo 1 elemento rimuovilo direttamente
        if self.nodesLength == 1:
            return self.rawNodes.pop()
        
        # Trovo il nodo root O(1)
        maxNodeValue:int = self.nodeRoot.nodeValue
        
        # Scambio il nodo massimo con l'ultimo nodo
        lastNodeIndex:int = self.nodesLength-1
        lastNode:Node = self.rawNodes[lastNodeIndex]
        
        lastNodeValue:int = lastNode.nodeValue
        self.nodeRoot.nodeValue = lastNodeValue
        lastNode.nodeValue = maxNodeValue
        
        # Rimuovo il nodo
        parentNode:Node = lastNode.parentNode
        provenience:bool = self.getChildNodeProvenience(lastNode, parentNode)
        assert provenience != None
        if provenience==True:
            #left child
           parentNode.leftChild = None
        elif provenience ==False:
            #right child
            parentNode.rightChild = None  
        
        nodeToDel:Node = self.rawNodes.pop(lastNodeIndex)
                
        # Richiamo max heapify sull'elemento per verificare che non violi la rep invariant
        self.maxHeapify(self.nodeRoot)
        self.nodesLength-=1
        # Ripeto per N volte
        print("------------------------------------------------------")
        self.printValues()
        print("------------------------------------------------------")
        return nodeToDel

    # Rep invariant
    def maxHeapify(self, node:Node)->None:
        """
        Questo metodo fixa una violazione di una rep invariant 
        per un nodo e i suoi 2 figli

        Time Complexity: 
            O(log n) -> in quanto al massimo bisognerà far scendere un elemento fino alla fine.

        Args:
            node (Node): Il nodo di partenza
        """
        left:Node = node.leftChild
        right:Node = node.rightChild
        largest:Node = node
        changed:bool = None
        
        if left != None and left.nodeValue <= self.nodesLength and left.nodeValue > node.nodeValue and ( right==None or left.nodeValue > right.nodeValue):
            # violazione rilevata, il nuovo elemento maggiore è il sinistro
            largest = left
            changed = True
            
        if right != None and right.nodeValue <= self.nodesLength and right.nodeValue > node.nodeValue and (left==None or right.nodeValue > left.nodeValue):
            # violazione rilevata, il nuovo elemento maggiore è il sinistro
            largest = right
            changed = False
            
        if largest != node:
            tmp:int = node.nodeValue
            node.nodeValue = largest.nodeValue
            
            if changed == True:
                node.leftChild.nodeValue = tmp
                # Left
            else:
                node.rightChild.nodeValue = tmp
                # Right
            self.maxHeapify(largest)
        
        pass

    def buildMaxHeap(self)->None:
        index:int = (self.nodesLength // 2) -1
        
        while index>=0:
            self.maxHeapify(self.rawNodes[index])
            index -= 1
        
        pass

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
