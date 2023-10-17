import random

class StockStatement:
    def __init__(self, price, manufactureCost, stockLevel, monthlyUnitsManufactured):
        self._price = price
        self._manufactureCost = manufactureCost
        self._stockLevel = stockLevel
        self._monthlyUnitsManufactured = monthlyUnitsManufactured

        self._totalUnitsSold = 0
        self._totalUnitsManufactured = 0

    def printDetails(self):
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

        self._totalUnitsManufactured += self._monthlyUnitsManufactured
        self._totalUnitsSold += monthlyUnitsSold

    def getNetProfit(self):
        return self._totalUnitsSold * self._price - self._totalUnitsManufactured * self._manufactureCost
