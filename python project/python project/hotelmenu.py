menu = {
    'pizza':50,
    'burger':60,
    'sandwich':80,
    'coffee':100,
    'salad':20,
    'maggie':40,
}
#greet 
print("welcome to python restro...")
print("pizza: RS40\nburger: RS60\nsandwich: RS80\ncoffee: RS100\nsalad: RS20\nmaggie: RS40")

order_total = 0

order_1 = input("how would you like to eat sir/mam = ")
if order_1 in menu:
    order_total += menu[order_1]
    print(f"your item {order_1} has been added to your order")

else:
    print("this item is  not available sorry, order something else")

another_order = input("would you like something else ")
if another_order == "yes":
    item_2 = input("enter the name of dish would you like")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your order")

    else:
        print(f"ordered item {item_2} is not available")

print(f"the total amount of items to pay is {order_total}")