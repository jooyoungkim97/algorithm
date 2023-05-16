T = int(input()) # 입력 데이터 수
vpss = [input() for _ in range(T)]
for vps in vpss:
    stack = []
    flag = False
    for ch in vps:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                flag = True
                print("NO")
                break
            else:
                stack.pop()
    if not flag:
        if stack:
            print("NO")
        else:
            print("YES")
