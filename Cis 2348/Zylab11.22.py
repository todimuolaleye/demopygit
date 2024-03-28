list_var = input().split()
count = {}
for word in list_var:
    count[word] = list_var.count(word)
    print(word, count[word])