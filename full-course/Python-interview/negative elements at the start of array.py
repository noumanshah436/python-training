
def rearrange(arr):
    length = len(arr)
    print(length)
    j = -1
    for i in range(length):
        print(f"i {i}" )
        if(arr[i] < 0):
            j += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            # swap(arr[j], arr[i])



arr = [ -5, 1, -1, 2, -2, 3 ]
rearrange(arr);
print(arr)