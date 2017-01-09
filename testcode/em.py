#!/usr/bin/env python3
__author__ = 'Emmanuel Oluka'
'''
computing fibonacci number using argparse on the commandline
Date: 06/01/2016
'''
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-V', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('num', help='The fibonacci number you wish to calculate', type=int)
    parser.add_argument('-o', '--output', help='Output results to a file.', \
                         action='store_true')
    args = parser.parse_args()

    result  = fib(args.num)

    if args.verbose:
         print('The '+ str(args.num)+ ' fibonacci number is '+str(result))
    elif args.quiet:
        print(result)
    else:
        print('Fib ('+str(args.num)+') = '+str(result))
    if args.output:
        f = open('/Users/olukaemma/PycharmProjects/ioluka/testcode/fibonacci.txt', 'a')
        f.write(str(result)+'\n')


if __name__=='__main__':
    Main()
