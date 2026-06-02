def get_fizz_buzz(n):
    my_fizz_buzz = []
    if not (1 <= n <= 10000):
        return []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            my_fizz_buzz.append("FizzBuzz")
        elif i % 3 == 0:
            my_fizz_buzz.append("Fizz")
        elif i % 5 == 0 :
            my_fizz_buzz.append("Buzz")
        else:
            my_fizz_buzz.append(f"{i}")

    return my_fizz_buzz



def main():
    print(get_fizz_buzz(0))
    print(get_fizz_buzz(1))
    print(get_fizz_buzz(5))
    print(get_fizz_buzz(20))
    print(get_fizz_buzz(10000))
    print(get_fizz_buzz(10001))


if __name__ == "__main__":
    main()