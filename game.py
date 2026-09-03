answer = 37
count = 0
history = []

while count < 5:
    count = count + 1
    guess = int(input(f"[{count}/5] 숫자를 입력하세요: "))
    history.append(guess)
    if guess == answer:
        print(f"정답입니다.!{count}번 만에 맞추셨습니다.")
        break    
    elif guess < answer:
        print("UP! 더 큰 수를 입력하세요.")
    else:
        print("DOWN! 더 작은 수를 입력하세요.")  
        
too_big = [g for g in history if g > answer]
too_small = [g for g in history if g < answer]

result = "성공" if guess == answer else "실패"
   

print("="*34)
print(f"{'게임결과':^34}")
print("="*34)
print(f"{'정답':<14} {answer:>8}")
print(f"{'시도횟수':<14} {count:>8}")
print(f"{'결과':<14} {result:>8}")
print("-"*34)
print(f"{'입력기록':<14} {str(history):>8}")
print(f"{'너무 큰 수':<14} {len(too_big):>8}")
print(f"{'너무 작은 수':<14} {len(too_small):>8}")
print("="*34)