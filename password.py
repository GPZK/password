import argparse
import random


element_pool = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
symbols = list('\\\'~`! @#$%^&*()_-+={[}]|:;"<,>.?/')
numbers = list('0123456789')
length = 0

def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', help='type the number of symbols in your desired password', type=int)
    parser.add_argument('-s', help = 'type this to include special symbols', action = 'store_true')
    parser.add_argument('-n', help = 'type this to include numbers', action = 'store_true')
    return parser

def parse_param(parser):
    args = parser.parse_args()
    return args

def generatePassword(args):
    if (args.s):
        element_pool.extend(symbols)
    if (args.n):
        element_pool.extend(numbers)
    password = ''.join(random.choices(element_pool, k = args.length))
    return password

if __name__ ==  '__main__':
    parser = setup_parser()
    args = parse_param(parser)
    print(generatePassword(args))