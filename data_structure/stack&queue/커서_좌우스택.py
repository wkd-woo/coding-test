from collections import deque

t = int(input())

for _ in range(t):
    left_stack = []
    right_stack = deque()
    l = input()
    for c in l:
        if c == '-':
            if left_stack:
                left_stack.pop()
        elif c == '<':
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif c == '>':
            if right_stack:
                left_stack.append(right_stack.popleft())
        else:
            left_stack.append(c)
    left_stack.extend(list(right_stack))
    print(''.join(left_stack))
