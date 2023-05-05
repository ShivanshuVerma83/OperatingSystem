bt=[]
print("Enter the number of process: ")
n=int(input())

bt = list(map(int,input("Enter burst time as spaced integers : ").split()))
btt=bt.copy()
print("Enter the time quantum: ")
t=int(input())
maxi=bt[0]
wt=[0]*n
avgwt=0
tat=[0]*n
avgtat=0
temp=0
# maximum nikal lenge burst time mein se uske badd ek loop chlayenge maxi//t+1
# tak uske baad ek loop n tk if bt[i]!=0
# if bt[i]<=t
for i in range(1,n):
    if maxi<bt[i]:
        maxi=bt[i]
for j in range((maxi//t)+1):
    for i in range(n):
        if(bt[i]!=0):
            if(bt[i]<=t):
                tat[i]=temp+bt[i]
                temp=temp+bt[i]
                bt[i]=0
            else:
                bt[i]-=t
                temp+=t
            print(temp)

for i in range(n):
    wt[i]=tat[i]-btt[i]
wtt=wt.copy()
tatt=tat.copy()
print(wtt,tatt)
avgwt=float(sum(wtt))/n
avgtat=float(sum(tatt))/n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")

for i in range(0,n):
   print(str(i)+"    \t\t     "+str(btt[i])+"      \t\t     "+str(wt[i])+"     \t\t     "+str(tat[i]))
   print("\n")

print("Average Waiting time is: "+str(avgwt))
print("Average Turn Arount Time is: "+str(avgtat))
