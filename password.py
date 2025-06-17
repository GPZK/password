import argparse
import random


elementPool = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
length = 0

def parseParam():
    global length
    symbols = list('\\\'~`! @#$%^&*()_-+={[}]|:;"<,>.?/')
    numbers = list('0123456789')

    parser = argparse.ArgumentParser()
    parser.add_argument('length', help='type the number of symbols in your desired password', type=int)
    parser.add_argument('-s', help = 'type this to include special symbols', action = 'store_true')
    parser.add_argument('-n', help = 'type this to include numbers', action = 'store_true')
    args = parser.parse_args()

    if (args.s):
        elementPool.extend(symbols)
    if (args.n):
        elementPool.extend(numbers)
    length = args.length

def generatePassword(pool, len):
    password = ''.join(random.choices(pool, k = len))
    return password

if __name__ ==  '__main__':
    parseParam()
    print(generatePassword(elementPool, length))