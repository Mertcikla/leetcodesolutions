fib = [None]*100
fib[0] = 0
fib[1] = 1
# print(fib)


def fibo(f: int) -> int:
    if f == 0:
        return 0
    elif f == 1:
        return 1
    elif fib[f] != None:
        return fib[f]
    elif fib[f] == None:
        fib[f] = fibo(f-1)+fibo(f-2)
        return fib[f]
    else:
        print('shouldnt happen')
        return -1


for i in range(30):
    print(fibo(i))
