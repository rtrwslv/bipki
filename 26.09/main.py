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

print(counter("aaBbcc"), counter_2("aaBbcc"))