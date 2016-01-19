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

def readMatrix():
    matrix = []
    print('Please enter the characters of each line (. = End)')
    while True:
        text = input()
        if text == '.':
            break
        matrix.append(text)
    return matrix

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
