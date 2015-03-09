#!/bin/python
import argparse, random, math

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
    parser.add_argument('--clean', action='store_true',
            help='clean output with only generated passphrases')
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

def show_guess_time(vocabularySize, numWords):
    guessSpeed = 1000 # guesses/sec

    # time required = totalPossibilities / speed
    #               = (vocabSize ^ numWords) / speed
    # ln(time)      = ln( vocabSize ^ numWords / speed )
    #               = numWords * ln(vocabSize) - ln(speed)
    # time          = e ^ (numWords * ln(vocabSize) - ln(speed))
    time = math.exp(numWords * math.log(vocabularySize) - math.log(guessSpeed))

    minutes = time / 60
    hours = minutes / 60
    days = hours / 24

    print()
    print("Passphrase would take {:.2f} days to bruteforce "
          "at {} guesses per second.".format(days, guessSpeed))


def main():
    args = parse_args()
    words = read_words(args.file)

    passphrases = [generate_passphrase_words(words, args.words) for _ in range(args.count)]
    for passphrase in passphrases:
        show_passphrase(passphrase)

    if not args.clean:
        show_guess_time(len(words), args.words)

if __name__ == '__main__':
    main()
