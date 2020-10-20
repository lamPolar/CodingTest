#다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    clock = 0 
    going = [] #다리를 건너고 있는 트럭
    time = []  #다리로 진입하는 시간
    #현재 대기 1순위 트럭 : truck_weights[0]
    
    while len(truck_weights)!=0:
        clock +=1
        if len(time)>0 and clock-time[0] == bridge_length:
            going.pop(0)
            time.pop(0)
        if sum(going)+ truck_weights[0] <= weight:
            going.append(truck_weights.pop(0))
            time.append(clock)
            
#    print(going, truck_weights, time, answer)
    answer = time.pop()+ bridge_length
    return answer
