def fab(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fab(n-1, memo) + fab(n-2, memo)
    return memo[n]
    

if __name__ == '__main__':
    print(fab(6))
    print(fab(7))
    print(fab(50))