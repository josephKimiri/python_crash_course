available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " +requested_topping+ ". ")
    else:
        print("Sorry the "+requested_topping+ " topping is not available!")
print("\nWelcome again to Mash Pizza again.")        

        