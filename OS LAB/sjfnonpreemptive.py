n = int(input("Enter number of processes:"))
arrival_time = list(map(int,input("Enter arrival time:").split()))
burst_time = list(map(int,input("Enter burst time of each process:").split()))
h = []
for i in range(n):
    h.append([arrival_time[i],burst_time[i],i+1])
h.sort()

turnaround_time = []
waiting_time = []

x = 0
for i in range(n):
    x = max(x,h[i][0]) + h[i][1]
    turnaround_time.append(x - h[i][0])
    waiting_time.append(turnaround_time[i] - h[i][1])
print("process_no.  arrival_time  burst_time waiting_time turaround_time")
print#(len(h),len(waiting_time),len(turnaround_time))
for i in range(n):
    print(h[i][2],"\t\t",h[i][0],"\t\t",h[i][1],"\t\t",waiting_time[i],"\t\t",turnaround_time[i])
