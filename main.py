from data import menu
from os import system, name
from art import logo


def clear():
    if name == "nt":
        _ = system("cls")


def money_inserted():
    quarter = float(input("\nHow many quarters?: ")) * 0.25
    loonie = float(input("How many loonies?: "))
    toonie = float(input("How many toonies?: ")) * 2
    total = quarter + loonie + toonie
    return total


def coffee_served(coffee_type, argent):
    cost = menu[coffee_type]["price"]
    m_total = money_inserted()
    if m_total > cost:
        change_back = "{:.2f}".format(m_total - cost)
        clear()
        print(logo)
        print(f"\nHere's your {coffee_type} ☕ and {change_back}$ change, enjoy!")
    elif m_total == cost:
        clear()
        print(logo)
        print(f"\nHere's your {coffee_type} ☕, enjoy!")
        argent += cost
    else:
        clear()
        print(logo)
        print("\nThere's not enough money for that, refund issued.")


def check_levels(var_eau, var_cafe, var_lait, argent):
    print(f"\nWater: {var_eau}ml")
    print(f"Milk: {var_lait}ml")
    print(f"Coffee: {var_cafe}mg")
    print(f"Money: {argent}$")


def coffee_maker():
    print(logo)
    run = True
    water = 600
    milk = 400
    coffee = 200
    money = 0
    money_decimals = "{:.2f}".format(money)

    while run:
        print("\nGood day!")
        coffee_type = input("What would you like to drink? (espresso/latte/cappuccino)\n").lower()

        if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
            water_needed = menu[coffee_type]["ingredients"]["water"]
            coffee_needed = menu[coffee_type]["ingredients"]["coffee"]
            milk_needed = menu[coffee_type]["ingredients"]["milk"]

            if water < water_needed or coffee < coffee_needed or milk < milk_needed:
                clear()
                print(logo)
                print("There's not enough resources for that, money refunded. Type 'refill' to top up the machine.")
            else:
                if coffee_type == "espresso":
                    coffee_served("espresso", money)
                elif coffee_type == "latte":
                    coffee_served("latte", money)
                elif coffee_type == "cappuccino":
                    coffee_served("cappuccino", money)
                water -= water_needed
                coffee -= coffee_needed
                milk -= milk_needed
                money += menu[coffee_type]["price"]

        elif coffee_type == "report":
            clear()
            print(logo)
            check_levels(water, coffee, milk, money_decimals)
        elif coffee_type == "refill":
            clear()
            print(logo)
            water = 600
            milk = 400
            coffee = 200
        elif coffee_type == "off":
            clear()
            print(logo)
            print("Goodnight!")
            run = False
        else:
            clear()
            coffee_maker()


coffee_maker()
