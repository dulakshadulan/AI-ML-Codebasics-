def merge_two_sorted(a,b , arr , key ,descending):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i][key] > b[j][key] if descending else  a[i][key] < b[j][key] :
            arr[k]  = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
          
    while i < len_a:
        arr[k] = a[i] 
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k+= 1
    
    return sorted_list

def merge_sort(arr ,key,descending= False ):
    if len(arr) <= 1:
        return 
    
    mid = len(arr)//2
    left = arr [:mid]
    right = arr[mid:]

    merge_sort(left,key,descending)
    merge_sort(right,key,descending)

    merge_two_sorted(left,right,arr, key, descending )


if __name__ == '__main__':

    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    merge_sort(elements, key='name')
    print(elements)