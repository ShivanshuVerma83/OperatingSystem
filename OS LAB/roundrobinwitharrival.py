bt=[]
print("Enter the number of process: ")
n=int(input())
remainprocess=n
bt = list(map(int,input("Enter burst time as spaced integers : ").split()))
at = list(map(int,input("Enter arrival time as spaced integers : ").split()))
btt=bt.copy()
print("Enter the time quantum: ")
t=int(input())
maxi=bt[0]
wt=[0]*n
avgwt=0
tat=[0]*n
avgtat=0
temp=0
totalwt=0
flag=0
for i in range(1,n):
    if maxi<bt[i]:
        maxi=bt[i]
while remainprocess!=0:
    for i in range(n):
        if(bt[i]<=t and bt[i]>0):
            temp=temp+bt[i]
            bt[i]=0
            flag=1
        elif (bt[i]>0):
            bt[i]-=t
            temp+=t
        if (flag==1 and bt[i]==0):
            wt[i]=temp-at[i]-btt[i]
            tat[i] = temp + bt[i]
            totalwt+=temp-at[i]-btt[i]
            flag=0
            remainprocess-=1

        if(i==n-1):
            i=0
        elif(at[i+1]<=totalwt):
            i+=1
        else:
            i=0

wtt=wt.copy()

tatt=[]
for i in range(n):
    tatt.append(tat[i]-at[i])
avgwt=float(sum(wtt))/n
avgtat=float(sum(tatt))/n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t completion time \tTurnAround time")

for i in range(0,n):
   print(str(i)+"    \t\t     "+str(btt[i])+"      \t\t     "+str(wt[i])+"    \t\t    "+str(tat[i])+"   \t\t    "+str(tatt[i]))
   print("\n")

print("Average Waiting time is: "+str(avgwt))
print("Average Turn Arount Time is: "+str(avgtat))

