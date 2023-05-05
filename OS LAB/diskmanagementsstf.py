

disks = list(map(int, input('Enter the sequence of Disk requests: ').strip().split()))
head = int(input('Enter current head position: '))
disks.sort()
k,l=[],[]
for i in range(len(disks)-1):
    if disks[i] < head:
        k.append(disks[i])
    else:
        l.append(abs(disks[i+1]-disks[i]))
k.append(head)
k.sort(reverse=True)
for i in range(len(k)-1,len(disks)):
    k.append(disks[i])
h=[]
for i in range(len(k)-1):
    h.append(abs(k[i+1]-k[i]))

#82,170,43,140,24,16,190
#(50-43)+(43-24)+(24-16)+(82-16)+(140-82)+(170-140)+(190-170)  =208 Unit

print(k)
print("Total head movement or total seek time will be", sum(h))
