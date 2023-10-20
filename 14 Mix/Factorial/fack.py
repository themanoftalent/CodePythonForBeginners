def fack(n):
    if n==1 or n==2:
        return n

    else:
        return n*fack(n-1)


print(fack(5))