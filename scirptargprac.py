import sys
from mspack.math import *


def process_comand(*agrs):
    command = agrs[0]
    x = int(agrs[1])
    y = int(agrs[2])

    if command == 'sum':
        print('Summation is: ', sum(x, y))
    elif command == 'sub':
        print('Subtraction is: ', sub(x, y))
    elif command == 'mul':
        print('Multiplication is: ', mul(x, y))
    elif command == 'div':
        print('Division is: ', div(x, y))
    elif command == 'mod':
        print('Modulus is: ', mod(x, y))
    elif command == 'power':
        print('Power is: ', power(x, y))


if len(sys.argv) >= 4:
    command = sys.argv[1].lower()
    x = sys.argv[2]
    y = sys.argv[3]

    try:
        process_comand(command,x,y)
    except Exception as e:
        print('Exception is: ',e)
else:
    print('command is not sufficient')
