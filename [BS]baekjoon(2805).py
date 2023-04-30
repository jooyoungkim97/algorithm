N, M = tuple(map(int,input().split()))
heights = list(map(int,input().split()))

start, end = 0, sum(heights)

while start <= end:
    mid = (start+end)//2
    cut = 0 
    for height in heights:
        if height >= mid:
            cut += height-mid
    
    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
