import sys

pixels = []
for _ in range(15):
    pixels.extend(sys.stdin.readline().split())

if 'w' in pixels:
    print("chunbae")
elif 'b' in pixels:
    print("nabi")
elif 'g' in pixels:
    print("yeongcheol")
