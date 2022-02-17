""" 이틀 이상 35도 이상일경우 열대야로"""

def hot_day(temp):
    if temp>=35:
        return 1
    else:
        return 0

days=[23, 32, 43,36, 43,15, 22]


transition=[[] for i in range(4)]                                    #transition diagram을 저장할 공간

transition[1].append((0,1))                                  #상태 1 공간에서 0이 나올 경우 상태 1로
transition[1].append((1,2))                                  #상태 1 공간에서 1이 나올 경우 상태 2로
transition[2].append((0,1))                                  #상태 2 공간에서 0이 나올 경우 상태 1로      
transition[2].append((1,3))                                  #상태 2 공간에서 1이 나올 경우 상태 3로
transition[3].append((0,3))                                  #상태 3 공간에서 0이 나올 경우 상태 3로
transition[3].append((0,3))                                  #상태 3 공간에서 1이 나올 경우 상태 1로

print(transition)
current_state = 1                                            # 현재 상태, 혹은 초기상태

def dfa(transition, current_state, input_list):                #dfa(상태천이 그래프, 초기상태, 입력리스트)
    for i in range(len(days)):
        yes = hot_day(input_list[i])
        current_state = transition[current_state][yes][1]
        print(current_state, end=' ')
    return current_state

result = dfa(transition, current_state,days)
print()
print(result)
    
# for i in range(len(days)):
#     yes=hot_day(days[i])
#     current_state = transition[current_state][yes][1]
#     print(current_state)
        
