def swap_case(s):
    new_s = ''
    for i in s:
        if i.isalpha():
            if i.isupper():
                new_s += i.lower()
            else:
                new_s += i.upper()
        else:
            new_s += i
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)