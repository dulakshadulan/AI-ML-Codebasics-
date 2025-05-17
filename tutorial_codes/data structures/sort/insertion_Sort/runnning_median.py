def get_index(arr,val):
    index = 0
    for i in arr:
        if i > val :
            return index
        index += 1
    return index
     
def get_median(arr):
            i = len(arr)
            if i ==1:
                return arr[0]
            if i % 2 == 0:
                return (arr[int(i//2)]+arr[int(i//2 -1)])/2
                
            else:
                return arr[int(i//2)]

def insert(arr, val):
    index = get_index(arr,val) 
    return arr[0:index] + [val] + arr[index :]

if __name__ == '__main__':
    arr = [2,45,82,9,372,482,40]
    s = []
    for i in arr:
        s = insert(s,i)
        print(get_median(s))

    print(s)