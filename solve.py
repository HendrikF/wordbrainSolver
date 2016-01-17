#!/usr/bin/python3
from time import time

def readWords(filename):
    words = []
    with open(filename) as f:
        for line in f:
            words.append(line.strip())
    return words

def readMatrix():
    matrix = []
    print('Please enter the characters of each line (. = End)')
    while True:
        text = input()
        if text == '.':
            break
        matrix.append(text)
    return matrix

def contains(word, words, wordsLower):
    ''' Looks for word in wordsLower and returns word with the case of words
    '''
    word = word.lower()
    if word in wordsLower:
        for w in words:
            if word == w.lower():
                return w
    return False

def solve(words, wordsLower, matrix, x = 0, y = 0, wordUntilNow = '', closedPath = []):
    if (x, y) in closedPath:
        return []
    if not (0 <= y < len(matrix) and 0 <= x < len(matrix[y])):
        return []
    closedPath.append((x, y))
    
    solutions = []
    
    currentWord = wordUntilNow + matrix[y][x]
    
    word = contains(currentWord, words, wordsLower)
    if word:
        print(word)
        solutions.append(word)
    
    solutions.extend(solve(words, wordsLower, matrix, x + 1, y    , currentWord, closedPath))
    solutions.extend(solve(words, wordsLower, matrix, x + 1, y + 1, currentWord, closedPath))
    solutions.extend(solve(words, wordsLower, matrix, x    , y + 1, currentWord, closedPath))
    solutions.extend(solve(words, wordsLower, matrix, x - 1, y + 1, currentWord, closedPath))
    solutions.extend(solve(words, wordsLower, matrix, x - 1, y    , currentWord, closedPath))
    solutions.extend(solve(words, wordsLower, matrix, x - 1, y - 1, currentWord, closedPath))
    solutions.extend(solve(words, wordsLower, matrix, x    , y - 1, currentWord, closedPath))
    solutions.extend(solve(words, wordsLower, matrix, x + 1, y - 1, currentWord, closedPath))

    closedPath.remove((x, y))

    return solutions

def main():
    start = time()

    words = readWords('words.txt')
    wordsLower = [word.lower() for word in words]

    matrix = readMatrix()

    print('Starting to solve... (This may take a while...)')
    print('Press CTRL-C to cancel')

    solutions = []
    try:
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                solutions.extend(solve(words, wordsLower, matrix, x, y))
        
        # filter and sort
        solutions = list(sorted(set(solutions), key = lambda word: str(len(word)) + word.lower()))
    except KeyboardInterrupt as e:
        print('Canceled')

    print('Found {} possible solutions in {} seconds:'.format(len(solutions), time() - start))
    for word in solutions:
        print(word)

if __name__ == '__main__':
    main()
