a = int(input())
counter = 0
for a in range(a, 25, 2):
    counter += 1
    if counter%2==0:
        b = 'сухой'
    else:
        b = 'мокрый'
    print(a, b)


