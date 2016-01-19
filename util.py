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
