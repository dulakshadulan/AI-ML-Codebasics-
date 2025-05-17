def swap(a,b,arr):
    if a!= b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements , p_index, pivot_idx):
    pivot = elements[pivot_idx]

    i = p_index

    for j in range(p_index,pivot_idx):
        if elements[j] <= pivot:
            swap (i,j,elements)

            i += 1
    swap (i,pivot_idx,elements)
    return i 

def quick_sort(elements, p_index, pivot_idx):
    if p_index>= pivot_idx :
        return
    p = partition(elements,p_index, pivot_idx)

    quick_sort(elements, p_index, p-1)
    quick_sort(elements, p+1 , pivot_idx)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]

    tests = [
        [11,2,23,56,1,33,12],
        [],
        [3],
        [1,2,3,4],
        [8,7,6,5,4,3]
    ]

    for element in tests:
        quick_sort(element,0,len(element)-1)
        print(element)