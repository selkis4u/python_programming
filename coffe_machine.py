MENU = {
    "espresso": {
        "ingredients": {
            "water" : 50,
            "coffee" : 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}가 부족합니다.")
            return False
    return True

def process_coins():
    total = 0
    print("동전을 넣어주세요.")
    quarters = int(input("몇개 넣으시겠어요? (쿼터동전): "))
    dimes = int(input("몇개 넣으시겠어요? (다임동전): "))
    nickels = int(input("몇개 넣으시겠어요? (니켈동전): "))
    pennies = int(input("몇개 넣으시겠어요? (페니동전): "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"거스름돈 ${change}를 반환합니다.")

        global profit
        profit += drink_cost
        return True
    else:
        print("죄송합니다. 돈이 부족합니다. 돈을 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"여기 {drink_name}가 나왔습니다. 즐기세요!")


while True:
    item = input("어떤 커피를 드릴까요? (espresso/latte/cappuccino): ")
    if item == "off":
        exit()
    elif item == "report":
        print(f"물: {resources['water']}ml")
        print(f"우유: {resources['milk']}ml")
        print(f"커피: {resources['coffee']}g")
        print(f"수익: ${profit:.2f}")
    elif item in MENU:
        drink = MENU[item]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(item, drink["ingredients"])