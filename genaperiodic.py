import numpy as np
arr_time = np.random.exponential(3, 3)	
print(arr_time)
Exec_Time = np.random.exponential(1, 3)
print(Exec_Time)


for i in range(0,3):
	print "A(",round(arr_time[i],1),",",round(Exec_Time[i],1),")"	

'''
Output

A(0.3, 1.1)
A(2.5, 2.0)
A(0.0, 4.7)



'''