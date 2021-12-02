horizontal = 0
depth = 0
aim = 0

with open("input.txt") as input:
    for i in input:  
        move = i.strip().split(' ')
        if move[0] == 'forward':
            horizontal += int(move[1])
            depth += int(move[1]) * aim 
        elif move[0] == 'up':
            aim -= int(move[1])
        elif move[0] == 'down':
            aim += int(move[1])

print(horizontal*depth)