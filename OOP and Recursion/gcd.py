

def gcd(m, n):
    step = 0
    while n != 0:
        step += 1
        print(f'{step}: {m}, {n}')
        temp = n
        n = m % n
        m = temp
    step += 1
    print(f'{step}: {m}, {n}')
    return m


def main():
    m = 1001
    n = 39
    ans = gcd(m, n)
    print(f"The greatest common divisor of {m} and {n} is {ans}")


main()
