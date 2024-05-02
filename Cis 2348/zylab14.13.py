#Oluwatodimu Olaleye
#2087951


num_calls = 0

def partition(user_ids, i, k):
    global num_calls
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]

    l = i
    h = k

    while True:
        while user_ids[l] < pivot:
            l += 1
        while user_ids[h] > pivot:
            h -= 1
        if l >= h:
            return h

        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
        l += 1
        h -= 1

def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i >= k:
        return

    j = partition(user_ids, i, k)
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:
        print(user_id)