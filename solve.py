#!/usr/bin/python3
from datetime import datetime
import multiprocessing
from util import readMatrix, readBoundaries, WordList, Matrix

def solve(wordList, matrix, x, y, boundaries, wordUntilNow = '', closedPath = []):
    closedPath.append((x, y))
    
    solutions = []
    
    currentWord = wordUntilNow + matrix.get(x, y)
    
    if boundaries[0] <= len(currentWord) <= boundaries[1]:
        word = wordList.check(currentWord)
        if word:
            print(word)
            solutions.append(word)
    
    if len(currentWord) <= boundaries[1]:
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == dy == 0:
                    continue
                newx = x + dx
                newy = y + dy
                if (newx, newy) in closedPath:
                    continue
                if not (0 <= newy < matrix.height and 0 <= newx < matrix.width):
                    continue
                if matrix.get(newx, newy) == '':
                    continue
                solutions.extend(solve(wordList, matrix, newx, newy, boundaries, currentWord, closedPath))
    
    closedPath.remove((x, y))

    return solutions

def main():
    print('WORDBRAIN solver')
    
    try:
        CORES = multiprocessing.cpu_count()
    except NotImplementedError as e:
        CORES = 4
        print('Could not determine CPU count. Assuming {} cores'.format(CORES))
    
    print('Running on {} cores!'.format(CORES))
    
    matrix = Matrix(readMatrix())
    
    boundaries = readBoundaries()
    
    wordList = WordList(matrix, boundaries)
    wordList.readFromFile('words.txt')
    
    start = datetime.now()
    
    print('Starting to solve... (This may take a while...)')
    print('Press CTRL-C to cancel')
    
    solutions = []
    args = []
    for y in range(matrix.height):
        for x in range(matrix.width):
            args.append((wordList, matrix, x, y, boundaries))
    
    with multiprocessing.Pool(CORES) as pool:
        for arr in pool.starmap(solve, args):
            solutions.extend(arr)
    
    # filter and sort
    solutions = list(sorted(set(solutions), key = lambda word: str(len(word)) + word.lower()))
    
    print('Found {} possible solutions in {}:'.format(len(solutions), datetime.now() - start))
    for word in solutions:
        print(word)

if __name__ == '__main__':
    main()
