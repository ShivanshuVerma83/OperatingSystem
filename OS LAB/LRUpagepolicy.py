

def f(pages,capacity):
    cpu=list()
    recent=list()
    pagefaults=0
    for i in pages:
        if i not in cpu:
            pagefaults+=1
            recent.append(i)
            if len(cpu)<capacity:
                cpu.append(i)
            else:
                cpu.append(i)
                index=cpu.index(recent[0])
                cpu.pop(index)
                recent.pop(index)
        else:
            if i in recent:
                recent.pop(recent.index(i))
                recent.append(i)
            else:
                recent.append(i)
    return pagefaults

pages = list(map(int, input('Enter the sequence of Pages: ').strip().split()))
capacity = int(input('Enter maximum number of pages in a frame: '))

print("\nThe number of Page Faults occurred in FIFO are: ", f(pages, capacity))

