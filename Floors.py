def uses_stairs(X, Y):
    if Y >= X:
        if Y - X <= 2:
            return "YES"
        else:
            return "NO"
    else:
        if X - Y <= 3:
            return "YES"
        else:
            return "NO"

X = int(input())
Y = int(input())
print(uses_stairs(X,Y))
