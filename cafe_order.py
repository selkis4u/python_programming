MENU = (('아메리카노', 4500), ('카페라떼', 5000), ('녹차', 4000))

print(f"="*30)
print(f"{'MENU':^26}")
print(f"="*30)
print(f"1.{MENU[0][0]:<12}{MENU[0][1]:>8,}원")
print(f"2.{MENU[1][0]:<12}{MENU[1][1]:>8,}원")
print(f"3.{MENU[2][0]:<12}{MENU[2][1]:>8,}원")
print(f"="*30)

num = int(input("메뉴번호: "))
qty = int(input("수량: "))
name,price = MENU[num - 1]
print(f"{name} {price}")

order_names = [name]
order_qtys = [qty]
order_amounts = [price * qty]
print(order_names, order_qtys, order_amounts)

num2 = int(input("메뉴번호: "))
qty2 = int(input("수량: "))
name2,price2 = MENU[num2 - 1]
order_names.append(name2)
order_qtys.append(qty2)
order_amounts.append(price2 * qty2)
print(order_names,order_qtys, order_amounts)
print(f"주문항목수 : {len(order_names)}건")

total = sum(order_amounts)
tax = int(total*0.1)

print(f"="*34)
print(f"{'영수증':^17}")
print(f"="*34)
print(f"{order_names[0]:<8}{order_qtys[0]:>4}개{order_amounts[0]:>11,}원")
print(f"{order_names[1]:<8}{order_qtys[1]:>4}개{order_amounts[1]:>11,}원")
print(f"-"*34)
print(f"{'주문금액':<16}{(total):>10,}원")
print(f"{'부가세(10%)':<16}{(tax):>10,}원")
print(f"{'결제금액':<16}{(total + tax):>10,}원")
print(f"="*34)