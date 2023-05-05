


def f(pages,capacity):
    cpu=list()
    pagefaults=0
    for i in pages:
        if i not in cpu:
            pagefaults+=1
            if len(cpu)<capacity:
                cpu.append(i)
            else:
                cpu.pop(0)
                cpu.append(i)
    return pagefaults


pages = list(map(int, input('Enter the sequence of Pages: ').strip().split()))
capacity = int(input('Enter maximum number of pages in a frame: '))

print("\nThe number of Page Faults occurred in FIFO are: ", f(pages, capacity))

