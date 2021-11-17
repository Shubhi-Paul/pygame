n = int(input())
prev,forw=0,0
list =[]
for i in range(0,n):
    list.append(int(input(i)))
for i in range(1,n):
    prev += list[i-1]
    forw = sum(list[i+1:])
    if prev == forw:
        print(i)
