Oluwatodimu Olaleye
2087951

a, b, c, d, e, f = [int(input()) for _ in range(6)]

solution_found = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            solution_found = True
            break
    if solution_found:
        break
if not solution_found:
    print('No solution')