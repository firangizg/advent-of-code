with open("input.txt") as input:
    depths = [int(line.strip()) for line in input]

# count the 3 measurement sums
sums = []
for i in range(len(depths)):
    sums.append(sum(depths[i:i + 3]))

# count how many sums are larger than others
larger_sum = 0
for i in range(1, len(sums)):
    if sums[i] > sums[i - 1]:
        larger_sum += 1

print(larger_sum)