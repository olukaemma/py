#!/usr/bin/env python3
__author__ = 'emmanueo'

bar = ""
for grade in open('grades.txt'):
    for i in range(1, int(grade) + 1):
        if i % 5 == 0:
            bar = bar + "*"
    print(bar, i)
    bar = ''

numbers = [1,2,3,4]
it = iter(numbers)
print(next(it))
fileIT = open('grades.txt', 'r')
print(next(fileIT), end='')

gradesdec = {'Cynthia':88, 'Emmanuel':100, 'David':88}
for key in gradesdec.keys():
    print(key, gradesdec[key])

num = range(1, 11)
it = iter(num)
print(next(it))

import os
files = os.popen('dir *.py')
for x in files:
    print(x)

sqr = ((10,8), (10,23), (25,23), (25,8))
for points in sqr:
    print(points)

grad = [71, 88, 90, 75]
grad = [gradx + 5 for gradx in grad]
print(grad)

words = ['NOW', 'WE', 'READY', 'TO', 'START']
words = [word.lower() for word in words]
print(words)

myFile = open('grades.txt')
grd = myFile.readlines()
print(grd)
for i in range(len(grd)):
    grd[i] = grd[i].rstrip()
print(grd)

myFile = [grd.rstrip() for grd in open('grades.txt')]
print(myFile)

#Print out the all even numbers in the range 1-100
N = range(1, 101)
EN = [x for x in N if x % 2 == 0]
print(EN)

sent = 'Now is the time for all the good people to come to the aid '
sent += 'of their party'
words = sent.split(' ')
wlen = [(word, len(word)) for word in words]
for i in wlen:
    print(i)

def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
            count += 1
    return count
ask = input("Please enter a sentence: ")
print(numVowels(ask))

def ftoc(temp):
    return (temp - 32.0) * (5.0 / 9.0)

def ctof(temp):
    return temp * (9/5) + 32

def convert(temp, toScale):
    if toScale.lower() == 'c':
        return ftoc(temp)
    elif toScale.lower() == 'f':
        return ctof(temp)
    else:
        print('You entered a wrong scale')

print('Enter a temperature: ')
temp = float(input())
scale = input('Enter the scale: ')
converted = convert(temp, scale)
print('The temperature is {} {}.f2 {}'.format(temp, converted, scale))

#The Boolian or predicate function


def isVowel(letter):
     if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
         return True
     else:
         return False

def newVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if isVowel(string[i]):
            count += 1
    return count
userinput = input('Please a string :')
print(newVowels(userinput))


def fact(number):
    product = 1
    for i in range(1,(number + 1)):
        product *= i
    return product
prdnum = int(input('Enter a number: '))
print(str(prdnum) + "! equals " + str(fact(prdnum)))

#compute factorial of a number

def factx(number):
    if number <= 1:
        return 1
    else:
        return number * factx(number - 1)
print(factx(5))

#recursing over string
#using the function explode
def explode(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] + " " + explode(word[1:])
#function to remove dups
def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0]==word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])
