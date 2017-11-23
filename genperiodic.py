import numpy as np
time_period = np.random.uniform(5, 10, 5)	
#print(time_period)
utilization = np.random.uniform(0.1, 0.20, 5)
#print(utilization)
Phase = [0 for i in range(0, 5)]
#print(Phase)
Exec_Time = []
Deadline = []
for i in range(0, 5):
	Exec_Time.append(time_period[i]*utilization[i])
	Deadline.append(time_period[i])

for i in range(0,5):
	print "P(",round(time_period[i],1),", ",round(Exec_Time[i],1),")"	

util = 0
sumutil = 0
for i in range(0, 5):
	util =  Exec_Time[i]/time_period[i]
	sumutil += util



e = 1.0/(float)(10)

U_algo = 10*(2**e - 1)

	
'''
OUTPUT

T1(5.6, 0.7)
T2(9.3, 1.3)
T3(6.3, 1.1)
T4(5.3, 0.8)
T5(6.3, 1.2)


'''	