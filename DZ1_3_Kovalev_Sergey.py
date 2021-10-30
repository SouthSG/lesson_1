numb = [11, 12, 13, 14]
for n in range(1, 101):
    if n in numb:
        print(n, 'процентов')
    elif n % 10 == 1:
        print(n, 'процент')
    elif n % 10 > 1 and n % 10 < 5:
        print(n, 'процента')
    else:
        print(n, 'процентов')


