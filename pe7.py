#!/usr/bin/env python

import sys

def main():
    prime_count = 0
    number = 1
    not_primes = set()

    while prime_count < 10001:
        number += 1
        if number not in not_primes:
            prime_count += 1
            not_primes.update(range(number * 2, 200000, number))

    print(number)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('')
