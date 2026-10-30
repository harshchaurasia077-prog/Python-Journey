def recursiveadd(n):
    if n==0 or n==1:
        return n
    return n+recursiveadd(n-1)
sum=recursiveadd(5)
print(sum)