def swap(a,b,arr):
    if a!= b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start , end):
    pivot_index = start
    pivot = elements[pivot_index]


    while start < end :
            

        while start<len(elements) and elements[start] <= pivot:
            start += 1

        while start<len(elements) and elements[end] > pivot:
            end -= 1
        if start < end: 
            swap(start,end,elements)
    
    swap(pivot_index,end,elements)

    return end

    


def quick_sort(elements, start, end):
    if start < end:
        p1 = partition(elements, start , end)
        quick_sort(elements,start,p1 - 1)
        quick_sort(elements,p1 +1 , end)

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