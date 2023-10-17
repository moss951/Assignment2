import product, stockStatement

def getResponse(message, type = 'string', min = None, max = None):
    while True:
        response = input(message)

        if type == 'float':
            try:
                convertedResponse = float(response)
            except:
                print('Invalid response. Enter a float.')
                continue
        elif type == 'int':
            if response.isnumeric():
                convertedResponse = int(response)
            else:
                print('Invalid response. Enter an integer.')
                continue

        if type == 'float' or type == 'int':
            if (min == None or min != None and convertedResponse > min) and (max == None or max != None and convertedResponse < max):
                return convertedResponse
            else:
                print('Invalid response. Enter a number in between the minimum and/or maximum.')
                continue
                
        return response

product1 = product.Product(getResponse('Enter product code: ', 'int', 99, 1001), getResponse('Enter product name: '))
stockStatement1 = stockStatement.StockStatement(getResponse('Enter sale price: ', 'float', 0), getResponse('Enter manufacure cost: ', 'float', 0), getResponse('Enter stock level: ', 'int', 0), getResponse('Enter monthly units sold: ', 'int', -1))

def printDetails():
    product1.printDetails()
    stockStatement1.printDetails()

def predictStock():
    for i in range(1, 13):
        stockStatement1.generateStockStatement(i)

def displayNetProfit():
    print('Net Profit:', stockStatement1.getNetProfit(), 'CAD')

printDetails()
predictStock()
displayNetProfit()
