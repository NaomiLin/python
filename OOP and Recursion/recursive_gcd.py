

def recursive_gcd(m, n, count=0):
    count += 1
    print(count, ":", m, n)
    if n == 0:
        print(f"The greatest common divisor is {m}")
        return m
    return recursive_gcd(n, m % n, count)


def main():
    recursive_gcd(39, 1001)


main()
