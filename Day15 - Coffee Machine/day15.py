MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit_earned = 0.0
is_coffee_machine_switched_off = False


def print_report(machine_resources, profit):
    print(f"Water: {machine_resources["water"]}ml")
    print(f"Milk: {machine_resources["milk"]}ml")
    print(f"Coffee: {machine_resources["coffee"]}g")
    print(f"Money: ${profit}")


def check_resources(machine_resources, drink_option):
    for item in MENU[drink_option]["ingredients"]:
        if machine_resources[item] < MENU[drink_option]["ingredients"][item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins(quarters, dimes, nickles, pennies, coffee_cost):
    entered_amount = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return round(entered_amount - coffee_cost, 2)


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


valid_options = ["off", "report", "espresso", "latte", "cappuccino"]
while not is_coffee_machine_switched_off:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "off" or option not in valid_options:
        is_coffee_machine_switched_off = True
    elif option == "report":
        print_report(resources, profit_earned)
    else:
        is_available = check_resources(resources, option)
        if not is_available:
            is_coffee_machine_switched_off = True
        else:
            print("Please insert coins.")
            quarters_count = int(input("How many quarters?: "))
            dimes_count = int(input("How many dimes?: "))
            nickles_count = int(input("How many nickles?: "))
            pennies_count = int(input("How many pennies?: "))
            coffee_type_cost = MENU[option]["cost"]
            diff_amount = process_coins(quarters_count, dimes_count, nickles_count, pennies_count, coffee_type_cost)
            if diff_amount < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if diff_amount == 0:
                    print("Exact Amount! No Change Required")
                else:
                    print(f"Here is ${diff_amount} in change")
                make_coffee(option, MENU[option]["ingredients"])
                profit_earned += coffee_type_cost
