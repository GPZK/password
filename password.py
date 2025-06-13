import argparse
import random

letters = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
symbols = list('\\\'~`! @#$%^&*()_-+={[}]|:;"<,>.?/')
numbers = list('0123456789')
elementPool = list(letters)
password = []

parser = argparse.ArgumentParser()
parser.add_argument('length', help='type the number of symbols in your desired password', type=int)
parser.add_argument('-s', help = 'type this to include special symbols', action = 'store_true')
parser.add_argument('-n', help = 'type this to include numbers', action = 'store_true')
args = parser.parse_args()

if (args.s):
    elementPool.extend(symbols)
if (args.n):
    elementPool.extend(numbers)

for i in range(0, args.length):
    elem = random.randint(0, len(elementPool)-1)
    password.append(elementPool[elem])

print(''.join(str(el) for el in password))



