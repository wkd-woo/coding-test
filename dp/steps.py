n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())

dp[0] = s[0] # 1번째 계단을 밟을 때 max
dp[1] = s[0] + s[1] # 2번째 계단을 밟을 때 max

# 3번째 계단을 밟을 때 max ]
dp[2] = max(s[1] + s[2], s[0] + s[2]) # 2번째 + 3번째 vs 1번째 3번째

for i in range(3, n):
    # 3전 + 1전 + 지금 vs 2전 + 지금
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])  
print(dp[n - 1])   
