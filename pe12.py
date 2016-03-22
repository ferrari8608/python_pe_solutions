#!/usr/bin/env python

import sys

def factor_count(triangle: int) -> int:
    factors = 0
    for possible_factor in range(1, triangle // 2):
        if not triangle % possible_factor:
            factors += 2
    return factors

def main():
    goal = 500  # Factors
    count = 1
    triangle = 0
    factors = 0

    while factors < goal:
        triangle += count
        count += 1
        factors = factor_count(triangle)
        print(triangle, "+", count, "has", factors, "factors")

    print(triangle, "has", factors, "factors")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('')
