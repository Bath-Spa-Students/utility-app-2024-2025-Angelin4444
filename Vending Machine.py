#This helps to import pretty table from the library. 
#PrettyTable helps in creating the item names, code, and the price to be in a good table format making it more appealing 
from prettytable import PrettyTable
#Labeling each product we have in the vending machine with its price and a id 
product_info = [
    {"productId": 0, "product": "Princles", 'productPrice': 7},
    {"productId": 1, "product": "Lays", 'productPrice': 5},
    {"productId": 2, "product": "Cheetos", 'productPrice': 5},
    {"productId": 3, "product": "Fanta", 'productPrice': 2},
    {"productId": 4, "product": "7up", 'productPrice': 2},
    {"productId": 5, "product": "Coke", 'productPrice': 2},
    {"productId": 6, "product": "Mars", 'productPrice': 4},
    {"productId": 7, "product": "Twix", 'productPrice': 4},
    {"productId": 8, "product": "Protein Bars", 'productPrice': 5},
    {"productId": 9, "product": "Water", 'productPrice': 1},
    {"productId": 10, "product": "Cold Tea", 'productPrice': 3},
    {"productId": 11, "product": "Cold Coffee", 'productPrice': 3},
]
#Helps in creating neat tables 
table = PrettyTable() #(Creates the table aligning all the products into one)
table.field_names = ["Product", "Price (Dhs)", "Code No."] #(Helps to give neat headings)
for product in product_info:
    table.add_row([product["product"], product["productPrice"], product["productId"]]) #(adding rows back to back)

# Allows to initializing variables
bag = [] #(empty cart for letting know how many products are added)
receipt = """ 
\t\tPRODUCT NAME -- COST (Dhs)
""" #(Shows what all bought and the total amount for it)
run = True#(the program will keep on running until the consumer finishes it)

# Welcome messages are print using the print function
print("------- Welcome to BathBite's Vending Machine -------\n\n")#(vending machine's name)
print("---------- Please Select a Product ----------\n\n")#(asking the consumer to select the product from the table)
print(table)#(table pop ups)

# this function starts the main vending machine process
def vendingMachine(product_info, run, bag):
    while run:#(asking the user this qns until they finshes ordering (quiting))
        try:#(finds out if there are any errors)
            buyProduct = int(input("\nEnter the product code for the product you want to buy: ")) #(asking the consumer what they want to buy)
            if 0 <= buyProduct < len(product_info): #(helps to find if the code given by the consumer is valid or not)
                bag.append(product_info[buyProduct])
                print(f"Added {product_info[buyProduct]['product']} to your bag!") #(if yes then this is outputed)
            else:
                print("Invalid product code. Please try again.") #(if no then this is outputed)
        except ValueError:#(finds out if there are any errors)
            print("Invalid input! Please enter a valid number.") #(if found then this is printed)
        
        moreProducts = input("Type any key to add more products, or type 'no' to stop: ").lower()
        #(asking the consumer if they wanted to buy more products)
        if moreProducts == "no":#(if no then print this statement)
            run = False
#used for calculating the total cost
    totalCost = sumProduct(bag) #(gives the list of products in the bag to the consumer)
    print(f"\nYour total cost is: Dhs{totalCost:.2f}") #(adds up the total amount and gives the total)
    processPayment(totalCost)#( starts the payment process)
#asking if the user needs a receipt or excit after the purchase 
    receiptChoice = input("\n1. Print the bill\n2. Exit\nEnter your choice: ")#(question for the user)
    if receiptChoice == "1":
        print(createReceipt(bag, receipt))#(if the user tells that they wanted the receipt this will be outputed)
    else:
        print("Thank you for using the vending machine!")#(if not then this will be outputed)
#these functions used bellow lets the user know how much is it in the bag and asking the user to make the payment
def sumProduct(bag):#calculates the total cost of all the products in the users bag.
    return sum(p["productPrice"] for p in bag)
#gives a detailed receipt telling all the purchased products and its prices.
def createReceipt(bag, receipt):
    for p in bag:
        receipt += f"\t{p['product']} -- {p['productPrice']} Dhs\n"
    receipt += f"\tTotal --- {sumProduct(bag)} Dhs\n"
    return receipt#(this will print for the receipt)
#This program tells the user how much money more is left for the user to pay 
def processPayment(amount_due):
    print("\n--- Payment Section ---")
    while amount_due > 0:
        try:
            payment = float(input(f"Please insert money (Dhs remaining: {amount_due:.2f}): "))#asking the user to input money 
            if payment >= amount_due:
                change = payment - amount_due#(helps in calculating is its correct amount paid)
                print(f"Thank you for your purchase! Your change is Dhs{change:.2f}.")#(if the user paid correct amount then this will output)
                break
            else:
                print("Insufficient payment. Please insert more money.")#(if not it will ask the user to insert the rest of the amount)
                amount_due -= payment
        except ValueError:#(helps in finding error)
            print("Invalid payment amount. Please enter a valid number.")

# Main code for running the entire program
vendingMachine(product_info, run, bag)
