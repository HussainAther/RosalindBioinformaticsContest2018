import itertools
import math
import re


def add(data):
    if " + " in data:
        data = f"[{data.split(' + ')[0]},{data.split(' + ')[1]}]"
    return data


def explode(data):
    offset = 0
    for p in re.findall("\[\d+,\d+\]", data):
        pair = re.search(re.escape(p), data[offset:])
        left_brackets = data[: pair.start() + offset].count("[")
        right_brackets = data[: pair.start() + offset].count("]")
        if left_brackets - right_brackets >= 4:
            x, y = pair.group()[1:-1].split(",")
            # split the string into two parts at the pair
            # flip left side around so we get the first num going backwards
            left = data[: pair.start() + offset][::-1]
            right = data[pair.end() + offset :]
            # look left
            search_left = re.search("\d+", left)
            if search_left:
                # need to find the rightmost match not the first
                amt = int(left[search_left.start() : search_left.end()][::-1]) + int(x)
                left = f"{left[:search_left.start()]}{str(amt)[::-1]}{left[search_left.end():]}"
            # look right
            search_right = re.search("\d+", right)
            if search_right:
                amt = int(right[search_right.start() : search_right.end()]) + int(y)
                right = (
                    f"{right[:search_right.start()]}{amt}{right[search_right.end():]}"
                )
            data = f"{left[::-1]}0{right}"
            break
        else:
            offset = pair.end() + offset
    return data


def split(data):
    dd = re.search("\d\d", data)
    if dd:
        left = data[: dd.start()]
        right = data[dd.end() :]
        left_digit = int(math.floor(int(dd.group()) / 2))
        right_digit = int(math.ceil(int(dd.group()) / 2))
        data = f"{left}[{left_digit},{right_digit}]{right}"
    return data


def reduce(data):
    exploded = explode(data)
    if exploded != data:
        return reduce(exploded)
    else:
        splitd = split(data)
        if splitd != data:
            return reduce(splitd)
        else:
            return splitd


def magnitude(data):
    while data.count(",") > 1:
        for p in re.findall("\[\d+,\d+\]", data):
            pair = re.search(re.escape(p), data)
            left_digit, right_digit = p[1:-1].split(",")
            data = f"{data[: pair.start()]}{int(left_digit) * 3 + int(right_digit) * 2}{data[pair.end() :]}"
    left_digit, right_digit = data[1:-1].split(",")
    return int(left_digit) * 3 + int(right_digit) * 2


# PART 1
data = open("day18.in").read().strip().split("\n")
p1 = list(data)
sum = ""
final_sum = ""
while p1:
    line1 = p1.pop(0)
    if not final_sum:
        line2 = p1.pop(0)
        final_sum = f"{line1} + {line2}"
    else:
        final_sum = f"{final_sum} + {line1}"
    final_sum = reduce(add(final_sum))
print(f"Part 1: {magnitude(final_sum)}")

# PART 2
p2 = list(data)
magnitudes = set()
pairs = list(itertools.permutations(p2, 2))
for pair in pairs:
    final_sum = reduce(add(f"{pair[0]} + {pair[1]}"))
    magnitudes.add(magnitude(final_sum))
print(f"Part 2: {max(magnitudes)}")
