def weird(string):
    x = [ x.upper() if i%2==0 else x.lower() for i,x in enumerate(string)]
    return ''.join(x)



result = weird('Hello')
print(result)
result = weird('heLLo')
print(result)
result = weird('This is a test')
print(result)