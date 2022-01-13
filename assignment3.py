import re

file1 = open("regex_sum_1374017.txt", "r")
Lines = file1.readlines()

sum = 0

for line in Lines:
    result = re.findall("[0-9]+", line)
    # print(result)
    if len(result) > 0:
        # print(result)
        for r in result:
            sum += int(r)

print(sum)