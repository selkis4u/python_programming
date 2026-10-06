SUBJECT = ('국어', '영어', '수학')
names = ['김민준', '이서연', '박도윤']
scores = [88, 95, 76]

print(f"과목: {SUBJECT}")
print(f"등록된 학생: {len(names)}명")
print(f"첫번째 학생: {names[0]}/ {scores[0]}점")
print(f"마지막 학생: {names[-1]}/ {scores[-1]}점")

add_name = input("추가할 학생 이름 :").strip()
add_scores = int(input("점수: "))
names.append(add_name)
scores.append(add_scores)

print(f"{names}")
print(f"{scores}")
print(f"이제 {len(names)}명입니다.")

total = sum(scores)
number = len(scores)
average = total / number
highest = max(scores)
lowest = min(scores)

print(f"총점: {total}점")
print(f"평균: {average:.1f}점")
print(f"최고점: {highest}점 / 최저점: {lowest}점")

max_number = scores.index(highest)
max_name = names[max_number]
find_index = names.index('박도윤')

sort_scores = sorted(scores, reverse= True)
sort_names = sorted(names)

print(f"1등: {max_name}({highest}점) - scores[{max_number}]자리")
print(f"박도윤의점수: {scores[find_index]}점(names[{find_index}])")
print(f"점수 내림차순: {sort_scores}")
print(f"이름 가나다순: {sort_names}")

print(f"="*30)
print(f"{'성적리포트':^24}")
print(f"="*30)
print(f"{'이름':<12} {'점수':>8}")
print(f"-"*30)
print(f"{names[0]:<12} {scores[0]:>8}")
print(f"{names[1]:<12} {scores[1]:>8}")
print(f"{names[2]:<12} {scores[2]:>8}")
print(f"{names[3]:<12} {scores[3]:>8}")
print(f"-"*30)
print(f"{'평균':<12} {average:>8.1f}")
print(f"{'1등':<12} {max_name:>8}")

min_num = scores.index(lowest)
low_name = names.pop(min_num)
low_num = scores.pop(min_num)
print(f"제외: {low_name} ({low_num}점)")

names.insert(0, '한지민')
scores.insert(0, 100)

print(names)
print(scores)
total = sum(scores)
average = total / len(names)
print(f"평균: {average:.1f}점")

print(f"{scores.count(88)}명")