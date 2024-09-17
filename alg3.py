def barometer_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return barometer_fibonacci(n - 1) + barometer_fibonacci(n - 2)

if __name__=='__main__':
    print(barometer_fibonacci(int(input())))