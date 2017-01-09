#!/usr/bin/env python3
'''Cars class'''
__author__ = 'Emmanuel Oluka'

class Cars(object):
    '''Class that returns the year, make and mode of a car'''
    def __init__(self, year, make, model):
        self.year = str(year)
        self.make = make
        self.model = model
        self.static = 'This is some model specific information'

    def __str__(self):
        '''This mothod, formats the output'''
        print('The model %s %s %s' %(self.year, self.make, self.model))

    def printCar(self):
        '''This method prints out the card details'''
        print('The make is : %s and model is : %s' % (self.make, self.model))
        print('More details: %s %s %s'% (self.year, self.make, self.model))


class MotoBike(Cars):
    pass

mbike = MotoBike(2016, 'Hally Davidson', 'Tonardo')
newCar = Cars(2015, 'Ford', 'Explorer')
print(newCar.printCar())

print('Moto Bike Info')
print(mbike.printCar())