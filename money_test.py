import sys

FILE = "records.txt"
CATEGORIES = ["식비", "교통", "문화", "기타"]

def add_record(date, category, item, amount):
    with open(FILE, 'a', encoding='utf-8') as f:
        f.write(f"{date},{category},{item},{amount}\n")
        print(f"기록했습니다.{date},{category},{item},{amount:,}원")

def load_records():
    records = []
    with open(FILE, 'a', encoding='utf-8') as f:
        pass
    with open(FILE, 'r', encoding='utf-8') as f:
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
    
    total = sum(r["amount"] for r in records)
    
    print("="*46)
    print(f"{'용돈기록장':^46}")
    print("="*46)
    print(f"{'번호':<5}{'날짜':<12}{'분류':<7}{'내용':<13}{'금액':>9}")
    print("-"*46)
    for i, r in enumerate(records, 1):
        print(f"{i:<5}{r['date']:<12}{r['category']:<7}{r['item']:<13}{r['amount']:>9,}")
    print("-"*46)
    print(f"합계 {total:>9,}원")

def summary():
    records = load_records()
    if not records:
        print("기록이 없습니다")
        return

    total = 0
    by_category = {}
    for r in records:
        c = r['category']
        amount = r['amount']
        total += amount
        #by_category[c] = by_category.get(c, 0) + c_amount
        if c in by_category:
            by_category[c] += amount
        else:
            by_category[c] = amount
    sorted_c = sorted(by_category, key=lambda k: by_category[k], reverse=True)

    print("="*46)
    print(f"{'분류별지출':^46}")
    print("="*46)
    for c in sorted_c:
        amount = by_category[c]
        ratio = amount / total * 100
        print(f"{c:<5}{amount:>12,}원{ratio:>9.1f}%")
    print("="*46)
    print(f"총지출 {total:>9,}원")
    print(f"기록수 {len(records):>9}건")
    print(f"평균 {int(total/len(records)):>9,}원")

def search(word):
    records = load_records()
    found = [r for r in records if word in r["item"] or word in r["category"]]
    print(f"'{word}' 검색 결과: {len(found)}건")
    for i, r in enumerate(found, 1):
        print(f"{i}. {r['date']}{r['category']}{r['item']}{r['amount']:,}원")
    if len(found) > 0:
        total = sum(r['amount'] for r in found)
        print(f"합계 {total:,}원")
            