#!/usr/bin/env python3
__author__ = 'Emmanuel Oluka'

'''using Templats in string'''

from string import Template

def Main():
    cart = []
    cart.append(dict(item='Coke', price=8, qty=2))
    cart.append(dict(item='Sugar', price=10, qty=3))
    cart.append(dict(item='rice', price=5, qty=5))

    tmp = Template("$qty x $item = $price")
    total = 0
    print("Cart: ")
    for data in cart:
        print(tmp.substitute(data))
        total += data["price"]
    print('Total: '+ str(total))

