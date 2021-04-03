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
            self.addInVowels(value, node)
        elif (newValue == self.CONSONANT):
            if (node.consonants != None):
                self._add(value, node.consonants)
            else:
                node.consonants = Node(value)
        elif (newValue == self.ODD):
            self.addInOdds(value, node)
        elif (newValue == self.EVEN):
            self.addInEvens(value, node)
    
    def addInVowels(self, value, node):
        cleanString = re.sub("\W+", "", value)
        if (node.vowels != None):
            if (cleanString[0] == self.vowelsArray[0]):
                node.a = Node(value)
            elif (cleanString[0] == self.vowelsArray[1]):
                node.e = Node(value)
            elif (cleanString[0] == self.vowelsArray[2]):
                node.i = Node(value)
            elif (cleanString[0] == self.vowelsArray[3]):
                node.o = Node(value)
            elif (cleanString[0] == self.vowelsArray[4]):
                node.u = Node(value)
        else:
            node.vowels = Node(value)
    
    def addInOdds(self, value, node):
        cleanString = re.sub("\W+", "", value)
        auxString = re.sub("\W+", "", node.data)
        if (node.odds != None):
            if (int(cleanString[0]) < int(auxString[0])):
                if (node.left != None):
                    self._add(value, node.left)
                else:
                    node.left = Node(value)
            else:
                if (node.right != None):
                    self._add(value, node.right)
                else:
                    node.right = Node(value)
        else:
            node.odds = Node(value)

    def addInEvens(self, value, node):
        cleanString = re.sub("\W+", "", value)
        auxString = re.sub("\W+", "", node.data)
        if (node.evens != None):
            if (int(cleanString[0]) < int(auxString[0])):
                if (node.left != None):
                    self._add(value, node.left)
                else:
                    node.left = Node(value)
            else:
                if (node.right != None):
                    self._add(value, node.right)
                else:
                    node.right = Node(value)
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
        cleanString = re.sub("\W+", "", value)
        newValue = self.valueType(cleanString[0])
        if (value == node.data):
            return print(node.data)
        elif (newValue == self.VOWEL and node.vowels != None):
            self._search(value, node.vowels)
        elif (newValue == self.CONSONANT and node.consonants != None):
            print('eh consoante')
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
#a.order()
