# Python 3.9 from functools import cache
from functools import lru_cache

# Pytho 3.9 @cache
@lru_cache(maxsize=32)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


def main():
    for i in range(200):
        print(i, fibonacci(i))


if __name__ == '__main__':
    main()
