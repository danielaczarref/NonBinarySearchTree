import re

class Node:
    def __init__ (self, data):
        self.vowels = None
        self.consonants = None
        self.odds = None
        self.evens = None
        self.data = data

class Tree:

    nonDigitPattern = "[^0-9]"
    integerPattern = "[0-9]+"

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
            if (value in ["a", "e", "i", "o", "u"]):
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
            node.vowels = Node(value)
        elif (newValue == self.CONSONANT):
            node.consonants = Node(value)
        elif (newValue == self.ODD):
            node.odds = Node(value)
        elif (newValue == self.EVEN):
            node.evens = Node(value)

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
        elif (newValue == self.VOWEL):
            self._search(value, node.vowels)
        elif (newValue == self.CONSONANT):
            self._search(value, node.consonants)
        elif (newValue == self.ODD):
            self._search(value, node.odds)
        elif (newValue == self.EVEN):
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
a.add('c7f55e08-9347-11eb-a8b3-0242ac130003')
a.add('369c68e1-3c04-4d83-80b4-92dc430938d1')
a.add('019f73e2-c67e-4e70-ad2a-c71440f8d4ef')
a.add('e07dc30d-e588-4d40-bb6a-11a4465ef7f1')
a.add('d723ce63-0b72-448c-a4e7-173fc20ac470')
a.add('03fefc36-c6f8-44b7-983c-43acc0be008a')
a.add('75d374e0-2e02-41af-a5e6-5eec4a402355')