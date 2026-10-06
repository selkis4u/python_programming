import random
# answer = 37
answer = random.randint(1, 100)
count = 0
history = []

while count < 5:
    count += 1
    guess = int(input(f"[{count}/5] 숫자를 입력하세요:(1~100): "))
    history.append(guess)

    if guess == answer:
        print(f"정답입니다.{count}번만에 맞히셨습니다.")
        break
    elif guess > answer:
        print("Down, 더 작은 수를 입력하세요.")
    else: 
        print("Up, 더 큰 수를 입력하세요.")

result = "성공" if guess == answer else "실패"
print(result)

# too_big = []
# for big in history:
#     if big > answer:
#         too_big.append(big)

too_big = [big for big in history if big > answer]
too_small = [small for small in history if small < answer]

print("="*34)
print(f"{'게임결과':^24}")
print("="*34)
print(f"{'정답':<14} {answer:>10}")
print(f"{'시도횟수':<14} {count:>10}")
print(f"{'결과':<14} {result:>10}")
print("-"*34)
print(f"{'입력기록':<14} {str(history):>10}")
print(f"{'너무큰수':<14} {len(too_big):>10}")
print(f"{'너무작은수':<14} {len(too_small):>10}")
print("="*34)