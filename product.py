import random

class Product:
    def __init__(self, code, name, price, manufactureCost, stockLevel, monthlyUnitsManufactured):
        self._code = code
        self._name = name
        self._price = price
        self._manufactureCost = manufactureCost
        self._stockLevel = stockLevel
        self._monthlyUnitsManufactured = monthlyUnitsManufactured

    def printDetails(self):
        print('\nProduct Code:', self._code)
        print('Product Name: ' + self._name, '\n')
        print('Sale Price:', self._price, 'CAD')
        print('Manufacture Cost:', self._manufactureCost, 'CAD')
        print('Monthly Production:', self._monthlyUnitsManufactured, 'units (Approx.)\n')
    
    def getMonthlyUnitsSold(self):
        return self._monthlyUnitsManufactured + random.randrange(-10, 11)

    def updateStockLevel(self, unitsSold):
        self._stockLevel += self._monthlyUnitsManufactured - unitsSold

    def generateStockStatement(self, index):
        monthlyUnitsSold = self.getMonthlyUnitsSold()
        self.updateStockLevel(monthlyUnitsSold)

        print('Month', index, ': ')
        print('|    Manufactured:', self._monthlyUnitsManufactured, 'units')
        print('|    Sold:', monthlyUnitsSold)
        print('|    Stock:', self._stockLevel)