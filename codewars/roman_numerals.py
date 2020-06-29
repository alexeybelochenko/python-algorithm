def solution(roman):
    i = 0
    pattern = {'I':1,'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}
    for b in roman:
        i += int(pattern.get(b))
    return i




result = solution('IV')
print(result)