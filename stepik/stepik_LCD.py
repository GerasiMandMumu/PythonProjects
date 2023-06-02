a =   [' -- ',
       '|  |',
       '|  |',
       '    ',
       '|  |',
       '|  |',
       ' -- ']
b =   ['    ',
       '  | ',
       '  | ',
       '    ',
       '  | ',
       '  | ', 
       '    ']
c =  [' -- ',
      '   |',
      '   |',
      ' -- ',
      '|   ',
      '|   ',
      ' -- ']
d =  [' -- ',
      '   |',
      '   |',
      ' -- ',
      '   |',
      '   |',
      ' -- ']
e =  ['    ',
      '|  |',
      '|  |',
      ' -- ',
      '   |',
      '   |',
      '    ']
f =  [' -- ',
      '|   ',
      '|   ',
      ' -- ',
      '   |',
      '   |',
      ' -- '] 
g =  [' -- ',
      '|   ',
      '|   ',
      ' -- ',
      '|  |',
      '|  |',
      ' -- ']
h =   [' -- ',
       '   |',
       '   |',
       '    ',
       '   |',
       '   |',
       '    ']
i =  [' -- ',
      '|  |',
      '|  |',
      ' -- ',
      '|  |',
      '|  |',
      ' -- '] 
j =   [' -- ',
       '|  |',
       '|  |',
       ' -- ',
       '   |',
       '   |',
       ' -- ']
digits =[a,b,c,d,e,f,g,h,i,j]

while True:         
    number=input()
    try:
        int(number)
    except:
        continue
    break

ndigit=len(number)
hdigit=len(a)
i = 0

while i<hdigit:
    j = 0
    row=''
    while j<ndigit:
        row+=digits[int(number[j])][i] + ' '
        j+=1    
    i+=1 
print('x' + len(row)*'-' + 'x')










i = 0
while i<hdigit:
    j = 0
    row=''
    while j<ndigit:
        row+=digits[int(number[j])][i] + ' '
        j+=1
    print('|'+row+'|')    
    i+=1   
print('x' + len(row)*'-' + 'x') 
