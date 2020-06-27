def dup(string):
    string = string.lower()
    d = []
    for i in range(len(string)):
        #print(string[i])
        if string.index(string[i]) != i:
            #print(string.index(string[i]))
            if string[i] not in d:
                d.append(string[i])

    if len(d) == 0:
        return 0
    else:
        return string.count(d[0])


result = dup('aA11')
print(result)
#result = dup('indivisibility')
#print(result)