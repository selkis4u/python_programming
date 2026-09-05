from collections import deque

queue = deque() # 재생 대기열 - 큐
history = [] # 재생이력 - 스택
now = None # 현재재생곡

def show_status(now):
    """현재곡,대기열,이력"""

    line_double = "=" * 44
    line_single = "-" * 44

    print(line_double)
    print("MY PLAYLST".center(44))
    print(line_double)

    now_title = now if now is not None else ("없음")
    print(f"{'현재재생':<8} {now_title:>18}")
    print(line_single)

    print(f"{'대기열':<8} {len(queue):>18}곡 (먼저넣은 곡부터 재생)")
    if len(queue) == 0:
        print("(비어있음)")
    else:
        for i, title in enumerate(queue, 1):
            print(f"{i}. {title}")
    print(line_single)

    print(f"{'재생이력':<8} {len(history):>18}곡 (최근에 들은 곡부터)")
    if len(history) == 0:
        print("(비어있음)")
    else:
        for i, title in enumerate(reversed(history), 1):
            print(f"{i}. {title}")
    print(line_double)

def add_song(title):
    """대기열 맨뒤에 추가 (큐)"""

    queue.append(title)
    print(f"'{title}'을 (를) 대기열 맨 뒤에 추가했습니다. (총 {len(queue)}곡)")


def play_next(now):
    """다음곡 재생(큐+스택)"""

    if len(queue) == 0:
        print(f"대기열이 비어있습니다.")
        return now

    if now is not None:
        history.append(now)

    now = queue.popleft()
    print(f"재생: '{now}'")
    return now

def play_prev(now):
    """이전곡으로 (스택+큐)"""

    if len(history) == 0:
        print("이전 재생곡이 없습니다.")
        return now

    if now is not None:
        queue.appendleft(now)

    now = history.pop()
    print(f"이전곡 재생: '{now}'")
    return now

def add_urgent(title):
    """대기열 맨앞에 넣기"""

    queue.appendleft(title)
    print(f"'{title}'을(를) 대기열 맨 앞에 넣었습니다. (총 {len(queue)}곡)")

def rotate_queue(n):
    """대기열 순서 회전"""

    if len(queue) == 0:
        print("대기열이 비어 있습니다.")
        return
    
    queue.rotate(n)
    print(f"대기열을 {n}칸 회전했습니다.")
    print(list(queue))

# 메뉴루프
"""while문으로 조립"""

MENU = """
1.곡추가  2.다음곡  3.이전곡
4.맨앞에넣기 5.대기열회전 6.현재상태 0.종료
"""

while True:
    print(MENU)
    menu = input("번호를 선택하세요: ")
    if menu == '1':
        title = input("추가할 곡 제목: ")
        add_song(title)

    elif menu == '2':
        now = play_next(now)

    elif menu == '3':
        now = play_prev(now)

    elif menu == '4':
        title = input("맨앞에 추가할 곡 제목: ")
        add_urgent(title)

    elif menu == '5':
        rotate_num = int(input("회전할 칸 수를 입력하세요: "))
        rotate_queue(rotate_num)

    elif menu == '6':
        show_status(now)

    elif menu == '0':
        print("종료합니다.")
        break

    else:
        print("없는 번호입니다.")