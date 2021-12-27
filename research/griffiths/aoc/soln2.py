steps = [step.strip().split(' ') for step 
    in open('input02.txt', 'r').readlines()]
steps = [[change, int(value)] for change, value in steps]

# part 1
horizontal, depth = 0,0
for change, value in steps:
    if change == 'forward':
        horizontal += value
    elif change == 'down':
        depth += value
    else:
        depth -= value
print('part 1:', horizontal * depth)

# part 2
aim, horizontal, depth = 0,0,0
for change, value in steps:
    if change == 'forward':
        horizontal += value
        depth += aim * value
    elif change == 'down':
        aim += value
    else:
        aim -= value
print('part 2:', horizontal * depth)
