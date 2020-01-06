n = int(input())

answer = 0
n_1 = 1
n_2 = 2

for i in range(1, n+1):
	if i == 1:
		answer += 1
	elif i == 2:
		answer += 1
	else:
		answer = n_1 + n_2
		n_1 = n_2
		n_2 = answer

print(answer % 10007)