'''

This file contains the product class, which stores the product's name and code number

'''

class Product:
    def __init__(self, code, name): # constructor
        self._code = code
        self._name = name

    def printDetails(self): # print the product's name and code
        print('\nProduct Code:', self._code)
        print('Product Name: ' + self._name, '\n')
        