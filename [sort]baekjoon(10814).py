N = int(input())
info = []
for _ in range(N):
    info.append(input().split())
info.sort(key=lambda x:int(x[0]))

for i in info:
    print(i[0],i[1])
