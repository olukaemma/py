#!/usr/bin/env python3
__author__ = 'Emmanuel Oluka'

'''
Sampla python code
'''

#script to test a few things around
import os, sys
from urllib import request as URL, parse as PA, error as ERR

##we will attempt to connect to the internet and retrive some web content, then write it to a file
myWeb = 'http://finance.yahoo.com/market-overview/'

try:
    os.chdir('/Volumes/Untitled/')
    #os.mkdir('output')
    os.chdir('output')
    for i in URL.urlopen(myWeb).readlines():
        myFile = open('output.html','a').writelines(str(i))
except ERR.URLError as e:
    print(e)
finally:
    print('completed')

try:
    a = int(input('Enter your first number: '))
    b = int(input('Enter your second number: '))
    print('Your result of ',a,'/',b,' is', a/b)
except (ZeroDivisionError, ValueError, TypeError) as e:
    print('Error : ', e)

def devlog(x,y):
    try:
        f = open('/Volumes/Untitled/output/mytext.txt','a')
        f.write('{0:g} / {1:g} = {2:g}\n'.format(x, y, (x/y)))
    except ZeroDivisionError as e:
        f.write('Error: Zeror is not divisable by zero', e)
        raise
    finally:
        print('done')
devlog(9,7)

