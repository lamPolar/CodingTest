
T = int(sys.stdin.readline())
for i in range(T):
	N, Q = map(int, sys.stdin.readline().split())
	I = list(map(int, sys.stdin.readline().split()))
	print(checkImportance(N, Q, I))

def checkImportance(N,Q,I):
    index = [i for i in range(n)]
    index[m] = 'target'    # 내가 찾고 싶은 index
    cnt = 0
 
    while I:
        if I[0] == max(I):    # 나머지 문서들보다 중요도가 더 높은 문서가 없다면
            cnt += 1
            if index[0] == 'target':
                print(cnt)
                break
            I.pop(0)
            index.pop(0)
        else:
            I.append(I.pop(0))
            index.append(index.pop(0))
