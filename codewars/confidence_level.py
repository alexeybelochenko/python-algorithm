import math

data = [25, 85, 63, 29, 75, 26]

var = float(sum(data)) / max(len(data), 1)

def dispersion(var):
    for num in float(len(data)):
        n1 = (data[num]-var)**2
        print(n1)

dispersion(var)