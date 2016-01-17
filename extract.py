#!/usr/bin/python3
import re

gender = (re.compile('({[m|f|n]})'), '')
brackets = (re.compile('(?:[\[<(])(.+)(?:[\]>)])'), '')

invalidChars = ' -?!0123456789:.\'"'

def prepare(word):
    ''' Strips unnecessary stuff from the given word.
        Returns None for unwanted words (like "Miene machen, etw. zu tun")

        Example:
        1) Hochpassfilter_{m}_[fachspr._meist_{n}]_<HPF>
        2) Hochpassfilter__[fachspr._meist_]_<HPF>
        3) Hochpassfilter___
        4) Hochpassfilter
    '''
    word = gender[0].sub(gender[1], word)
    word = brackets[0].sub(brackets[1], word)
    word = word.strip()
    for char in invalidChars:
        if char in word:
            return None
    return word

def read_dict(filename):
    words = set()
    i = 0
    with open(filename, 'rb') as f:
        while True:
            i += 1
            line = f.readline()
            if not line:
                break
            line = line.strip(b'\r\n')
            if not line or line.startswith(b'#'):
                continue
            word = line.split(b'\t')[0]
            try:
                word = word.decode()
            except UnicodeError as e:
                raise
            word = prepare(word)
            if not word:
                continue
            words.add(word)
    return words

def main():
    words = list(sorted(read_dict('dict.cc.txt')))

    with open('words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')

    print('Successfully extracted {} words!'.format(len(words)))

if __name__ == '__main__':
    main()
