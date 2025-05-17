def swap(a,b,arr):
    arr[a],arr[b] = arr[b],arr[a]



def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(min_index,n):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            swap(i,min_index,arr)

def mul_selection_sort_dict(arr,keys):
    for key in keys[-1::-1]:
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(min_index,n):
                if arr[j][key] < arr[min_index][key]:
                    min_index = j
            if i != min_index:
                swap(i,min_index,arr)


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)
    elements = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
    mul_selection_sort_dict(elements,['First Name','Last Name'])
    print(elements,sep='\n')