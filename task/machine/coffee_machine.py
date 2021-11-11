# Write your code here
water = 400
milk = 540
beans = 120
cups = 9
money = 550
empty_resource = ''
coffee = {'1': {'water': 250,
                'milk': 0,
                'beans': 16,
                'money': 4},
          '2': {'water': 350,
                'milk': 75,
                'beans': 20,
                'money': 7},
          '3': {'water': 200,
                'milk': 100,
                'beans': 12,
                'money': 6}
          }


def print_stats():
    global water, milk, beans, cups, money
    print(f"""The coffee machine has:
    {water} of water
    {milk} of milk
    {beans} of coffee beans
    {cups} of disposable cups
    {money} of money""")
    pass


def cnt_cups():
    cnt = int(input("Write how many cups of coffee you will need:"))
    print(f"""For {cnt} cups of coffee you will need:
    {cnt * 200} ml of water
    {cnt * 50} ml of milk
    {cnt * 15} g of coffee beans""")


def cnt_cups2(coffee_picked):
    global water, milk, beans, cups, empty_resource
    if coffee[coffee_picked]["milk"] != 0:
        max_cups = min(water // coffee[coffee_picked]["water"],
                       milk // coffee[coffee_picked]["milk"],
                       beans // coffee[coffee_picked]["beans"])
        if water // coffee[coffee_picked]["water"] == 0:
            empty_resource = 'water'
        elif milk // coffee[coffee_picked]["milk"] == 0:
            empty_resource = 'milk'
        else:
            empty_resource = 'beans'
    else:
        max_cups = min(water // coffee[coffee_picked]["water"],
                       beans // coffee[coffee_picked]["beans"])
        if water // coffee[coffee_picked]["water"] == 0:
            empty_resource = 'water'
        else:
            empty_resource = 'beans'
    cnt = 1

    if cnt <= max_cups:
        return True
    else:
        return False


def buy():
    global coffee, water, milk, beans, money, cups, empty_resource
    coffee_picked = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if coffee_picked == 'back':
        return
    if cnt_cups2(coffee_picked):
        water -= coffee[coffee_picked]["water"]
        milk -= coffee[coffee_picked]["milk"]
        beans -= coffee[coffee_picked]["beans"]
        cups -= 1
        money += coffee[coffee_picked]["money"]
    else:
        print(f"Sorry, not enough {empty_resource}!.")


def fill():
    global water, milk, beans, cups
    water += int(input("Write how many ml of water you want to add:"))
    milk += int(input("Write how many ml of milk you want to add:"))
    beans += int(input("Write how many grams of coffee beans you want to add:"))
    cups += int(input("Write how many disposable coffee cups you want to add:"))


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


def coffee_machine():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit)")
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            print_stats()
        elif action == "exit":
            break


coffee_machine()
