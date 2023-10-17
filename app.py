import product

product1 = product.Product(int(input('Enter product code: ')), input('Enter product name: '), float(input ('Enter product sale price: ')), float(input('Enter product manufacture cost: ')), int(input('Enter stock level: ')), int(input('Enter monthy units manufactured: ')))

product1.printDetails()

for i in range(1, 13):
    product1.generateStockStatement(i)
