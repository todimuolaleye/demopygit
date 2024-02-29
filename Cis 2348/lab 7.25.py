Oluwatodimu Olaleye
2087951

def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100
    num_quarters = user_total // 25
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    user_total %= 5
    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars > 0:
        print(f"{num_dollars} dollar{'s' if num_dollars > 1 else ''}")
    if num_quarters > 0:
        print(f"{num_quarters} quarter{'s' if num_quarters > 1 else ''}")
    if num_dimes > 0:
        print(f"{num_dimes} dime{'s' if num_dimes > 1 else ''}")
    if num_nickels > 0:
        print(f"{num_nickels} nickel{'s' if num_nickels > 1 else ''}")
    if num_pennies > 0:
        print(f"{num_pennies} penn{'ies' if num_pennies != 1 else 'y'}")
    if input_val <= 0:
        print('no change')