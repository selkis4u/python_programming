MENU = (('아메리카노', 4500), ('카페라떼', 5000), ('녹차', 4000))

print(f"{'='*30}")
print(f"{'MENU':^26}")
print(f"{'='*30}")
print(f"{MENU[0][0]:<12} {MENU[0][1]:>8,}")
print(f"{MENU[1][0]:<12} {MENU[1][1]:>8,}")
print(f"{MENU[2][0]:<12} {MENU[2][1]:>8,}")
print(f"{'='*30}")

num = int(input("메뉴번호: "))
qty = int(input("수량: "))

name, price = MENU[num - 1]
order_amount = qty * price

order_names = [name]
order_quantities = [qty]
order_amounts = [order_amount]

print(name, price)
print(order_names, order_quantities, order_amounts)

num2 = int(input("메뉴번호: "))
qty2 = int(input("수량: "))

name2, price2 = MENU[num2 - 1]
order_amount2 = qty2 * price2

order_names.append(name2)
order_quantities.append(qty2)
order_amounts.append(order_amount2)

print(name2, price2)
print(order_names, order_quantities, order_amounts)
print(f"주문항목수: {len(order_names)}건")

total = sum(order_amounts)
tax = int(total * 0.1)
total_money = total + tax

print("="*34)
print(f"{'영수증':^30}")
print("="*34)
print(f"{order_names[0]:<12} {order_quantities[0]:>4}개"
    f"{order_amounts[0]:>11,}원")
print(f"{order_names[1]:<12} {order_quantities[1]:>4}개"
    f"{order_amounts[1]:>11,}원")
print("-"*34)
print(f"{'주문금액':<16} {total_money:>13,}원")
print(f"{'부가세(10%)':<16} {tax:>13,}원")
print(f"{'결제금액':<16} {total_money:>13,}원")
print("="*34)