num = int(input(""))

if num <= 0:
    print("Not Ugly Number")
else:
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    if num == 1:
        print("Ugly Number")
    else:
        print("Not Ugly Number")
