a, b = int(input()), int(input())
i = a
while i <= b:
    if i%3==0 or i%2==0:
        i += 1
        continue
    if i%777==0:
        break
    print(i)
    i += 1
