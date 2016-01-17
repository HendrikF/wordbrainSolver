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

def contains(word, wordList):
	'''	Looks for word in wordList and returns word with the case of wordList
	'''
	word = word.lower()
	for w in wordList:
		if word == w.lower():
			return w
	return False

def solve(words, matrix, x = 0, y = 0, wordUntilNow = '', closedPath = []):
	if (x, y) in closedPath:
		return []
	if not (0 <= y < len(matrix) and 0 <= x < len(matrix[y])):
		return []
	solutions = []
	currentWord = wordUntilNow + matrix[y][x]
	word = contains(currentWord, words)
	if word:
		print(word)
		solutions.append(word)
	closedPath.append((x, y))
	
	solutions.extend(solve(words, matrix, x + 1, y    , currentWord, closedPath))
	solutions.extend(solve(words, matrix, x + 1, y + 1, currentWord, closedPath))
	solutions.extend(solve(words, matrix, x    , y + 1, currentWord, closedPath))
	solutions.extend(solve(words, matrix, x - 1, y + 1, currentWord, closedPath))
	solutions.extend(solve(words, matrix, x - 1, y    , currentWord, closedPath))
	solutions.extend(solve(words, matrix, x - 1, y - 1, currentWord, closedPath))
	solutions.extend(solve(words, matrix, x    , y - 1, currentWord, closedPath))
	solutions.extend(solve(words, matrix, x + 1, y - 1, currentWord, closedPath))

	closedPath.remove((x, y))

	return solutions

def main():
	start = time()

	words = readWords('words.txt')

	matrix = readMatrix()

	print('Starting to solve... (This may take a while...)')

	solutions = []
	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			solutions.extend(solve(words, matrix, x, y))

	# filter and sort
	solutions = list(sorted(set(solutions), key = lambda word: word.lower()))

	print('Found {} solutions in {} seconds'.format(len(solutions), time() - start))
	for word in solutions:
		print(word)

if __name__ == '__main__':
	main()
