#!/usr/bin/env python3
__author__ = 'olukaemma'
'''Sinmple payrole script'''
def logic():
    '''using a function to acomplish the same task'''
    hoursworked = int(input('Enter hours worked: '))
    rate = int(input('Enter the hourly rate: '))

    if hoursworked > 40:
        print('Gross pay: '+ str((40 * rate) + ((hoursworked - 40) * (rate * 1.5))))
    elif hoursworked <=40:
        print('Gross pay: '+ str(hoursworked * rate))

logic()
