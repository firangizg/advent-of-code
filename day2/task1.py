horizontal = 0
depth = 0

with open("input.txt") as input:
    for i in input:  
        move = i.strip().split(' ')
        if move[0] == 'forward':
            horizontal += int(move[1])
        elif move[0] == 'up':
            depth -= int(move[1])
        elif move[0] == 'down':
            depth += int(move[1])

print(horizontal*depth)
