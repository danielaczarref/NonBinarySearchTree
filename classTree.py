import re
from classNode import Node

class Tree:

    nonDigitPattern = "[^0-9]"
    integerPattern = "[0-9]+"
    vowelsArray = ["a", "e", "i", "o", "u"]

    VOWEL = "vowel"
    CONSONANT = "consonant"
    ODD = "odd"
    EVEN = "even"

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if (self.root == None):
            self.root = Node(value)
        else:
            self._add(value, self.root)
    
    def valueType(self, value):
        if (re.match(self.nonDigitPattern, value)):
            if (value in self.vowelsArray):
                return self.VOWEL
            else:
                return self.CONSONANT
        elif (re.match(self.integerPattern, value)):
            if (int(value) % 2) == 0:
                return self.EVEN
            else:
                return self.ODD
    
    def _add(self, value, node):
        cleanString = re.sub("\W+", "", value)
        newValue = self.valueType((cleanString[0]))
        if (newValue == self.VOWEL):
            if (node.vowels == None):
                node.vowels = Node(value)
            else:
                self._add(value, node.vowels)
        elif (newValue == self.CONSONANT):
            if (node.consonants != None):
                self._add(value, node.consonants)
            else:     
                node.consonants = Node(value)
        elif (newValue == self.ODD):
            if (node.odds != None):
                self._add(value, node.odds)
            else:
                node.odds = Node(value)
        elif (newValue == self.EVEN):
            if (node.evens != None):
                self._add(value, node.evens)
            else:
                node.evens = Node(value)    

    def addFromFile(self, filePath):
        lines = []
        with open(filePath) as f:
            lines = f.readlines()
        for line in lines:
            if (line != None):
                a.add(str(line))

    def search(self, value):
        if (self.root != None):
            return self._search(value, self.root)
        else:
            return None
    
    def _search(self, value, node):
        cleanString = re.sub(r"\W+", "", value)
        cleanAux = re.sub(r"\W+", "", node.data)
        newValue = self.valueType(cleanString[0])
        if (cleanString == cleanAux):
            return print("found it: " + node.data)
        elif (newValue == self.VOWEL and node.vowels != None):
            self._search(value, node.vowels)
        elif (newValue == self.CONSONANT and node.consonants != None):
            self._search(value, node.consonants)
        elif (newValue == self.ODD and node.odds != None):
            self._search(value, node.odds)                    
        elif (newValue == self.EVEN and node.evens != None):
            self._search(value, node.evens)
        else:
            return print(value, ': 404 - Not found')

    def order(self):
        if (self.root != None):
            self._order(self.root)

    def _order(self, node):
        if (node != None):
            print(node.data)
            self._order(node.evens)
            self._order(node.odds)
            self._order(node.vowels)
            self._order(node.consonants)

a = Tree()
a.addFromFile('v4_uuids(1).txt')
a.order()
