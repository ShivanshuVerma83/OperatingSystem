

n = int(input("Enter the number of Processes: "))
m = int(input("Enter the number of Resources: "))

allocation = []
for i in range(n):
    allocation.append(list(map(int, input('\nEnter the number of instances allocated for Process P' + str(i) + " : ").strip().split())))

maX = []
for i in range(n):
    maX.append(list(map(int, input("\nEnter Max matrix entry for Process P" + str(i) + " : ").strip().split())))

available = list(map(int, input("\nEnter the number of instances available of Resources : ").strip().split()))

need = [[ 0 for i in range(m)]for i in range(n)]

for i in range(n):
    for j in range(m):
        need[i][j] = maX[i][j] - allocation[i][j]

ans=[0]*n
visited=[False]*n
ind=0
def check(i):
    for j in range(m):
        if need[i][j] > available[j]:
            return False
    return True
while ind<n:
    safe=False
    for i in range(n):
        if(visited[i]==False and check(i)):
            ans[ind]="P"+str(i)
            ind+=1
            visited[i]=True
            safe=True
            for j in range(m):
                available[j]+=allocation[i][j]
    if not safe:
        break
if(ind<n):
    print("UNSAFE")
else:
    print()
    print("The System is Safe!")
    print("Safe Sequence is", ans)
    print("Available resource is", available)

