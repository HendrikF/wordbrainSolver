#!/usr/bin/python3
from datetime import datetime
from multiprocessing import Pool
from util import readWords, readMatrix, readBoundaries

def contains(word, words, wordsLower):
    ''' Looks for word in wordsLower and returns word with the case of words
    '''
    word = word.lower()
    if word in wordsLower:
        for w in words:
            if word == w.lower():
                return w
    return False

def solve(words, wordsLower, matrix, x = 0, y = 0, boundaries = (0, 0), wordUntilNow = '', closedPath = []):
    closedPath.append((x, y))
    
    solutions = []
    
    currentWord = wordUntilNow + matrix[y][x]
    
    if boundaries[0] <= len(currentWord) <= boundaries[1]:
        word = contains(currentWord, words, wordsLower)
        if word:
            print(word)
            solutions.append(word)
    
    if len(currentWord) <= boundaries[1]:
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == dy == 0:
                    continue
                if (x + dx, y + dy) in closedPath:
                    continue
                if not (0 <= y + dy < len(matrix) and 0 <= x + dx < len(matrix[y + dy])):
                    continue
                solutions.extend(solve(words, wordsLower, matrix, x + dx, y + dy, boundaries, currentWord, closedPath))
    
    closedPath.remove((x, y))

    return solutions

def main():
    CORES = 4
    
    words = readWords('words.txt')
    wordsLower = [word.lower() for word in words]
    
    print('WORDBRAIN solver')
    print('Running on {} cores!'.format(CORES))
    
    matrix = readMatrix()
    
    boundaries = readBoundaries()
    
    start = datetime.now()

    print('Starting to solve... (This may take a while...)')
    print('Press CTRL-C to cancel')
    
    solutions = []
    args = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            args.append((words, wordsLower, matrix, x, y, boundaries))
    
    try:
        with Pool(CORES) as pool:
            for arr in pool.starmap(solve, args):
                solutions.extend(arr)
        
        # filter and sort
        solutions = list(sorted(set(solutions), key = lambda word: str(len(word)) + word.lower()))
    except KeyboardInterrupt as e:
        print('Canceled')

    print('Found {} possible solutions in {}:'.format(len(solutions), datetime.now() - start))
    for word in solutions:
        print(word)

if __name__ == '__main__':
    main()
