# Python3 program for implementation
# of Priority scheduling

# Function to find the waiting
# time for all processes
def findWaitingTime(processes, n,bt, wt):

# waiting time for
# first process is 0
	wt[0] = 0

# calculating waiting time
	for i in range(1,n):
		wt[i] = bt[i-1]+wt[i-1]

# Function to calculate turn
# around time
def findTurnAroundTime(processes, n,bt, wt, tat):

# calculating turnaround
# time by adding bt[i] + wt[i]
	for i in range(n):
		tat[i] = bt[i] + wt[i]

# Function to calculate
# average time
def findavgTime(processes, n, bt,pt):

	wt =[0]*n
	tat= [0]*n
	total_wt = 0
	total_tat = 0

# Function to find waiting
# time of all processes
	findWaitingTime(processes, n, bt, wt)

# Function to find turn around
# time for all processes
	findTurnAroundTime(processes, n,bt, wt, tat)

# Display processes along
# with all details
	print("Processes Burst time "+" Waiting time " +" Turn around time "+" Priority")

# Calculate total waiting time
# and total turn around time
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(str(processes[i]) + "\t\t" +str(bt[i]) + "\t" +str(wt[i]) + "\t\t" +str(tat[i])+"\t\t" +str(pt[i]))

	print("Average waiting time = "+str(total_wt / n))
	print("Average turn around time ="+str(total_tat / n))

#Sorting processes burst time, on the basis of their priority
def sortShortest(processes, n, bt,pt):
	for i in range(0,n):
		for j in range(0,n-i-1):
			if(pt[j]>pt[j+1]):
				swap=pt[j]
				pt[j]=pt[j+1]
				pt[j+1]=swap
				swap=processes[j]
				processes[j]=processes[j+1]
				processes[j+1]=swap
				swap=bt[j]
				bt[j]=bt[j+1]
				bt[j+1]=swap
			
 
# Driver code
if __name__ =="__main__":

# process id’s
	processes = [ 1, 2, 3]
	n = len(processes)

# Burst time of all processes
	burst_time = [10, 5, 8]

#priority
	priority = [3,1,2]
	print("Priority")
	sortShortest(processes, n, burst_time,priority)
	findavgTime(processes, n, burst_time,priority)
