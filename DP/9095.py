T = int(input())
N = []
for i in range(T):
	N.append(int(input()))


for i in N:
	N_list = [1, 2, 4]	
	start = 3
	if i > 3:
		while(i != len(N_list)):
			N_list.append(N_list[start-1]+N_list[start-2]+N_list[start-3])
			start += 1

		print(N_list[-1])
	else:
		print(N_list[i-1])