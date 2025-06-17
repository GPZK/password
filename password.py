import argparse
import random


element_pool = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
symbols_list = list('\\\'~`!@#$%^&*()_-+={[}]|:;"<,>.?/')
numbers_list = list('0123456789')
length = 0

def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', help = 'type the number of symbols in your desired password', type=int)
    parser.add_argument('-s', help = 'type this to include special symbols', action = 'store_true')
    parser.add_argument('-n', help = 'type this to include numbers', action = 'store_true')
    return parser

def parse_param(parser):
    args = parser.parse_args()
    s = args.s
    n = args.n
    length = args.length
    return s, n, length

def generatePassword(s, n, len):
    if s:
        element_pool.extend(symbols_list)
    if n:
        element_pool.extend(numbers_list)
    password = ''.join(random.choices(element_pool, k = len))
    return password

if __name__ ==  '__main__':
    parser = setup_parser()
    symbols, numbers, length = parse_param(parser)
    print(generatePassword(symbols, numbers, length))