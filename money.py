import sys

FILE = "records.txt"
CATEGORIES = ["식비", "교통", "문화", "기타"]

def add_record(date, category, item, amount):
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"{date},{category},{item},{amount}\n")
    print(f"기록했습니다.({date} {category} {item} {amount:,}원)")

def load_records():
    records = []
    with open(FILE, "a", encoding="utf-8"):
        pass
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            date, category, item, amount = line.split(",")
            records.append({"date":date, "category":category, "item":item, "amount":int(amount)})            
    return records

def show_all():
    records = load_records()
    if not records:
        print("아직 기록이 없습니다.")
        return
    
    print("="*46)
    print(f"{'용돈기록장':^23}")
    print("="*46)
    print(f"{'번호':<5}{'날짜':<12}{'분류':<7}{'내용':<13}{'금액':>9}")
    print("-"*46)
    for i, r in enumerate(records, 1):
        print(f"{i:<5}{r['date']:<12}{r['category']:<7}{r['item']:<13}{r['amount']:>9,}")
    print("-"*46)
    total = sum([r['amount'] for r in records])
    print(f"{'합계':<5}{total:<13}")
    print("="*46)

def summary():
    records = load_records()
    if not records:
        print("아직 기록이 없습니다.")
        return

    total = 0
    by_category = {}

    for r in records:
        c = r["category"]
        amount = r["amount"]
        total += amount
        if c in by_category:
            by_category[c] += amount
        else:
            by_category[c] = amount

    sorted_cat = sorted(by_category, key=lambda k:by_category[k], reverse=True)

    print("-"*46)
    print(f"{'분류별지출':^23}")
    print("-"*46)

    for c in sorted_cat:
        amt = by_category[c]
        ratio = (amt / total) * 100
        print(f"{c:<6}{amt:8,}원{ratio:7.1f}%")
    print("-"*46)

    count = len(records)
    avg = int(total / count)

    print(f"{'총 지출':<6}{total:>8,}원")
    print(f"{'기록 수':<6}{count:>8}건")
    print(f"{'평균':<6}{avg:>8,}원")
    print("-"*46)
 
def search(word):
    records = load_records()

    found = [r for r in records if word in r ["item"] or word in r["category"]]
    print(f"'{word}'검색 결과 : {len(found)}건")
    for i, r in enumerate(found, 1):
        print(f"{i}. {r['date']} {r['category']} {r['item']} {r['amount']:,}원")

    if len(found) > 0:
        total = sum([r['amount'] for r in found])
        print(f"합계 {total:,}원")

# 메뉴루프
    # sys.argv
args = sys.argv[1:]

if len(args) > 0:
    
    if args[0] == "list":
        show_all()
    elif args[0] == "sum":
        summary()
    elif args[0] == "find" and len(args) > 1 :
        search(args[1])
    else:
        print("사용법: python money.py [list | sum | find 검색어]")

else:
    while True:
        print("1. 기록추가 2.전체보기 3.통계 4.검색 0.종료")
        menu = input("번호를 선택하세요: ")

        if menu == "1":
            date = input("날짜(예: 2026-08-24): ")
            print(f"분류:{CATEGORIES}")

            category = input("분류: ")
            if category not in CATEGORIES:
                print("분류항목에 없습니다.")
                continue

            item = input("내용: ")
            amount = int(input("금액: "))
            add_record(date, category, item, amount)

        elif menu == "2":
            show_all()

        elif menu == "3":
            summary()

        elif menu == "4":
            word = input("검색어: ")
            search(word)

        elif menu == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("없는 번호입니다. 다시 입력해주세요.")