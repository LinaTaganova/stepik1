from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
similar = [i for i in 'il1Lo0O']
chars = []

print('Сколько нужно паролей?')
num = int(input())
print('Какая длина пароля?')
length = int(input())
print('Включать ли цифры 0123456789?; д = да, н = нет')
digit = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет')
upper = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет')
lower = input()
print('Включать ли символы !#$%&*+-=?@^_?; д = да, н = нет')
symbols = input()
print('Исключать ли неоднозначные символы il1Lo0O?; д = да, н = нет')
similar_symbols = input()

if digit == 'д':
    chars += digits
if upper == 'д':
    chars += uppercase_letters
if lower == 'д':
    chars += lowercase_letters
if symbols == 'д':
    chars += punctuation

if similar_symbols == 'д':
    for i in similar:
        if i in chars:
            chars.remove(i)

def generate_password():
    x = sample(chars, length)
    m = ''.join(x)
    return m

for i in range(num):
    print(generate_password())

