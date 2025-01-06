def find_room(N):
    if N == 1:
        return 1
    rooms = 1
    layer = 1
    
    while rooms < N:
        rooms += 6 * layer
        layer += 1
    return layer    
n = int(input())
print(find_room(n))