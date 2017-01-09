#!/usr/bin/env python3
__author__ = 'Emmanuel Oluka'

__doc__
'''
This is just a simple program to test a few new ideas
The program is writen by Emmanuel and with the help of other resources
'''

#main function
name = input('Please tell me your name: ')
age = int(input('Please tell us your age: '))

if age >=20:
    print(name, 'you are allowed in!')
    print('What would your like to drink?')
elif age >=18 and age < 20:
    print(name, 'you are allowed in!')
    print('But you are not allowed to drink, please enjoy the dance')
else:
    print(name, 'unfortunatly, you are not allowed in')
