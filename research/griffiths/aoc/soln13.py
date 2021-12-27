import numpy as np
import pathlib
import re
import sys
from typing import TypeVar
 
C = TypeVar("list[tuple[int, int]]")
 
 
def parse(puzzle_input: str) -> tuple[C, C]:
    """ Parse input """
    dots, instructions = puzzle_input.split('\n\n')
    # Process coordinates
    coords = []
    for dot in dots.split('\n'):
        x, y = [int(d) for d in dot.split(',')]
        coords.append((x, y))
    # Process instructions
    folds = []
    pattern = re.compile(r"fold along (x|y)=(\d+)")
    for fold in instructions.split('\n'):
        match = re.search(pattern, fold)
        direction, value = match.groups()
        if direction == 'x':
            folds.append((int(value), 0))
        elif direction == 'y':
            folds.append((0, int(value)))
    return (coords, folds)
 
 
def make_grid(coords: C) -> 'np.ndarray[int]':
    """ Work out dimensions of inital gird, retun as zeroed array """
    exes, whys = [], []
    for (x, y) in coords:
        exes.append(x)
        whys.append(y)
    return np.zeros((max(whys) + 1, max(exes) + 1), dtype=int)
 
 
def update_grid(coords: C, grid: 'np.ndarray[int]') -> None:
    """ Change grid coords to 1 based on input """
    for (x, y) in coords:
        grid[y][x] = 1
 
 
def split_grid(
        grid: 'np.ndarray[int]',
        fold: tuple[int, int]) -> tuple['np.ndarray[int]', 'np.ndarray[int]']:
    """ Return a grid split either x or y axis """
    x, y = fold
    if x == 0:
        return (grid[:y], grid[y + 1:][::-1])
    elif y == 0:
        return (grid[:, :x], np.flip(grid[:, x + 1:], 1))
 
 
def part1(data: tuple[C, C]) -> int:
    """ Solve part 1 """
    coords, folds = data
    page = make_grid(coords)
    # Add coords to grid
    update_grid(coords, page)
    first_half, second_half = split_grid(page, folds[0])
    combined = np.where(second_half == 1, second_half, first_half)
    return np.count_nonzero(combined == 1)
 
 
def printable(num: int) -> str:
    """ Return a string dependent on value of num """
    return "#" if num == 1 else " "
 
 
def print_grid(grid: 'np.ndarray[int]') -> None:
    """ Print grid """
    for row in grid:
        print("".join(printable(val) for val in row))
 
 
def part2(data: tuple[C, C]) -> str:
    """ Solve part 2 """
    coords, folds = data
    page = make_grid(coords)
    # Add coords to grid
    update_grid(coords, page)
    for fold in folds:
        first, second = split_grid(page, fold)
        page = np.where(second == 1, second, first)
    print_grid(page)
    answer = input("Write down the code above: ")
    return answer
 
 
def solve(puzzle_input: str) -> tuple[int, str]:
    """ Solve the puzzle for the given input """
    data = parse(puzzle_input)
    solution1 = part1(data)  # Correct answer was 682 (with my data)
    solution2 = part2(data)  # Correct answer was "FAGURZHE" (with my data)
 
    return solution1, solution2
 
 
if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print('\n'.join(str(solution) for solution in solutions))
