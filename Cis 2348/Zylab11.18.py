numbers = list(map(int, input().split()))

non_negative_numbers = sorted(num for num in numbers if num >= 0)

for num in non_negative_numbers:
    print(num, end=' ')