''' Base case '''

def fib2(n: int) -> int:
    if n < 2:   # base case
        return n
    return fib2(n-2) + fib2(n-1)

if __name__ == "__main__":
    print(fib2(5)) # Takes 15 recursive calls to finish
    print(fib2(10)) # Takes 177 recursive calls to finish
    print(fib2(20)) # Takes 21,891 recursive calls to finish
    print(fib2(50)) # It never stops on practical time