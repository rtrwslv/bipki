import time

def time_of_function(function, function2):
    def wrapped(string):
        start_time = time.perf_counter_ns()
        function(string)
        res = time.perf_counter_ns() - start_time
        start_time = time.perf_counter_ns()
        function2(string)
        res2 = time.perf_counter_ns() - start_time
        if res < res2: print(res)
        else: print(res2)
    return wrapped

def counter(string):
    st = string.lower()
    res = 0
    for i in set(st):
        if st.count(i) > 1:
            res += 1
    return(res)


def counter_2(string):
    repeating_letters = []
    res = 0
    for letter in string.lower():
        if letter in repeating_letters:
            res += 1
        else:
            repeating_letters.append(letter)
    return(res)

res = time_of_function(counter, counter_2)

res("aabbcc")