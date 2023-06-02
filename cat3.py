a = int(input())
for i in range(a, 24, 4):
    for j in range(0, 2):
        if j % 2 == 0:
            b = 'мокрый'
            print(i, b)
        else:
            b = 'сухой'
            print(i + 2, b)


