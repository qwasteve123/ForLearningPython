def swap(a, b, arr):
    # arr[a], arr[b] = arr[b], arr[a]
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index = end
    pivot = elements[end]

    i = start - 1

    for j in range(start,end-1):
        if elements[j] < pivot:
            i += 1
            swap(i,j,elements)

    i += 1
    swap(i,end,elements)
    return i

def quick_sort(elements,start,end):
    if start < end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,pi-1) # left partition
        quick_sort(elements,pi +1,end) # right partition

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]

    tests = [
        [11,9,29,7,2,15,28],
        [3,7,9,11],
        [25,22,21,10],
        [29,15,28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements,0,len(elements)-1)
        print(elements)