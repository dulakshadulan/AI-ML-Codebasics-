def bubble_sort(elements):
    size = len(elements)

    for i in range(len(elements)-1):
        swapped = False

        for j in range (size-1 -i ):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break
    return elements

def bubble_sort_on_key(elements, key):

    size = len(elements)

    for i in range(len(elements)-1):
        swapped = False

        for j in range (size-1 -i ):
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break
    return elements     


if __name__=="__main__":
    elements = [5,9,2,1,67,34,88,34]

    elements_2 = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print(f'raw {elements}')
    

    bubble_sort(elements)

    bubble_sort_on_key(elements_2, key='name')

    print(elements_2)