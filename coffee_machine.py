MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
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
    """주문을 만들 수 있을 때는 True를 반환하고 , 재료가 부족할때는 False를 반환한다."""
    for item in order_ingredients:
        if  order_ingredients[item] > resources.get(item, 0):
            print(f"죄송합니다. {item}이 충분하지 않습니다.")
            return False
    return True

def process_coins():
    """투입된 동전으로 계산된 총액을 반환한다."""
    total = 0
    print("동전을 넣어주세요.")
    quarters = int(input("쿼터동전을 몇개 넣으시겠습니까?($0.25): "))
    dimes = int(input("다임동전을 몇개 넣으시겠습니까?($0.10): "))
    nickels = int(input("니켈동전을 몇개 넣으시겠습니까?($0.05): "))
    pennies = int(input("페니동전을 몇개 넣으시겠습니까?($0.01): "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """지불이 승인되면 True를 반환하고, 금액이 부족하면 False를 반환한다."""
    global profit
    if money_received >= drink_cost:
        charge = round(money_received - drink_cost, 2)
        if charge > 0:
            print(f"거스름돈 ${charge:.2f}를 돌려드립니다.")
        profit += drink_cost
        return True
    else:
        print("죄송합니다. 금액이 부족합니다. 돈이 환불되었습니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """재원(resources)에서 필요한 재료 (order_ingredients)를 차감한다."""
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print(f"여기 {drink_name}가 나왔습니다. 즐기세요!")

while True:
    choice = input("어떤 음료를 원하시나요?(espresso/latte/cappuccino): ")

    if choice == "off":
        print("커피머신 프로그램을 종료합니다.")
        break
    elif choice == "report":
        print(f"-물: {resources['water']}ml")
        print(f"-우유: {resources['milk']}ml")
        print(f"-커피: {resources['coffee']}g")
        print(f"-돈: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            total = process_coins()
            if is_transaction_successful(total, drink['cost']):
                make_coffee(choice, drink['ingredients'])
    else:
        print("잘못입력하였습니다. 다시 입력해주세요.")