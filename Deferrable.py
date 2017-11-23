#Taking input paramenters of a polling server
from decimal import Decimal, getcontext

getcontext().prec  = 3

n = (int)(input())
tasks = []
queue = []
l1 = [] 

for i  in range(0, n):
	a = input()
	b = a.split(',')
	c = b[0].split('(')
	task = c[0]
	tasks.append(task)
	per = (float)(c[1])
	exe = (float)(b[1][:-1].strip())
	queue.append({})
	queue[i][task] = []
	l1.append([])
	l1[i].append({})
	l1[i][0][task] = []
	for j in range(0,20):
		l1[i][0][task].append([per*j, exe])

#l1[0].pop(0)
m = (int)(input())
A = []


for i in range(0,m):
	a = input()
	b = a.split(',')
	c = b[0].split('(')
	per = (float)(c[1])
	exe = (float)(b[1][:-1].strip())
	A.append([per, exe])


T = 100 #max time of scheduling

#print(l1[0][0][tasks[0]][0][1])
time = []
for i in range(0, 400):
	time.append((float)(i/10))

A_queue = []
perodic_task = {};
for t in time:
	if(A):
		if(t >= A[0][0]):
			A_queue.append(A[0][1])
			A.pop(0)

	for i in range(0,n):
		if(l1[i][0][tasks[i]][0][0] == t):
			period = l1[i][0][tasks[i]][0][0]
			exec_time = l1[i][0][tasks[i]][0][1]
			if(tasks[i] == 'P'):
				queue[i]['P'] = [exec_time]
				l1[i][0][tasks[i]].pop(0)
			else:	
				queue[i][tasks[i]].append(exec_time)
				l1[i][0][tasks[i]].pop(0)
	
	a = 0
#	print(queue)
	for i in range(0,n):
		if(queue[i][tasks[i]] and tasks[i] == 'P'):
			if(A_queue):
				a = i
				break
		if(queue[i][tasks[i]] and tasks[i] != 'P'):
			a = i
			break


	if(queue[a][tasks[a]]):
		queue[a][tasks[a]][0] = float(Decimal(queue[a][tasks[a]][0]) - Decimal(0.1))
		if(tasks[a] == 'P'):
			if(A_queue):
				A_queue[0] =  float(Decimal(A_queue[0]) - Decimal(0.1))
				print("Aperiodic at ",t)
		else:
#			print(tasks[a]," at ",t)
			perodic_task[tasks[a]] = float(Decimal(t) + Decimal(0.1))

		if(queue[a][tasks[a]][0] == 0):
			queue[a][tasks[a]].pop(0)
			print("Periodic Tasks",perodic_task)
		if(A_queue):
			if(A_queue[0] == 0):
				A_queue.pop(0)



'''
Input

6
P(2.5, 0.5)
T1(5.6, 0.7)
T2(9.3, 1.3)
T3(6.3, 1.1)
T4(5.3, 0.8)
T5(6.3, 1.2)
3
A(0.3, 1.1)
A(2.5, 2.0)
A(0.0, 4.7)




Output

Aperiodic at  0.3
Aperiodic at  0.4
Aperiodic at  0.5
Aperiodic at  0.6
Aperiodic at  0.7
Periodic Tasks {'T1': 0.3}
Periodic Tasks {'T1': 1.2}
Periodic Tasks {'T1': 1.2, 'T2': 2.5}
Aperiodic at  2.5
Aperiodic at  2.6
Aperiodic at  2.7
Aperiodic at  2.8
Aperiodic at  2.9
Periodic Tasks {'T1': 1.2, 'T2': 2.5}
Periodic Tasks {'T3': 4.1, 'T1': 1.2, 'T2': 2.5}
Periodic Tasks {'T3': 4.1, 'T1': 1.2, 'T2': 2.5, 'T4': 4.9}
Aperiodic at  5.0
Aperiodic at  5.1
Aperiodic at  5.2
Aperiodic at  5.3
Aperiodic at  5.4
Periodic Tasks {'T5': 5.0, 'T3': 4.1, 'T1': 1.2, 'T2': 2.5, 'T4': 4.9}
Periodic Tasks {'T5': 5.0, 'T3': 4.1, 'T1': 6.3, 'T2': 2.5, 'T4': 5.6}
Periodic Tasks {'T5': 5.0, 'T3': 7.4, 'T1': 6.3, 'T2': 2.5, 'T4': 5.6}
Aperiodic at  7.5
Aperiodic at  7.6
Aperiodic at  7.7
Aperiodic at  7.8
Aperiodic at  7.9
Periodic Tasks {'T5': 5.0, 'T3': 7.4, 'T1': 6.3, 'T2': 2.5, 'T4': 7.5}
Periodic Tasks {'T5': 5.0, 'T3': 7.4, 'T1': 6.3, 'T2': 2.5, 'T4': 8.6}
Aperiodic at  10.0
Aperiodic at  10.1
Aperiodic at  10.2
Aperiodic at  10.3
Aperiodic at  10.4
Periodic Tasks {'T5': 9.3, 'T3': 7.4, 'T1': 6.3, 'T2': 10.0, 'T4': 8.6}
Periodic Tasks {'T5': 9.3, 'T3': 7.4, 'T1': 6.3, 'T2': 11.1, 'T4': 8.6}
Periodic Tasks {'T5': 9.3, 'T3': 7.4, 'T1': 11.9, 'T2': 11.1, 'T4': 11.2}
Aperiodic at  12.5
Aperiodic at  12.6
Aperiodic at  12.7
Aperiodic at  12.8
Aperiodic at  12.9
Periodic Tasks {'T5': 9.3, 'T3': 7.4, 'T1': 11.9, 'T2': 11.1, 'T4': 12.5}
Periodic Tasks {'T5': 9.3, 'T3': 14.1, 'T1': 11.9, 'T2': 11.1, 'T4': 12.5}
Periodic Tasks {'T5': 9.3, 'T3': 14.1, 'T1': 11.9, 'T2': 11.1, 'T4': 14.2}
Periodic Tasks {'T5': 14.6, 'T3': 14.1, 'T1': 11.9, 'T2': 11.1, 'T4': 14.2}
Aperiodic at  15.0
Aperiodic at  15.1
Aperiodic at  15.2
Aperiodic at  15.3
Aperiodic at  15.4
Periodic Tasks {'T5': 15.0, 'T3': 14.1, 'T1': 11.9, 'T2': 11.1, 'T4': 14.2}
Periodic Tasks {'T5': 16.3, 'T3': 14.1, 'T1': 11.9, 'T2': 11.1, 'T4': 14.2}
Periodic Tasks {'T5': 17.5, 'T3': 14.1, 'T1': 11.9, 'T2': 11.1, 'T4': 14.2}
Aperiodic at  17.5
Aperiodic at  17.6
Aperiodic at  17.7
Aperiodic at  17.8
Aperiodic at  17.9
Periodic Tasks {'T5': 17.5, 'T3': 14.1, 'T1': 11.9, 'T2': 11.1, 'T4': 14.2}
Periodic Tasks {'T5': 17.5, 'T3': 14.1, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  20.0
Aperiodic at  20.1
Aperiodic at  20.2
Aperiodic at  20.3
Aperiodic at  20.4
Periodic Tasks {'T5': 17.5, 'T3': 20.0, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Periodic Tasks {'T5': 17.5, 'T3': 21.5, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  22.5
Aperiodic at  22.6
Aperiodic at  22.7
Aperiodic at  22.8
Aperiodic at  22.9
Periodic Tasks {'T5': 22.5, 'T3': 21.5, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Periodic Tasks {'T5': 23.2, 'T3': 21.5, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  25.0
Aperiodic at  25.1
Aperiodic at  25.2
Aperiodic at  25.3
Aperiodic at  25.4
Periodic Tasks {'T5': 23.2, 'T3': 21.5, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Periodic Tasks {'T5': 23.2, 'T3': 26.6, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  27.5
Aperiodic at  27.6
Aperiodic at  27.7
Aperiodic at  27.8
Aperiodic at  27.9
Periodic Tasks {'T5': 27.5, 'T3': 26.6, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Periodic Tasks {'T5': 28.3, 'T3': 26.6, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  30.0
Aperiodic at  30.1
Aperiodic at  30.2
Aperiodic at  30.3
Aperiodic at  30.4
Periodic Tasks {'T5': 28.3, 'T3': 26.6, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  32.5
Aperiodic at  32.6
Aperiodic at  32.7
Aperiodic at  32.8
Aperiodic at  32.9
Periodic Tasks {'T5': 28.3, 'T3': 32.5, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Periodic Tasks {'T5': 28.3, 'T3': 33.1, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Periodic Tasks {'T5': 34.3, 'T3': 33.1, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  35.0
Aperiodic at  35.1
Aperiodic at  35.2
Aperiodic at  35.3
Aperiodic at  35.4
Periodic Tasks {'T5': 34.3, 'T3': 33.1, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}
Aperiodic at  37.5
Aperiodic at  37.6
Aperiodic at  37.7
Periodic Tasks {'T5': 34.3, 'T3': 38.9, 'T1': 11.9, 'T2': 19.9, 'T4': 14.2}


'''
