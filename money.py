import sys

FILE = "records.txt"
CATEGORIES = ["식비", "교통", "문화", "기타"]

def add_record(date, category, item, amount):
    # add.record = input("date","catrgory", "item", "amount")
    
    with open(FILE, "a", encoding="utf-8") as f:
    # record = input("date","catrgory", "item", "amount")
        f.write(f"{date},{category},{item},{amount}\n")
            # for line in f:
        print(f"기록했습니다.{line}\n")


# load_records()

# show_all()

# summary()

# search(word)

# 메뉴루프

# sys.argv cjfl
