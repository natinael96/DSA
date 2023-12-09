nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
allNums = []

while True:
    n = input()
    if n.strip() == "":
        break

    first = None
    second = None

    for i in range(len(n)):
        if n[i].isnumeric():
            if first is None:
                first = int(n[i])
            second = int(n[i])
        else:
            for indx, j in enumerate(nums):
                if i + len(j) <= len(n):
                    curr = n[i:i+len(j)]
                    if curr == j:
                        if first is None:
                            first = indx + 1
                        second = indx + 1
                        break  

    if first is not None and second is not None:
        allNums.append(int(str(first) + str(second)))


sum_calibration = sum(allNums)
print(f"Calibration values: {allNums}")
print(f"Sum of calibration values: {sum_calibration}")
