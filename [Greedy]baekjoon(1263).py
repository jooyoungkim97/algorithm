N = int(input())
times = [tuple(map(int,input().split())) for _ in range(N)]

times.sort(key=lambda x:x[1], reverse=True)

ans = times[0][1] - times[0][0]
for i in range(1,N):
    if ans > times[i][1]:
        ans = times[i][1] - times[i][0]
    else:
        ans -= times[i][0]

if ans>=0:
    print(ans)
else:
    print(-1)
