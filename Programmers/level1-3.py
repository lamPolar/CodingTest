#카카오 인턴(숫자패드 누르기)- not done yet
def solution(numbers, hand):
    answer = ''
    posi_L=10
    posi_R=12
    for i in numbers:
        if i == 1 or i==4 or i ==7:
            answer += "L"
            posi_L = i
        elif i ==3 or i ==6 or i==9:
            answer+= "R"
            posi_R = i
        else:
            if i == 0:
                i=11
            dis_L = abs(posi_L-i)djd
            dis_R = abs(posi_R-i)
            dL =distance(dis_L)
            dR = distance(dis_R)
            print(posi_L,dL,posi_R,dR)
            if dL <dR:
                answer += "L"
                posi_L = i
            elif dR< dL:
                answer += "R"
                posi_R = i
            else:
                if hand == 'right':
                    answer += "R"
                    posi_R = i
                else : 
                    answer +="L"
                    posi_L = i
    return answer
def distance(dis):
    if dis ==1 or dis ==3:
        return 1
    elif dis ==2 or dis ==4 or dis==6:
        return 2
    elif dis ==5 or dis==7:
        return 3
    else:
        return 4
