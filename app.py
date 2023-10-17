'''

This file contains the main program which will be run. It interacts with the user and contains objects from external classes.

'''

import product, stockStatement

def getResponse(message, type = 'string', min = None, max = None): # keep prompting until a valid response is detected
    while True:
        response = input(message)

        if type == 'float':
            try: # try to convert the response into a float. If it can't, the exception will run
                convertedResponse = float(response)
            except:
                print('Invalid response. Enter a float.')
                continue
        elif type == 'int':
            if response.isnumeric(): # try to convert the response into an integer
                convertedResponse = int(response)
            else:
                print('Invalid response. Enter an integer.')
                continue

        if type == 'float' or type == 'int':
            if (min == None or min != None and convertedResponse > min) and (max == None or max != None and convertedResponse < max): # check if the number entered is greater than the minimum and/or less than the maximum, if there are any specified
                return convertedResponse
            else:
                print('Invalid response. Enter a number in between the minimum and/or maximum.')
                continue
                
        return response

product1 = product.Product(getResponse('Enter product code (between 100 and 1000): ', 'int', 99, 1001), getResponse('Enter product name: ')) # product1 stores the code and name of the product
stockStatement1 = stockStatement.StockStatement(getResponse('Enter sale price (above 0): ', 'float', 0), getResponse('Enter manufacure cost (above 0): ', 'float', 0), getResponse('Enter stock level (above 0): ', 'int', 0), getResponse('Enter monthly units sold (0 or more): ', 'int', -1)) # stockStatement1 stores the prices and inventory of the product

def printDetails(): # print product details located in the product objects
    product1.printDetails()
    stockStatement1.printDetails()

def predictStock(): # print a stock statement 12 times
    for i in range(1, 13):
        stockStatement1.generateStockStatement(i)

def displayNetProfit(): # print the net profit made in 12 months
    print('Net Profit:', stockStatement1.getNetProfit(), 'CAD')

printDetails()
predictStock()
displayNetProfit()
