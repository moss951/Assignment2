class Product:
    def __init__(self, code, name):
        self._code = code
        self._name = name

    def printDetails(self):
        print('\nProduct Code:', self._code)
        print('Product Name: ' + self._name, '\n')
        