a=int(input())
b=int(input())
c=input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/' and b!=0:
    print(a/b)
elif c=='*':
    print(a*b)
elif b==0 and c=='/':
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')