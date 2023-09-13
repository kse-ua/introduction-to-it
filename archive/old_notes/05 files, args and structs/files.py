import sys

file = open(sys.argv[1], "r")
lines = file.readlines()
total = 0
for line in lines:
    data = line.split(" ")
    total += int(data[2])

print("Average salary", total / len(lines))

result_file = open(sys.argv[2], "w")
result_file.write()