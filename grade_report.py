SUBJECT = ('국어', '영어', '수학')
names = ['김민준', '이서연', '박도윤']
scores = [88, 95, 76]

print(f"과목: {SUBJECT}")
print(f"등록된 학생: {len(names)}명")
print(f"첫번째 학생: {names[0]} / {scores[0]}점")
print(f"마지막 학생: {names[-1]} / {scores[-1]}점")

new_name = input("추가할 학생 이름 : ")
new_scores = int(input("점수: "))

names.append(new_name)
scores.append(new_scores)

print(f"{names}")
print(f"{scores}")
print(f"이제 {len(names)}명입니다.")

total = sum(scores)
average = total/len(scores)
highest = max(scores)
lowest = min(scores)

print(f"총점 : {total}점 ")
print(f"평균 : {average:.1f} 점")
print(f"최고점 : {highest}점 / 최저점 : {lowest}점")

top_index = scores.index(highest)
top_name = names[top_index]
find_index = names.index('박도윤')

print(f"1등 :{top_name}({highest}점) - scores[{top_index}]자리")
print(f"박도윤의 점수 : {scores[find_index]}점 (names[{find_index}])")
print(f"점수 내림차순 : {sorted(scores, reverse=True)}")
print(f"이름 가나다순 : {sorted(names)}")

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
print(f"{'1등':<12} {top_name:>8}")
print(f"="*30)