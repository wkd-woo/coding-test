# 1번
def solution(p):
    answer, table = [], {}
    
    for i, each in enumerate(p):
        table[i] = [each] 

    for i, each in enumerate(table):
        curr = []
        for k in table:
            curr.append(table[k][-1])

        mn = min(curr[i:]) 
        j = curr.index(mn)
        if mn < table[i][-1]:
            temp = table[i][-1]
            table[i].append(table[j][-1]), table[j].append(temp) 

    for each in table:
        answer += [len(table[each]) - 1] 
    
    return answer
  
  
#2번
def solution(periods, payments, estimates):
    answer, vip = [0, 0], {}
    for i, (period, payment) in enumerate(zip(periods, payments)):
        if period >= 60 and sum(payment) >= 600000:
            vip[i] = [True]
        elif 24 <= period < 60 and sum(payment) >= 900000:
            vip[i] = [True]
        else:
            vip[i] = [False]

    for i, (period, payment, estimate) in enumerate(zip(periods, payments, estimates)):
        if period + 1 >= 60 and sum(payment[1:] + [estimate]) >= 600000:
            vip[i] += [True]
        elif 24 <= period + 1< 60 and sum(payment[1:] + [estimate]) >= 900000:
            vip[i] += [True]
        else:
            vip[i] += [False]
    
    for each in vip:
        if not vip[each][0] and vip[each][1]:
            answer[0] += 1
        elif vip[each][0] and not vip[each][1]:
            answer[1] += 1
              
    return answer
  
# 3번
def solution(n, plans, clients):
    data, services, answer = {i+1:0 for i in range(len(plans))}, {i+1:[] for i in range(len(plans))}, []

    for i, plan in enumerate(plans):
        policy = plan.split()
        data[i+1] = int(policy[0])
        for j in range(i, len(plans)):
            services[j+1] += policy[1:]
        
    for num, client in enumerate(clients):
        cond = True
        client = client.split()
        need_d, need_s = int(client[0]), client[1:]
        for i, (d, service) in enumerate(zip(data.values(), services.values())):
            if need_d <= d: # 데이터 만족하면
                for s in need_s:
                    print(i, s, service)
                    if s not in service:
                        cond = False
                        break
                if cond:
                    answer += [i+1]
                    break

        if len(answer) < num + 1:
            answer += [0]

    return answer