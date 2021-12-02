# create an array called depth of all the numbers in input file
with open("input.txt") as input:
    depth = [int(line.strip()) for line in input]

# count how many increases there are
count = 0
for i in range(1, len(depth)):
    if depth[i] > depth[i - 1]:
        count += 1
    else:
        continue

print(count)