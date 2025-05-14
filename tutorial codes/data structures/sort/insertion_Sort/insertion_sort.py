def insertion_sort(elements):
    median = 0
    for i in range(len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j +1 ] = elements[j]
            j -= 1
        elements[j +1]  =  anchor

        if i % 2 == 0:
            median = elements[int(i/2)]
        else:
            median = (elements[int(i//2)]+elements[int(i//2 +1)])/2

        print( median
)    


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)