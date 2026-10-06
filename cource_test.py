python_list = ['김민준', '이서연', '박도윤', '이서연', '최지우']
web_list = ['이서연', '박도윤', '한지민', '한지민']

python_set = set(python_list)
web_set = set(web_list)

print(f"파이썬 신청 {len(python_list)}건 -> 실제 {len(python_set)}명")
print(f"웹개발 신청 {len(web_list)}건 -> 실제 {len(web_set)}명")

print(sorted(python_set))
print(sorted(web_set))

both_list = python_set & web_set
all_student = python_set | web_set
only_python = python_set - web_set
only_web = web_set - python_set
one_only = python_set ^ web_set

print(f"둘다 수강: {sorted(both_list)}")
print(f"전체수강: {sorted(all_student)}")
print(f"파이썬만: {sorted(only_python)}")
print(f"웹개발만: {sorted(only_web)}")
print(f"한과목만: {sorted(one_only)}")

name = '이서연'
print(f"이서연 파이썬 수강? {bool(name in python_set)}")
print(f"이서연 웹개발 수강? {bool(name in web_set)}")
print(f"이서연 둘다 수강? {bool(name in python_set & web_set)}")
print(f"이서연 하나라도 수강? {bool(name in python_set | web_set)}")
print(f"이서연 미수강? {bool(name not in all_student)}")
print(f"교집합은 비었나? {not bool(python_set & web_set)}")

report = {'python':len(python_set), 'web':len(web_set), 'both':len(both_list), 'total':len(all_student)}
print(report)
print("="*32)
print(f"{'수강현황':^24}")
print("="*32)
print(f"{'파이썬':<14} {report['python']:>10}명")
print(f"{'웹개발':<14} {report['web']:>10}명")
print("-"*32)
print(f"{'둘다수강':<14} {report['both']:>10}명")
print(f"{'전체인원':<14} {report['total']:>10}명")
print("="*32)
print(f"중복수강률: {(report['both']/report['total']*100):.1f}%")