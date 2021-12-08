from ShopClassDRS import ShopDRS

def itemDRS():
    list = [] 
    num = int(input("Enter the amount of food you're ordering: "))
    while num < 1: 
        print("The amount must be atleast 1, Please input another amount")
        num = int(input("Enter the amount of item you're ordering:"))
    for i in range(num):
        name = str(input(f"Whats food are you ordering #{i+1}?: "))
        pound = float(input("Enter the amount in pounds: "))
        while pound <= 0: 
            print("The amount must be atleast 1, Please input another amount")
            pound = float(input("Enter the amount in pounds: "))
        print("")
        item = ShopDRS(name,pound)
        list.append(item) 
    return list

def showDRS(list):
    print("Items purchased") 
    print("=================")
    for i in list:
        print(f"Item : {i.getFoodNameDRS()}") 
        print(f"Amount : {i.getAmountDRS()} pounds")
        print("Price per pound : ${:.2f}".format(i.getPriceDRS())) 
        print("Price of order : ${:.2f}".format(i.PriceCalcDRS()))
        print("") 

def priceDRS(list):
    cost = 0 
    for i in list: 
        cost += i.PriceCalcDRS()
    print("The total cost is: ${:.2f}".format(cost)) #The output

def main(): #The main method
    x = itemDRS()
    showDRS(x)
    priceDRS(x)

main() #To run the program