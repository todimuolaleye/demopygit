#Oluwatodimu Olaleye
#2087951

def selection_sort_descend_trace(lst):
   for i in range(len(lst) - 1):
       max_ind = i
       for j in range(i + 1, len(lst)):
           if lst[j] > lst[max_ind]:
               max_ind = j
       lst[i], lst[max_ind] = lst[max_ind], lst[i]
       print(*lst, end=' ')
       print()
   


if __name__ == '__main__':
   numbers = [int(x) for x in input().split()]
   selection_sort_descend_trace(numbers)
 