MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def enough(order):
    """Return True if there are enough resources, else print why not and return False."""
    for item, amount in MENU[order]["ingredients"].items():
        if amount > resources.get(item, 0):
            print(f"Sorry, we don't have enough {item}.")
            return False
    return True


def take_payment(cost):
    """Return the amount of money inserted, or None if the user can't pay."""
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total = quarters * QUARTER + dimes * DIME + nickels * NICKEL + pennies * PENNY

    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return None
    change = round(total - cost, 2)
    if change > 0:
        print(f"Here's ${change} in change.")
    return total


def make_coffee(order):
    for item, amount in MENU[order]["ingredients"].items():
        resources[item] -= amount


print("Welcome to the coffee machine. espresso is $1.5, latte is $2.5, cappuccino is $3.0")

ending = False
while not ending:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        print(resources)
        continue
    elif order == "off":
        ending = True
        continue
    elif order not in MENU:
        print("Please choose between our three options.")
        continue

    if not enough(order):
        continue

    cost = MENU[order]["cost"]
    print(f"Please insert coins for ${cost}")

    payment = take_payment(cost)
    if payment is None:
        continue

    make_coffee(order)
    print(f"Here's your {order}, enjoy!")


