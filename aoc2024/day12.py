def neighbours(grid, x):
    """valid neighbours of a cell"""
    return [x + m for m in [1, +1j, -1j, -1] if x + m in grid]


def flood(grid, cell):
    """Flood fill from cell to find all cells in region"""
    q, seen = [cell], set()
    while q:
        cell = q.pop(0)
        seen.add(cell)
        for move in neighbours(grid, cell):
            if move not in seen and move not in q and grid[move] == grid[cell]:
                q += [move]
    return seen


def perimeter(grid, region):
    perim = 0
    for cell in region:
        bounds = [cell + m for m in [1, +1j, -1j, -1]]
        perim += len([x for x in bounds if x not in grid or grid[x] != grid[cell]])
    return perim


def bounds(grid, cell):
    bounds = [1, +1j, -1j, -1]
    return [x for x in bounds if cell + x not in grid or grid[cell + x] != grid[cell]]


def sides(grid, region):
    sides = 0
    for cell in region:
        bnds = set(bounds(grid, cell))
        lu = [cell + m for m in [-1j, -1]]
        nbs = [x for x in lu if x in grid and grid[x] == grid[cell]]
        for nb in nbs:
            bnds -= set(bounds(grid, nb))
        sides += len(bnds)
    return sides


def regions(grid):
    todo = list(grid.keys())
    regions = []
    while todo:
        cell = todo[0]
        region = flood(grid, cell)
        todo = [x for x in todo if x not in region]
        regions += [{"type": grid[cell], "cells": region}]
    return regions


def part_a(data):
    grid = data.grid()
    res = 0
    for region in regions(grid):
        res += len(region["cells"]) * perimeter(grid, region["cells"])
    return res


def part_b(data):
    grid = data.grid()
    res = 0
    for region in regions(grid):
        res += len(region["cells"]) * sides(grid, region["cells"])
    return res
