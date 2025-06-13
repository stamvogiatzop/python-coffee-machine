from data import MENU, resources
from art import logo, royal
from time import sleep

PENNY = 0.01
NICKLE = 0.05
DIME = 0.10
QUARTER = 0.25
BANK = 0

def report_resources():
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")

def delayed_message(msg, secs):
    for i in range(len(msg)):
        print(msg[i], sep=' ', end=' ', flush=True)
        sleep(secs)

def refill_resources():
    message = 'Refilling...'
    delayed_message(message, 0.2)
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100
    print("Refilling successful!\n")
    print(f"Current resources are:"
          f"\nWater: {resources["water"]}ml"
          f"\nMilk: {resources["milk"]}ml"
          f"\nCoffee: {resources["coffee"]}g"
          f"\nMoney: ${resources["money"]}")

def collect_money():
    global BANK
    message = 'Collecting gold...'
    delayed_message(message, 0.1)
    BANK += resources["money"]
    resources["money"] = 0
    print("\n'The coffers are full, Your Grace. The peasants have paid their due.'\n")

def bank():
    print(f"\nAs decreed by fate and filtered through "
          f"the finest beans, your treasury rests at a modest ${BANK}\n")

def check_resources(coffee_type):
    ingredients_needed = MENU[coffee_type]["ingredients"]
    for ingredient in ingredients_needed:
        if resources[ingredient] < ingredients_needed[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def insert_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coin_sum = round((quarters * QUARTER) + (dimes * DIME) + (nickles * NICKLE) + (pennies * PENNY), 2)
    print(f"You inserted ${coin_sum}")
    return coin_sum

def make_coffee(coffee_type):
    ingredients_needed = MENU[coffee_type]["ingredients"]
    for ingredient in ingredients_needed:
        resources[ingredient] -= ingredients_needed[ingredient]
    return resources

def check_transaction(coffee_type):
    coffee_price = MENU[coffee_type]["cost"]
    coin_sum = round(insert_coins(), 2)
    change = 0
    if coin_sum >= coffee_price:
        change = round((coin_sum - coffee_price), 2)
        resources["money"] += coffee_price
        make_coffee(coffee_type)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type} 🍵🍵🍵. Enjoy!")
    else:
        print(f"Sorry that's not enough money. ${coin_sum} refunded.")
    return change

# TODO: 1. Prompt user by asking “ What would you like? (espresso: $1.5/latte: $2.5/cappuccino: $3): ”
print(logo)
choice = input("espresso: $1.5\nlatte: $2.5\ncappuccino: $3\nWhat would you like?:\n").lower()

while True:
    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == "off":
        print("Turning off the machine. Goodbye!")
        break

    elif choice == "maintenance":
        print(royal)
        print("Aaaaah... A royal coffee bean initiate! What would you like to do sire?")
        option = input("Report resources, Refill resources, Collect your gold, check your royal coffers or exit the realm?"
                       " (report/refill/collect/bank/exit): \n").lower()
        while True:
            if option == "exit":
                print("Farewell, and may your coffee days be most splendid.")
                break
            elif option == "report":
                # TODO: 3. Print report.
                report_resources()
            elif option == "refill":
            # TODO: 7. Refill machine
                refill_resources()
            # TODO: 8 Collect money
            elif option == "collect":
                collect_money()
            elif option == "bank":
                bank()
            else:
                print("Invalid input. Buzz off coffee peasant...")
            option = input("Does your noble self desire anything further?? (report/refill/collect/bank/exit): \n").lower()

    # TODO: 4. Check resources sufficient?
    elif choice in MENU:
        if check_resources(choice):
            # TODO: 5. Process coins.
            check_transaction(choice)

    else:
        print("Invalid input. Please choose espresso, latte, or cappuccino. or exit.")

    print(logo)
    choice = input("espresso: $1.5\nlatte: $2.5\ncappuccino: $3\nWhat would you like?:\n").lower()

# TODO: 6. Check transaction successful?
