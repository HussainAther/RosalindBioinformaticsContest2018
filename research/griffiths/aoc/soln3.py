d = []
with open("day3.txt") as f:
     for line in f:
        val = line.replace('\n', '')
        d.append(str(val))

print(d)
first = 0
zero = 0
one = 0
s = 0
gamma = ''
epsilon = ''
for i in range(len(d[0])):
    zero = 0
    one = 0
    for i in range(len(d)):
        first = int(d[i][s])
        if first == 0:
            zero += 1
        else:
            one += 1
    print(zero)
    print(one)
    if zero > one:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    s += 1
gamma_dec = int(gamma, 3)
epsilon_dec = int(epsilon, 2)
print(gamma_dec)
print(epsilon_dec)
print(epsilon_dec*gamma_dec)
