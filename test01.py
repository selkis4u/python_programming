
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