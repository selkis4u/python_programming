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
        "cost": 3.5,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk" : 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """주문을 만들 수 있을 때는 True를 반환하고, 재료가 부족할 때는 False를 반환한다."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이 충분하지 않습니다.")
            return False
    return True

def process_coin():
    """투입된 동전으로 계산된 총액을 반환한다."""
    print(f"동전을 넣어주세요.")
    quarters = int(input("동전을 몇개 넣으시나요?(쿼터동전):"))
    dimes = int(input("동전을 몇개 넣으시나요?(다임동전):"))
    nikels = int(input("동전을 몇개 넣으시나요?(니켈동전):"))
    pennies = int(input("동전을 몇개 넣으시나요?(페니동전):"))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nikels + 0.01 * pennies
    return total    

def is_transaction_successful(money_received, drink_cost):
    """지불이 승인되면 True를 반환하고, 금액이 부족하면 Flase를 반환한다."""
    if money_received < drink_cost:
        print(f"죄송합니다. 금액이 부족합니다.돈이 환불되었습니다.")
        return False
    else:
        global profit
        profit = profit + drink_cost
        change = money_received - drink_cost
        print(f"거스름돈 ${change:.2f}를 돌려드립니다.")
        return True
       
def make_coffee(drink_name, order_ingrdients):
    """자원(resources)에서 필요한 재료(ingredients)를 차감한다.)"""
    for item in order_ingrdients:
        resources[item] = resources[item] - order_ingrdients[item]
    print(f"여기 {drink_name}가 나왔습니다. 즐기세요!")


while True:
    name = input("어떤 음료를 원하시니요? (espresso/latte/cappuccino):")
    if name == "off":
        exit()
    elif name == "report":
        print(f"물: {resources['water']}ml")
        print(f"우유: {resources['milk']}ml")
        print(f"커피: {resources['coffee']}g")
        print(f"돈: ${profit:.2f}")
    elif name in MENU:
        drink = MENU[name]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(name, drink["ingredients"])