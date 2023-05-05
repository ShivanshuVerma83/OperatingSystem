n = int(input("Enter the number of processes:"))
arrival = [0 for i in range(n)]
burst = list(map(int, input("Enter burst time:").split()))
priority = list(map(int, input("Enter priority:").split()))

rec = []
for i in range(n):
    rec.append([priority[i], arrival[i], i, burst[i]])
rec.sort()

turnaround = [0 for i in range(n)]
waiting = [0 for i in range(n)]
completion = [0 for i in range(n)]
c = rec[0][1]

for i in range(n):
    temp = []
    h = []
    f = 1
    for j in rec:
        if j[1] <= c and f:
            temp = j
            f = 0
        else:
            h.append(j)
    c += temp[-1]
    completion[temp[-2]] = c
    turnaround[temp[-2]] = (c - temp[1])
    waiting[temp[-2]] = (turnaround[temp[-2]] - temp[-1])
    rec = h
    rec.sort()
print("completion time:", *completion)
print("turaround time:", *turnaround)
print("Waiting time:", *waiting)
print("Average time:", sum(waiting) / n)
