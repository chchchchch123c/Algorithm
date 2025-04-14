def largest_cake_piece_volume(n, h, v):
    max_height = max(h, n - h)
    max_width = max(v, n - v)
    thickness = 4
    return max_height * max_width * thickness

# Example Usage
n, h, v = map(int, input().split())
print(largest_cake_piece_volume(n, h, v))
