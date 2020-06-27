#универсальное решение
def num(value):
    a = value 
    b = []
    while a > 0:
        b.append(a%10)
        a = a // 10

    for num in b:
        n += num**len(b)
        
    return n == value

#Тупа питон ыыыыыы
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
    

result = narcissistic(7)
print(result)

result = num(145)
print(result)
result = num(21)
print(result)
result = num(7)
print(result)
