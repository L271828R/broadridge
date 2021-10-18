class VendingMachine:
    def __init__(self):
        self.dic_id_price = {"ID100":100.00,"ID200":200.00,"ID300":300.00}

    def getItemIds(self):
        return self.dic_id_price.keys() 

    def getPriceForItem(self, id):
        if id in self.dic_id_price:
            return self.dic_id_price[id]
        else:
            raise Exception("Item not found")

    def isValidMoney(self, money):
        if (not isinstance(money, (int, float))):
            return False 
        else:
            return True

    def validatePurchase(self, itemId, money):
        if not self.isValidMoney(money):
            raise Exception("Money input not valid")

        if itemId not in self.dic_id_price:
            raise Exception("Item not found")
    
        if (money >= self.getPriceForItem(itemId)):
                return True
        else:
            return False


if __name__ == '__main__':
    vendingmachine = VendingMachine()
    print(vendingmachine.getItemIds())
    print(vendingmachine.getPriceForItem('ID100'))
    print(vendingmachine.validatePurchase("ID100", 110))
    print(vendingmachine.validatePurchase("ID100", 90))

