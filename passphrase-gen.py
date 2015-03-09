#!/bin/python3
import argparse, random

def parse_args():
    parser = argparse.ArgumentParser(
            description=
            'Generate a passphrase with random words'
            'out of a dictionary.')
    parser.add_argument('-f', '--file', type=str, default='words.txt',
            help='file where the words are, seperated by newlines')
    parser.add_argument('-n', '--words', type=int, default=5,
            help='amount of words to include in the passphrase')
    parser.add_argument('-c', '--count', type=int, default=15,
            help='amount of passphrases to generate')
    return parser.parse_args()

def read_words(filename):
    with open(filename) as f:
        words = [line.strip() for line in f]
    return words

def generate_passphrase_words(vocabulary, numWords):
    choice = random.SystemRandom().choice
    return [choice(vocabulary) for _ in range(numWords)]

def show_passphrase(words):
    print(' '.join(words))

def main():
    args = parse_args()
    words = read_words(args.file)

    passphrases = [generate_passphrase_words(words, args.words) for _ in range(args.count)]
    for passphrase in passphrases:
        show_passphrase(passphrase)

    #todo: print time to guess at 1000 guesses/sec


if __name__ == '__main__':
    main()
