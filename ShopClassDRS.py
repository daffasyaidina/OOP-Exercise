class ShopDRS:
    def __init__(self,food,amount): 
        self.__food = food
        self.__amount = amount
        self.__price = self.getPriceDRS()
        self.__totalprice = self.PriceCalcDRS()

    def getFoodNameDRS(self): 
        return self.__food
    def getAmountDRS(self): 
        return self.__amount

    def __PriceListDRS(self): 
        if self.__food == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__food == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__food == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__food == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__food == "Moose Cheese":
            self.__price = 487.20
        elif self.__food == "White Truffles":
            self.__price = 3600.00
        elif self.__food == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__food == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else:
            self.__price = 0  

    def getPriceDRS(self): 
        self.__PriceListDRS()
        return self.__price
    def PriceCalcDRS(self): 
        self.__totalprice = self.__price * self.__amount
        return self.__totalprice