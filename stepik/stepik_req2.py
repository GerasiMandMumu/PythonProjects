import requests

with open('dataset_3378_3.txt','r') as inf:
    file = inf.readline().strip()
r = requests.get(file).text
adr = 'https://stepic.org/media/attachments/course67/3.6.3/'

w=''
while r[0] + r[1]!='We':  
    need = adr + r
    r = requests.get(need).text

a = r.splitlines()
for i in a:
    print(i)
