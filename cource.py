python_list = ['김민준', '이서연', '박도윤', '이서연', '최지우']
web_list = ['이서연', '박도윤', '한지민', '한지민']

python_set = set(python_list)
web_set = set(web_list)

print(f"파이썬 신청 {len(python_list)}명 -> 실제 {len(python_set)}명")
print(f"웹개발 신청 {len(web_list)}명 -> 실제 {len(web_set)}명")
print(sorted(python_set))
print(sorted(web_set))

both = python_set&web_set
all_students = python_set|web_set
only_py = python_set-web_set
only_web = web_set-python_set
one_only = python_set^web_set

print(f"둘다수강: {both}")
print(f"전체수강생: {all_students}")
print(f"파이썬만: {only_py}")
print(f"웹개발만: {only_web}")
print(f"한과목만 : {one_only}")

name = '이서연'
print(f"{name} 파이썬 수강? {name in python_set}")
print(f"{name} 웹개발수강? {name in web_set}")
print(f"{name} 둘 다 수강? {name in python_set and name in web_set}")
print(f"{name} 하나라도 수강? {name in python_set or name in web_set}")
print(f"{name} 미수강? {name not in all_students}")
print(f"교집합이 비었나? {not bool(both)}")

report = {'python':len(python_set), 'web':len(web_set), 'both':len(both), 'total':len(all_students)}
print(report)
print("=" *32)
print(f"{'수강현황':^16}")
print("=" *32)
print(f"{'파이썬':14}{report['python']:>10}명")
print(f"{'웹개발':14}{report['web']:>10}명")
print("-" *32)
print(f"{'둘다수강':14}{report['both']:>10}명")
print(f"{'전체인원':14}{report['total']:>10}명")
print("=" *32)
print(f"{'중복수강률':14}:{report['both']/report['total']*100:>10.1f}%")