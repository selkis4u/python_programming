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
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}
def is_resource_sufficient(oder_ingredients):
    """주문을 만들 수 있을때는 True를 반환하고, 재료가 부족할 경우에는 False를 반환한다."""
    for item in oder_ingredients:
        if oder_ingredients[item]>resources[item]:
            print(f"죄송합니다. {item}이 충분하지 않습니다.")
            return False
    return True

def process_coins():
    """투입된 동전으로 계산된 총액을 반환한다."""
    total = 0
    print("동전을 넣어주세요.")
    quarters = int(input("동전을 몇개 투입하시겠습니까?(쿼터 동전)"))
    dimes = int(input("동전을 몇개 투입하시겠습니까?(다임 동전)"))
    nikels = int(input("동전을 몇개 투입하시겠습니까?(니켈 동전)"))
    pennies = int(input("동전을 몇개 투입하시겠습니까?(페니 동전)"))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nikels + 0.01 * pennies
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    """지불이 승인되면 True를 반환하고, 금액이 부족하면 False를 반환한다."""
    if money_received >= drink_cost:
       change = round(money_received - drink_cost, 2)
       if change > 0:
           print(f"거스름돈 ${change}를 돌려드립니다.")
       global profit
       profit = profit + drink_cost
       return True
    else:
        print(f"죄송합니다. 금액이 부족합니다. 돈이 환불되었습니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """자원(resources)에서 필요한 재료(order_ingredients)를 차감한다."""
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print(f"여기 {drink_name}가 나왔습니다. 즐기세요.")

#menu = ["espresso", "latte", "cappuccino"]
#print(menu)

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
    else:
        print("잘못입력하셨습니다. 다시 입력해주세요") 