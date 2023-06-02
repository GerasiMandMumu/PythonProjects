import random
cls = input()
listname = []
line = 0
if cls == '8А-1':
    with open('8А-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '8А-2':
    with open('8А-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '8Б-1':
    with open('8Б-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '8Б-2':
    with open('8Б-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '8В-1':
    with open('8В-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)

if cls == '8В-2':
    with open('8В-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)

if cls == '9А-1':
    with open('9А-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)

if cls == '9А-2':
    with open('9А-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '9Б-1':
    with open('9Б-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '9Б-1':
    with open('9Б-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '9В-1':
    with open('9В-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)

if cls == '9В-2':
    with open('9В-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)

if cls == '10А-1':
    with open('10А-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)

if cls == '10А-2':
    with open('10А-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '10Б-1':
    with open('10Б-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '10Б-2':
    with open('10Б-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '11А-1':
    with open('11А-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '11А-2':
    with open('11А-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '11Б-1':
    with open('11Б-1.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)
    
if cls == '11Б-2':
    with open('11Б-2.txt','r') as inf:
        line = inf.readline().strip().split()
    for i in line:
        listname.append(i)


k =[]

num = len(listname)

for i in range(1,num + 1):
    k.append(i)

random.shuffle(k)

if num <= 20:
    
    if len(k) % 2 == 0:

        for i in range(1, len(k) + 1, 2):
            print(listname[k[i - 1] - 1], listname[k[i] - 1])
    else:
        print(listname[k[-1] - 1])

        for i in range(1, len(k), 2):
            print(listname[k[i - 1] - 1], listname[k[i] - 1])

else:
    for i in k:
        print(listname[i - 1])
        k.remove(i)
        if len(k) <= 20:
            break
    for i in range(1, len(k) + 1, 2):
        print(listname[k[i - 1] - 1], listname[k[i] - 1])  




input('<<Enter>>')
