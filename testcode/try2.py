#!/usr/bin/env python3
__author__ = 'Emmanuel Oluka'
'''
Program to print mulitple lines
'''
print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+   This program is writen by and property of Emmanuel Oluka      +
+           under GNU license and ioluka inc.                     +
+ You are free to resue this code but any furhter modifications,  +
+        should be shared under the GNU license                   +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('An Error occured, values', e.value)
