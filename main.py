import re
import time, random
def check_time(nums):
    time1 = time.time()
    nums.sort()
    done_time = time.time() - time1
    print(done_time)


def degenerator(lenght):
    new_list = []
    for i in range(lenght):
        new_list.append(random.randint(0, 100))
    return new_list

def announce(function):
    def new_f(*args, **kwargs):
        name = function.__name__
        print("выполняется", name)
        result = function(*args, **kwargs)
        print(args, kwargs)
        return result
    return new_f

def sum_two(a, b):
    return a + b


def gen(n, step = 1):
    s = 0
    for i in range(1, n, step):
        if i % 2 != 0:
            yield i
#for i in gen(10, step = 6):
    #print(i)

def cool_filter(words):
    new_list = []
    for word in words:
        if word.__contains__("a"):
            new_list.append(word)
    return new_list



def going_up(line):
    line = line.split(" ")
    for i in range(len(line)):
        line[i] = line[i].capitalize()
    return " ".join(line)
        
nums = [0, 1, 2, 3, 4, 5]
def find_my_num():
    while True:
        user_input = input("Введите индекс [q для выхода]: ")
        if user_input == "q":
            break
        try:
            print('Ваше число: ', nums[int(user_input)])
        except ValueError:
            print("Вводить можно только целые числа")
        except IndexError:
            print("Вы превысили длину списка. Самый большой индекс:", len(nums) - 1)


import random
import time
def degenerator(n, start, end):
    i = 0
    while i < n:
        yield random.randint(start, end)
        i += 1

def round(number):
    if number % 1 >= 0.5:
        print(int(number) + 1)
    else:
        print(int(number))


def timer(function):
    def new_f(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        time_result = time.time() - start_time
        print(time_result)
        return result
    return new_f

@timer
def phone_validation(phone_num):
    file = open("test.txt", "w")
    file.write("len(phone_num) =" + str(len(phone_num)) + "\n")
    if len(phone_num) == 16:
        file.write("phone_num[0:3]=" + phone_num[0:3] + "\n")
        if (phone_num[0:3] == "+7("):
            if (phone_num[6] == ")"):
                if (phone_num[10] == "-") & (phone_num[13] == "-"):
                    return True
    return False

print(phone_validation("+7(960)107-96-85"))