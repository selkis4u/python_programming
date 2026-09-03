while True:
    item = input("어떤 커피를 드릴까요? (espresso/latte/cappuccino): ")
    if item not in menu:
        print("죄송합니다. 메뉴에 없는 커피입니다. 다시 선택해주세요.")
        continue
    elif item == "off":
        exit()
        
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