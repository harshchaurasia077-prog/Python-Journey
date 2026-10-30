def largestno(a,b,c):
    largest=0
    if a>b:
        if a>c:
            largest=a
        else:
            largest=c
    if b>a:
        if b>c:
            largest=b
        else:
            largest=c
    return largest
print(largestno(466,566,5989))
    