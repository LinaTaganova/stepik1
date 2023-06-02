a = int(input())
for a in range(a, 25, 2):
    if (a//2)%2==1:
        b = 'мокрый'
    else:
        b = 'сухой'
    print(a, b)