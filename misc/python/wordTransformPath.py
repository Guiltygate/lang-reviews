'''
    Python 2.7 (using Queue)

    Given
        String beginWord
        String endWord
        ??? wordDictionary
    find the shortest lexigraphical path to transform beginWord into endWord, using only words
    found in the dictionary.

    Assuming no spaces, alpha only, and words are same length (for now).
'''

import json
import string
from Queue import Queue



class WordGraph:
    '''  Graphs words from a given dictionary of a given size. Does not support deletion.
            nodes (dict of Nodes)
            dictionary (dict of strings)
            wordLength (int)
    '''
    nodes = None
    #could use a dictionary parallel to the list if space was not an issue, for faster lookup when using findPath
    dictionary = None
    wordLength = 0


    def __init__( self ,dictionary ,wordLength):
        ''' dictionary (strings) & wordLength (int) (length of words to be graphed)'''

        self.dictionary = dictionary
        self.wordLength = wordLength
        self.nodes = []

        self.build()


    def build( self):
        count = 0
        for word in self.dictionary:
            if len( word) == self.wordLength:
                self._add( word)
            elif len( word) == 5:
                count += 1
        print( count)


    def _add( self ,textWord):
        ''' Add new Node to Graph.
            The options were to cycle through each word in dictionary (in this case, 500k)
            or cycle through each letter of the new word a-z (so 25^n).
            Given scaling issues, the dictionary cycle seems most efficient (although still not great)

            Does not screen additions!
        '''
        newWord = self.Node( textWord)
        for wordNode in self.nodes:
            wordNode.updateNeighbors( newWord)
        
        self.nodes.append( newWord)


    
    def findPath( self ,beginWord ,endWord):
        ''' Find path between two words, where each link is a one-character difference.
            Using BFS '''

        startNode = -1
        endNode = -1
        
        for node in self.nodes:
            if node.equals( beginWord):
                startNode = node
            elif node.equals( endWord):
                endNode = node
        
        if( startNode == -1 or endNode == -1):
            return []

        nodesToVisit = Queue()
        nodesToVisit.put( startNode)
        path = []

        while( True):
            if nodesToVisit.empty():
                break
            
            currentNode = nodesToVisit.get( False)

            if currentNode.equals( endNode):
                while( True):
                    path.append( currentNode.getWord())
                    if currentNode == startNode:
                        break
                    
                    currentNode = currentNode.getParent()
                    

            for neighbor in currentNode.getNeighbors():
                if( not neighbor.hasBeenVisited()):
                    neighbor.setParent( currentNode)
                    nodesToVisit.put( neighbor)

            
        self.resetNodes()    
        

        return path


    def resetNodes( self):
        for node in self.nodes:
            node.setParent( False)


       
        


    class Node:
        ''' Node in WordGraph. Represents a string word.
            word (string)
            chars (list of chars):   list of chars in word, used for comparison
            wordLength (int)
            neighbors (list of Nodes)
            parent ( Node)
        '''
        word = ""
        chars = None
        wordLength = 0
        neighbors = None
        parent = False

        def __init__( self ,wordData):
            self.word = wordData
            self.chars = list( wordData)
            self.wordLength = len( wordData)
            self.neighbors = []


        def getChar( self ,index):
            return self.chars[ index]

        def getWord( self):
            return self.word

        def equals( self ,word):
            if isinstance( word ,str):
                return self.getWord() == word
            elif isinstance( word ,self.__class__):
                return self.getWord() == word.getWord()
            else:
                return False
            

        def isNeighbor( self ,node):
            differences = 0
            for i in range( self.wordLength):
                if self.getChar(i) != node.getChar( i):
                    differences += 1
                
                if differences > 1:
                    return False

            return True

        def hasBeenVisited( self):
            return not( self.parent == False)

        def hasParent( self):
            return self.parent

        def setParent( self ,node):
            self.parent = node

        def getParent( self):
            return self.parent

        def addNeighbor( self ,newNeighborNode):
            self.neighbors.append( newNeighborNode)

        def getNeighbors( self):
            return self.neighbors

        def updateNeighbors( self ,potentialNeighbor):
            if( self.isNeighbor( potentialNeighbor)):
                self.addNeighbor( potentialNeighbor)
                potentialNeighbor.addNeighbor( self)








def readDictionary():
    with open( '../../resources/words_dictionary.json' ,'r') as f:
        dictionary = json.load( f)
        f.close()
    
    return dictionary





dictionary = readDictionary()

wordGraph3 = WordGraph( dictionary ,3)
print( wordGraph3.findPath( 'cat' ,'dog'))
# print( wordGraph3.findPath('cog' ,'hog') )
# print( wordGraph3.findPath('cog' ,'sun') )

# wordGraph4 = WordGraph( dictionary ,4)
# print( wordGraph4.findPath( 'lark' ,'lake') )

# wordGraph5 = WordGraph( dictionary ,5)
# print( wordGraph5.findPath( 'hello' ,'sunny') )


# wordGraph9 = WordGraph( dictionary ,9)
# print( wordGraph9.findPath( 'conscious' ,'planetary') )

