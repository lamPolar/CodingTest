#크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                #print(i-1,j[i-1], basket)
                basket.append(j[i-1])
                j[i-1] = 0
                if len(basket)>=2 and basket[-1] == basket[-2]:
                    basket = basket[:-2]
                    answer += 2
                break
    return answer
