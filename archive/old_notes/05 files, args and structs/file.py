file = open("data.txt", 'r')
lines = file.readlines()
total = 0
for line in lines:
    print(line, end=" ")
    data = line.split(" ")
    data[2] = int(data[2])
    total += int(data[2])

print(total / len(lines))

result_file = open("result.txt", 'w')
result_file.write(str(total))
