'''

This file contains the StockStatement class, which displays and keeps track of the units manufactured and sold, as well as net profit.

'''

import random

class StockStatement:
    def __init__(self, price, manufactureCost, stockLevel, monthlyUnitsManufactured): # constructor
        self._price = price
        self._manufactureCost = manufactureCost
        self._stockLevel = stockLevel
        self._monthlyUnitsManufactured = monthlyUnitsManufactured

        self._totalUnitsSold = 0 # keep track of total units sold and manufactured over time
        self._totalUnitsManufactured = 0

    def printDetails(self): # print the product's price, manufacture cost and units manufactured per month
        print('Sale Price:', self._price, 'CAD')
        print('Manufacture Cost:', self._manufactureCost, 'CAD')
        print('Monthly Production:', self._monthlyUnitsManufactured, 'units (Approx.)\n')

    def getMonthlyUnitsSold(self): # get the number of units sold per month. Ranges from units manufactured +/- 10
        return self._monthlyUnitsManufactured + random.randrange(-10, 11)

    def updateStockLevel(self, unitsSold): # set the new stock of the product after manufacturing and selling units
        self._stockLevel += self._monthlyUnitsManufactured - unitsSold

    def generateStockStatement(self, index): # update the stock, total units sold and manufactured, and print a stock statement for a month
        monthlyUnitsSold = self.getMonthlyUnitsSold()
        self.updateStockLevel(monthlyUnitsSold)

        print('Month', index, ': ')
        print('|    Manufactured:', self._monthlyUnitsManufactured, 'units')
        print('|    Sold:', monthlyUnitsSold)
        print('|    Stock:', self._stockLevel)

        self._totalUnitsManufactured += self._monthlyUnitsManufactured
        self._totalUnitsSold += monthlyUnitsSold

    def getNetProfit(self): # calculate the net profit from the total units sold and manufactured
        return format(self._totalUnitsSold * self._price - self._totalUnitsManufactured * self._manufactureCost, '.2f')
