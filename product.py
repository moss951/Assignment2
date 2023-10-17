class Product:
    def __init__(self, code, name, price, manufactureCost, stockLevel, monthlyUnitsManufactured):
        self._code = code
        self._name = name
        self._price = price
        self._manufactureCost = manufactureCost
        self._stockLevel = stockLevel
        self._monthlyUnitsManufactured = monthlyUnitsManufactured
    
    