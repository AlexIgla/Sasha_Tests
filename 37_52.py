#Счастливый билет
s = input()
if int(s[0]) + int(s[1]) + int(s[2]) == int(s[-1]) + int(s[-2]) + int(s[-3]):
    print('YES')
else:
    print('NO')