bt=[]
print("Enter the number of process: ")
n=int(input())

bt = list(map(int,input("Enter burst time as spaced integers : ").split()))

wt=[]
avgwt=0
tat=[]
avgtat=0

wt.insert(0,0)
tat.insert(0,bt[0])

for i in range(1,len(bt)):
   wt.insert(i,wt[i-1]+bt[i-1])
   tat.insert(i,wt[i]+bt[i])
   avgwt+=wt[i]
   avgtat+=tat[i]

avgwt=float(avgwt)/n
avgtat=float(avgtat)/n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")

for i in range(0,n):
   print(str(i)+"    \t\t     "+str(bt[i])+"      \t\t     "+str(wt[i])+"     \t\t     "+str(tat[i]))
   print("\n")

print("Average Waiting time is: "+str(avgwt))
print("Average Turn Arount Time is: "+str(avgtat))