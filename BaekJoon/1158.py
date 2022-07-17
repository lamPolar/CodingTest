N, K = input().split()
N = int(N)
K = int(K)
num = [str(i+1) for i in range(N)]
i = K-1
order = []
while (len(order) < N):
    if i >= len(num):
        i %= len(num)
    order.append(num.pop(i))
    i += K-1

result = ", ".join(order)
print("<" + result+ ">")