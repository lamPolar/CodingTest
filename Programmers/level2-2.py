#오픈채팅방
def solution(record):
    answer = []
    user = {} #dictionary로 id와 nickname을 연동
    #최종 닉네임 확인을 위해 record재생
    for i in record: 
        som = i.split()
        if som[1] not in user:
            user[som[1]] = som[2]
        else:
            if som[0] == 'Enter':
                user[som[1]] = som[2]
            if som[0] == 'Change':
                user[som[1]] = som[2]
    #for key in user:
    #    print(key, user[key])
    
    # 최종 닉네임을 들어오고 나간 순서대로 출력
    for i in record:
        som = i.split()
        if som[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(user[som[1]]))
        elif som[0]=='Leave':
            answer.append("{}님이 나갔습니다.".format(user[som[1]]))
    return answer
