

disks = list(map(int, input('Enter the sequence of Disk requests: ').strip().split()))
head = int(input('Enter current head position: '))

k=[]
k.append(abs(disks[0]-head))
for i in range(len(disks)-1):
    k.append(abs(disks[i+1]-disks[i]))
print(k)
print("Total head movement or total seek time will be", sum(k))
# 82,170,43,140,24,16,190
# (82-50)+(170-82)+(170-43)+(140-43)+(140-24)+(24-16)+(190-16) = 642 Unit