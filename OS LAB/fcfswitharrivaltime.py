print("First Come first serve scheduling in operating system")
n=int(input("Enter the number of process: "))
di=dict()
for i in range(n):
    #process burst time and arrival time nikalna hai
    #sabse pehle p le lete hain
    process="P"+str(i*1)
    arrivalTime=int(input("Enter the arrival time: "))
    burstTime=int(input("Enter the burst time: "))
    l=[]
    l.append(arrivalTime)
    l.append(burstTime)
    di[process] = l
print(l)
print(di)
d=sorted(di.items(), key=lambda item: item[1][0])
#print the exit time
print(d)
exit=[]
for i in range(len(d)):
    if i==0:
        exit.append(d[i][1][1])
    else:
        exit.append(exit[i-1]+d[i][1][1])
turnaround=[]
for i in range(len(d)):
    turnaround.append(exit[i]-d[i][1][0])
waitingtime=[]
for i in range(len(d)):
    waitingtime.append(turnaround[i]-d[i][1][1])
print("Process | Arrival | Burst | Exit | Turn Around  | Wait |")
for i in range(n):
      print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",exit[i],"  |    ",turnaround[i],"   |   ",waitingtime[i],"   |  ")



