T = int(input())
def fibonacciCount0and1(N):
    answer = None
    N_2 = [1, 0]
    N_1 = [0, 1]
    N_0 = [1, 1]
    if N == 0:
        return (1, 0)
    elif N == 1:
        return (0, 1)
    elif N == 2:
        return (1, 1)

    while(N>=3):
        N_temp = N_0
        N_0 = [a+b for a, b in zip(N_0, N_1)]
        N_1 = N_temp
        N -= 1

    answer = N_0
    return answer
answer_list = []
for i in range(T):
    N = int(input())
    answer_list.append(fibonacciCount0and1(N))

for j in answer_list:
    print("%s %s" %(j[0],j[1]))

def fibonacci(N):
    answer = None
    N_2 = 0
    N_1 = 1
    N_0 = 1
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 1

    while(N>=3):
        N_temp = N_0
        N_0 = N_0 + N_1
        N_1 = N_temp
        N -= 1

    answer = N_0
    return answer
answer_list = []
