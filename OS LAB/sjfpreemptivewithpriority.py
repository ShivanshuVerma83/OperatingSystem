n = int(input('Enter no of processes: '))
bt = [0] * (n + 1)
at = [0] * (n + 1)
abt = [0] * (n + 1)
priority = [0] * (n + 1)
for i in range(n):
    abt[i] = int(input('Enter the burst time for process {}: '.format(i + 1)))
    at[i] = int(input('Enter the arrival time for process {}: '.format(i + 1)))
    priority[i] = int(input('Enter the priority for process {}: '.format(i + 1)))
    bt[i] = [abt[i], at[i], i, priority[i]]

bt.pop(-1)

sumbursttime = 0
i = 0
ll = []
print(bt)
print("aaaaaa")
for i in range(1, sum(abt) + 1):
    l = [j for j in bt if j[1] <= i and j[0] > 0]
    l.sort(key=lambda x: (x[3], x[0]))  # Sort by priority and burst time
    bt[bt.index(l[0])][0] -= 1
    for k in bt:
        if k[0] == 0:
            t = bt.pop(bt.index(k))
            ll.append([k, i + 1])
ct = [0] * (n + 1)
tat = [0] * (n + 1)
wt = [0] * (n + 1)
for i in ll:
    ct[i[0][2]] = i[1]

for i in range(len(ct)):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - abt[i]
ct.pop(-1)
wt.pop(-1)
tat.pop(-1)
abt.pop(-1)
at.pop(-1)
print('BT\tAT\tCT\tTAT\tWT\tPriority')
for i in range(len(ct)):
    print("{}\t{}\t{}\t{}\t{}\t{}\n".format(abt[i], at[i], ct[i], tat[i], wt[i], priority[i]))
print('Average Waiting Time = ', sum(wt) / len(wt))
print('Average Turnaround Time = ', sum(tat) / len(tat))
