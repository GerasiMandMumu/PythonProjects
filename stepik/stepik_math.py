number = input()
d = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
a = len(number)
def prov(n, de):
    numb = 0
    for i in range(0, len(n)):
        if n[i - 1] != n[i]:
            return False
        else:
            numb += de[n[0]]
    return numb
num = 0
if prov(number, d) != False:
    print(prov(number,d))
else:
    i = 0
    while i < a and number != "":
        if len(number) != 1:
            if d[number[0]] >= d[number[1]]:
                num += d[number[0]]
                number = number[1:]
                i += 1
            else:
                num += (d[number[1]] - d[number[0]])
                number = number[2:]    
                i += 1
        else:
            num += d[number[0]]
            break
    print(num)
      

