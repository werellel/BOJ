T = int(input())
N = []
step = []
for i in range(T):
	N.append(int(input()))
	step.append(0)
	
step[0] = N[0]
step[1] = N[0] + N[1]

for i in range(2, len(N)):
	step[i] = max(N[i] + step[i-2], N[i] + step[i-3] + N[i-1])

print(step[-1])