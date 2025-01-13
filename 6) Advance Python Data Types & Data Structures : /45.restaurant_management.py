
## Restaurant Management System :

# Restaurant Management System is a simple python project for beginners, from which they can learn to develop web based python project. 

# If we are going to any restaurant and we are checking the menu of that particular restaurant
    # what we will see that in the menu , In the menu all the food items would be there
    # and the price of that food items would be there.
# If I am a user , I am coming to the restaurant , if I get that particular menu card,
    # I can get to know that this is the food and this is the price of that food and 
    # we respect to that I will order that particular food.

# So I just need to create a data structure which will store the food name and the price of that food name. 
    # So for that we are going to use the dictionary data structure because in
    # dictionary we can store the key-value pair. So in a key I can write my food name 
    # and in the value I can write the price of that food name.


# Create a dictionary "menu" and in that dictionary I will store the food name and the price of that food name.
menu = {
    "Coffee": 2,
    "Pasta": 3,
    "Pizza": 5,
    "Burger": 6,
    "Chicken": 10,
}

# Now print the menu because I want to show the menu in front of the user whenever they will execute 
    # our application.

print(
    """

    Welcome to Rajkumar's Restaurant. Please Order Food!

    Coffee: $2
    Pasta: $3
    Pizza: $5
    Burger: $6
    Chicken: $10

    """

)

# Now I will take the order from the user. So I will ask the user to enter the food name and the quantity of that food name.

total_price = 0   # Initially the total price is 0 because the user has not ordered anything yet.

item1 = input("Enter the name of the item you want to order:")  # I will take the input from the user and store it in the variable "item1".
if item1 in menu:                                 # If the item1 is in the menu then I will add the price of that item to the total price and print the message.
    total_price += menu[item1]                   # I will add the price of that item to the total price.
    print(f"You ordered {item1}. Your total order is ${total_price}.")   # I will print the message that you ordered this item and your total order is this much.

else:                                           # If the item1 is not in the menu then I will print the message that the item is invalid.
    print("Invalid item. Please order something from the Menu.")

# Now another order from the user and I will ask the user to enter the food name and the quantity of that food name.

another_order = input("Do you want to add another item ? (yes/no):").lower()  # I will take the input from the user and store it in the variable "another_order". lower() is used to convert the input to lowercase so that the user can enter the input in any case.

if another_order == "yes":    # If the user enters "yes" then I will take the order from the user and store it in the variable "item2".
    item2 = input("Enter the name of the 2nd item you want to order:")   # I will take the input from the user and store it in the variable "item2".
    if item2 in menu:  # If the item2 is in the menu then I will add the price of that item to the total price and print the message.
        total_price += menu[item2]  # I will add the price of that item to the total price.
        print(f"You ordered {item2}. Your total order is ${total_price}.")
    
    else:
        print("Invalid item. Please order something from the Menu.")  # If the item2 is not in the menu then I will print the message that the item is invalid.

print(f"Your Total amount is ${total_price}. Thank you!")  # Finally I will print the total amount of the order.



