#Taking input paramenters of a polling server
from decimal import Decimal, getcontext

getcontext().prec  = 3

n = (int)(input())
tasks = []
queue = []
l1 = [] 
t_ctr = []

for i  in range(0, n):
	a = input()
	b = a.split(',')
	c = b[0].split('(')
	task = c[0]
	tasks.append(task)
	t_ctr.append({task: 0})
	per = (float)(c[1])
	exe = (float)(b[1][:-1].strip())
	queue.append({})
	queue[i][task] = []
	l1.append([])
	l1[i].append({})
	l1[i][0][task] = []
	for j in range(0,10):
		l1[i][0][task].append([per*j, exe])

#l1[0].pop(0)
A = []
print(t_ctr)
T = 100 #max time of scheduling

#print(l1[0][0][tasks[0]][0][1])
time = []
for i in range(0, 200):
	time.append((float)(i/10))

#A_queue = []
perodic_task = {};

for t in time:
	for i in range(0,n):
		if(l1[i][0][tasks[i]][0][0] == t):
			period = l1[i][0][tasks[i]][0][0]
			exec_time = l1[i][0][tasks[i]][0][1]
			queue[i][tasks[i]].append(exec_time)
			l1[i][0][tasks[i]].pop(0)
	
	a = 0
	for i in range(0,n):
		if(queue[i][tasks[i]]):
			a = i
			break


	if(queue[a][tasks[a]]):
		queue[a][tasks[a]][0] = float(Decimal(queue[a][tasks[a]][0]) - Decimal(0.1))
		perodic_task[tasks[a]] = float(Decimal(t) + Decimal(0.1))

		if(queue[a][tasks[a]][0] == 0):
			queue[a][tasks[a]].pop(0)
			t_ctr[a][tasks[a]] += 1	
			print("Periodic Tasks",tasks[a],t_ctr[a][tasks[a]],perodic_task)

#print(queue)
#print("Periodic Tasks",perodic_task)

