import multiprocessing
import time


def heavy_calculation(task_id):
    total = sum(i * i for i in range(10_000_000))
    print(f"Task {task_id} 완료")
    return total


# 멀티프로세싱 작성 시 필수 가드 선언
if __name__ == "__main__":
    start = time.time()
    processes = []

    # CPU 코어 수만큼 독립 프로세스 생성 및 실행
    for i in range(4):
        p = multiprocessing.Process(target=heavy_calculation, args=(i,))
        processes.append(p)
        p.start()

    # 모든 자식 프로세스의 작업 완료 대기
    for p in processes:
        p.join()

    print(f"전체 병렬 연산 완료 시간: {time.time() - start:.2f}초")