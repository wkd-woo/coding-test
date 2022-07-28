n = int(input())

cnt = 1
stack = []
result = []

for i in range(1, n+1):  # data 개수만큼 반복
    data = int(input())  # data 입력받음
    while cnt <= data:  # 만약 cnt가 data보다 작거나 같으면
        stack.append(cnt)  # 스택에 push
        cnt += 1  # cnt 증가
        result.append('+')
    if stack[-1] == data:  # 스택 맨 윗값과 data 값이 같다면
        stack.pop()  # stack을 pop
        result.append('-')
    else:  # 앞의 조건에 해당하지 않는다면 stack 이 깨진 것.
        print('NO')
        exit()

print('\n'.join(result))
