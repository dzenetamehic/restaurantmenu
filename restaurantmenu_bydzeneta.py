print "Welcome to our restaurant! Would you like us to quote prices of our dishes?"

# dishes we serve:
# Beef steak with potatoes
# Wiener Schnitzel with potato salad
# Hokkaido papaya cream soup
# Veal goulash with homemade 'Nockerl'
# Steak from young beef with potato wedges

menu = {}

while True:
    dish_name = raw_input("Please enter the name of the dish here: ")
    dish_price = raw_input("Enter the price for '%s': " % dish_name)
    menu[dish_name] = dish_price

    new = raw_input("Do you want to enter a new dish? (yes/no) ")

    if new.lower() == "no":
        break

print "Menu: %s" % menu

with open("menu.txt", "w+") as menu_file:
    for dish in menu:
       menu_file.write("%s, %s EUR\n" % (dish, menu[dish]))

print "Thank you!"