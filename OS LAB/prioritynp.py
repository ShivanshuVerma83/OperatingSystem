n = int(input("Enter no of processes:"))

burst_time = list(map(int,input("Enter burst time of each process as spaced integers : ").split()))

arrival_time = list(map(int,input("Enter arrival time as spaced integers : ").split()))

priorities = list(map(int,input("Enter priority as spaced integers : ").split()))
processes = []
for i in range(n):
    processes.append([i+1,burst_time[i],arrival_time[i]])


queue = []
for pid, burst, arrival in processes:
    queue.append([arrival, pid, burst])
for i in range(len(priorities)):
    queue[i].append(int(priorities[i]))
process = sorted(queue, key=lambda x: (x[3], x[0]))
n = len(process)
wt = [0] * n
tat = [0] * n
total_wt = 0
total_tat = 0
time = 0
time += process[0][0]
wt[0] = 0

for i in range(1, n):
    time += process[i - 1][2]
    wt[i] = time - process[i][0]
    if (wt[i] < 0):
        wt[i] = 0
        time = process[i][1]
time += process[-1][2]

for i in range(n):
    tat[i] = process[i][2] + wt[i]

for i in range(n):
    total_wt += wt[i]
    total_tat += tat[i]

avg_wt = total_wt / n
avg_tat = total_tat / n
result = [avg_wt, avg_tat]




print("process_no.  burst_time    arrival_time          priority")
for i in range(len(processes)):
    print(processes[i][0],"       \t\t",processes[i][1],"         \t\t",processes[i][2],"         \t\t",priorities[i])


# print("Waiting time of the above processes sorted according to process ids are: ")
# print(wt)
# print("Turn around time of above processes sorted in process ids are: ")
# print(tat)
print("The Average waiting time and average turn around time are below: ")
print(result)













