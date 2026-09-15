import numpy as np

# 1. 단일 샘플의 가중합 계산 (스칼라 반복문 vs 벡터 내적)
x = np.array([2.0, 3.0, -1.5])  # 특성 벡터 (3차원)
w = np.array([0.5, -0.8, 1.2])  # 가중치 벡터
b = 0.25                         # 편향(Bias)

# 방법 A: 수학적 수식 그대로 벡터 내적 수행 (np.dot)
net_dot = np.dot(w, x) + b

# 방법 B: 파이썬 @ 행렬곱 연산자 활용
net_matmul = w @ x + b

print(f"가중합 (np.dot)  : {net_dot:.4f}")
print(f"가중합 (@ 연산자): {net_matmul:.4f}")


# 2. 미니배치(Batch) 데이터의 병렬 가중합 계산
# shape: (4개 데이터 샘플, 3개 특성)
X_batch = np.array([
    [0.0, 0.0, 1.0],
    [1.0, 2.0, 0.5],
    [2.0, -1.0, 0.0],
    [-1.0, 1.5, 2.0]
])

# 배치 행렬곱: (4, 3) @ (3,) + scalar -> (4,)
# 브로드캐스팅(Broadcasting)에 의해 편향 b는 4개 샘플 각각에 자동 가산됨
batch_net = X_batch @ w + b

print("\n=== 미니배치 가중합 결과 ===")
for idx, val in enumerate(batch_net):
    print(f"Sample {idx+1} Net Input: {val:.4f}")
# from sklearn.datasets import load_diabetes
# df = load_diabetes(as_frame=True).frame
# print(df.head())

# import os, sklearn.datasets as ds
# print(os.path.join(os.path.dirname(ds.__file__),'data'))


# class Counter:
#     def __init__(self):
#         self.count = 0
#     def __call__(self):
#         self.count += 1
#         return self.count


# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         print(count)
#         return count
#     return counter

# a = Counter()
# b = Counter()

# print (a())
# print (a())
# print (a())

# print (b())
# b()

# print (a())



#count = make_counter()
# print(count)

# score = "python"

# def level_up():
#     #score = 0
#     #score += 10
#     print(f"hello: {score}")

# level_up()
# print(f"함수외부: {score}")

# def mul(m):
#     def wrapper(n):
#         return m*n
#     return wrapper

# if __name__ == "__main__":
#     mul3 = mul(3)
#     mul5 = mul(5)

#     print(mul3(10))
#     print(mul5(10))
        
    
# import time
# import threading
# import multiprocessing

# def long_task():
#     for i in range(1, 6):
#         time.sleep(1)
#         print("working:%s\n"%i)

# if __name__ == "__main__":

#     print("Start")
#     start = time.time()

# #threads = []
#     processes = []

#     for i in range(5):
#         p = multiprocessing.Process(target=long_task)
#         processes.append(p)
#         #t = threading.Thread(target=long_task)
#         #threads.append(t)

#     for p in processes:
#         p.start()

#     for p in processes:
#         p.join()

#     end = time.time()
#     print("End")
#     print("걸린시간: %.2f초"%(end - start))

# import time

# def long_task():
#     for i in range(1, 5):
#         time.sleep(1)
#         print("working:%s\n"%i)

# print("Start")
# start = time.time()

# for i in range(5):
#     long_task()

# end = time.time()
# print("End")
# print("걸린시간: %.2f초"%(end - start))



# from operator import itemgetter

# students = [
#     {"name":"jane", "age":22, "grade":'A'},
#     {"name":"dave", "age":32, "grade":'B'},
#     {"name":"sally", "age":17, "grade":'A'},
#     ]

# result = sorted(students, key=itemgetter('age'))
# print(result)

# import functools

# data = [1, 2, 3, 4, 5]
# result = functools.reduce(lambda x, y: x + y, data, 10)
# print(result)

# import random

# card = [1, 2, 3, 4, 5, 6]
# random.shuffle(card)
# print(card)




# file = None

# try:
#     file = open('foo.txt', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("파일없음")
# finally:
#     if file:
#         file.close()
#         print("파일닫힘")
#     else:
#         print("Do nothing!")
# try:
#     f = open('foo.txt', 'w')
#     pass
# finally:
#     f.close()
    
# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# try:
#     number = int(input("번호: "))
# except ValueError as e:
#     print(e)
#     print("숫자를 입력해주세요.")
# print("계속진행")

# # ValueError: invalid literal for int()