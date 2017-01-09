#!/usr/bin/env python3
__author__ = 'Emmanuel Oluka'
'''
using regular expressions
'''
import re

def Main():
    line = 'I think I understand regular expressions'

    matchResults = re.match('think', line, re.M|re.I)
    if matchResults:
        print('Match found: '+matchResults.group())
    else:
        print('No match was found')

    searchResult = re.search('think', line, re.M|re.I)
    if searchResult:
        print('Search found: '+searchResult.group())
    else:
        print('No search results was found')


if __name__=='__main__':
    Main()
