
Save New Duplicate & Edit Just Text Twitter
import sys

file = open('input.txt')

algo_string = next(file).strip()
if algo_string[0] == ".":
    algo = [
      {i for i, p in enumerate(algo_string) if p == "#"},
    ]
elif algo_string[-1] == ".":
    algo = [
        {i for i, p in enumerate(algo_string) if p == "."},
        {i^511 for i, p in enumerate(algo_string) if p == "#"},
    ]
else:
    print("Infinity")
    sys.exit()

image = {(x, y) for y, line in enumerate("".join(file).strip().split("\n")) for x, p in enumerate(line) if p == "#"}

for i in range(50):
    (x1, x2), (y1, y2) = ((min(d), max(d)) for d in zip(*image))
    image = {(x, y) for x in range(x1-1, x2+2) for y in range(y1-1, y2+2) if sum(1<<(8-z) for z in range(9) if (x-1+z%3, y-1+z//3) in image) in algo[i%len(algo)]}

(x1, x2), (y1, y2) = ((min(d), max(d)) for d in zip(*image))
for y in range(y1, y2+1):
    print("".join(("#" if (x, y) in image else ".") for x in range(x1, x2+1)))

print(len(image))
