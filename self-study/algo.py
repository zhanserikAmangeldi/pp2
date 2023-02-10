def binary_search(list, end, x):
    start = 0
    counter = 0
    while start <= end:
        mid = int((start + end) / 2)
        counter += 1
        if list[mid] == x:
            return mid, counter
        elif list[mid] > x:
            end = mid - 1
        elif list[mid] < x:
            start = mid + 1
    return None
def recursive_binary_search(list,start, end, x):
    counter =0

    if start <= end:
        mid = int((start + end)/2)
        counter +=1
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return recursive_binary_search(list,start, mid -1, x)
        elif list[mid] < x:
            return recursive_binary_search(list,mid + 1, end, x)
    else:
        return None

def selection_sort(list, n):
    for i in range(0, n-1):
        smallest = i
        for j in range(i+1, n):
            if list[j] < list[smallest]:
                smallest = j
                list[i], list[smallest] = list[smallest], list[i]
    return list


def insertion_sort(list, n):
    for i in range(1,n):
        j = i
        while j>0 and list[j - 1] > list[j]:
            list[j],list[j-1] = list[j-1], list[j]
            j -= 1
    return list



print(insertion_sort([3,2,5,6,54,2,35,1,5,3,54,3,2,4,7,9], len([3,2,5,6,54,2,35,1,5,3,54,3,2,4,7,9])))


# S= [x for x in range(30, 100000)]
# print(recursive_binary_search(S,0, len(S) - 1, 33))


print("Alihan che tam")