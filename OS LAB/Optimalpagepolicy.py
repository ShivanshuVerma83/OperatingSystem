

def f(pages,memory_size):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < memory_size:
                memory.append(page)
            else:
                # Find the page that will not be used for the longest time in the future
                farthest_page = \
                max([(p, pages[index + 1:].index(p) if p in pages[index + 1:] else float('inf')) for index, p in
                     enumerate(memory)], key=lambda x: x[1])[0]
                memory[memory.index(farthest_page)] = page
            page_faults += 1

    return page_faults

pages = list(map(int, input('Enter the sequence of Pages: ').strip().split()))
capacity = int(input('Enter maximum number of pages in a frame: '))

print("\nThe number of Page Faults occurred in FIFO are: ", f(pages, capacity))
