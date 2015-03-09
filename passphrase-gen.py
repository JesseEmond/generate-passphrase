#!/bin/python3
import argparse

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
args = parser.parse_args()

with open(args.file) as f:
    words = [line.strip() for line in f]

print(', '.join(words))
