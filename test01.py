import time
import threading
import multiprocessing

def long_task():
    for i in range(1, 6):
        time.sleep(1)
        print("working:%s\n"%i)

if __name__ == "__main__":

    print("Start")
    start = time.time()

#threads = []
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=long_task)
        processes.append(p)
        #t = threading.Thread(target=long_task)
        #threads.append(t)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print("End")
    print("걸린시간: %.2f초"%(end - start))

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