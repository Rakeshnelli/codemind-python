def rotate_list(lst, positions):
    n = len(lst)
    positions = positions % n
    rotated_lst = lst[-positions:] + lst[:-positions]
    return rotated_lst
n = int(input())  
lst = list(map(int, input().split()))  
positions = int(input()) 
rotated_lst = rotate_list(lst, positions)
print(*rotated_lst)
