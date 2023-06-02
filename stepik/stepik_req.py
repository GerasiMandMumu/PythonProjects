import requests

with open('dataset_3378_2.txt','r') as inf:
    file = inf.readline().strip()
r = requests.get(file).text


a = r.splitlines()
print(len(a))
