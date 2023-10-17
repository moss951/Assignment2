import product, stockStatement

product1 = product.Product(int(input('Enter product code: ')), input('Enter product name: '))
stockStatement1 = stockStatement.StockStatement(float(input ('Enter product sale price: ')), float(input('Enter product manufacture cost: ')), int(input('Enter stock level: ')), int(input('Enter monthy units manufactured: ')))

product1.printDetails()
stockStatement1.printDetails()

for i in range(1, 13):
    stockStatement1.generateStockStatement(i)

print('Net Profit:', stockStatement1.getNetProfit(), 'CAD')
