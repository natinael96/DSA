import textwrap

def wrap(string, max_width):
    count = 0
    new_str = ""
    for i in string:
        if count < max_width:
            new_str += i
            count+=1
        if count == max_width:
            new_str += "\n"
            count = 0
    return new_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)