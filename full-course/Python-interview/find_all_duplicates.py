
#  https://www.youtube.com/watch?v=8ci8WfQ6cns

arr = [1,2, 1, 3, 4 , 5, 6, 7, 7,2]

duplicates = []
for i in range(len(arr)):
    num =  abs(arr[i])
    if(arr[num] < 0):
        duplicates.append(num)
    else:
        arr[num] *= -1

print(duplicates)

