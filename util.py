import copy

class WordList:
    def __init__(self, boundaries = None):
        self.boundaries = boundaries
        self.words = {}
        self.wordsLower = {}
    
    def add(self, word):
        if not word:
            return
        if self.boundaries is not None:
            if not (self.boundaries[0] <= len(word) <= self.boundaries[1]):
                return
        self.words.setdefault(word[0].lower(), []).append(word)
        self.wordsLower.setdefault(word[0].lower(), []).append(word.lower())
    
    def check(self, word):
        first = word[0].lower()
        if word.lower() in self.wordsLower.setdefault(first, []):
            for w in self.words.setdefault(first, []):
                if w.lower() == word.lower():
                    return w
        return None
    
    def readFromFile(self, filename):
        with open(filename) as f:
            for line in f:
                self.add(line.strip())

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.calcSize()
        self.gravity()
    
    def calcSize(self):
        self._height = len(self.matrix)
        self._width = len(self.matrix[0]) if self._height else 0
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def __repr__(self):
        return '\n'.join([''.join([c.upper() if c else ' ' for c in row]) for row in self.matrix])
    
    def __bool__(self):
        return len(self.matrix) > 0
    
    def get(self, x, y):
        return self.matrix[y][x]
    
    def remove(self, positions):
        newMatrix = copy.deepcopy(self.matrix)
        for position in positions:
            newMatrix[position[1]][position[0]] = ''
        newMatrix.gravity()
        return newMatrix
    
    def gravity(self):
        for y in range(self.height-2, -1, -1):
            for x in range(self.width):
                if not self.matrix[y][x]:
                    # nothing to push down
                    continue
                if self.matrix[y + 1][x]:
                    # is on ground
                    continue
                # let current character fall down
                y_ = y
                char = self.matrix[y_][x]
                self.matrix[y_][x] = ''
                while y_ < self.height - 1 and not self.matrix[y_ + 1][x]:
                    y_ += 1
                self.matrix[y_][x] = char
        
        self.trim()
    
    def trim(self):
        # if we have a matrix
        if self.matrix:
            # remove empty lines at the beginning
            while True:
                if not self.matrix:
                    break
                firstLineIsEmpty = True
                for char in self.matrix[0]:
                    if char:
                        firstLineIsEmpty = False
                        break
                if firstLineIsEmpty:
                    self.matrix = self.matrix[1:]
                else:
                    break
            
            # remove empty columns at the beginning
            while True:
                if not self.matrix or not self.matrix[0]:
                    break
                # we assume that gravity has been called before
                # so we only have to check the last line for characters
                if not self.matrix[len(self.matrix)-1][0]:
                    for y in range(len(self.matrix)):
                        self.matrix[y] = self.matrix[y][1:]
                else:
                    break
            
            # remove empty columns at the end
            while True:
                if not self.matrix or not self.matrix[0]:
                    break
                # we assume that gravity has been called before
                # so we only have to check the last line for characters
                if not self.matrix[len(self.matrix)-1][len(self.matrix[0])-1]:
                    for y in range(len(self.matrix)):
                        self.matrix[y] = self.matrix[y][:-1]
                else:
                    break
        
        self.calcSize()

def readMatrix():
    print('Please enter the characters of each line (. = End, Space for Space)')
    # (['ab', 'cd'])
    textMatrix = []
    while True:
        text = input()
        if text == '.':
            break
        textMatrix.append(text)
    # look for max width, so that we can create a square matrix
    maxwidth = 0
    for y in range(len(textMatrix)):
        maxwidth = max(maxwidth, len(textMatrix[y]))
    # create list matrix ([['a', 'b'], ['c', 'd']])
    listMatrix = []
    for y in range(len(textMatrix)):
        row = [''] * maxwidth
        listMatrix.append(row)
        for x in range(len(textMatrix[y])):
            if textMatrix[y][x] == ' ':
                continue
            listMatrix[y][x] = textMatrix[y][x]
    return listMatrix

def readBoundaries():
    while True:
        try:
            minimum = int(input('Minimum length: '))
        except ValueError as e:
            print('Please enter a number!')
        else:
            break
    while True:
        try:
            maximum = int(input('Maximum length: '))
        except ValueError as e:
            print('Please enter a number!')
        else:
            break
    if minimum > maximum:
        print('Swapping values!')
        return (maximum, minimum)
    return (minimum, maximum)
