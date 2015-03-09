#!/bin/python3

with open('words.txt') as f:
    words = [line.strip() for line in f]

print(', '.join(words))
