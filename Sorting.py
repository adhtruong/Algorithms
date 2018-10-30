
def merge(left, right):
    merged_list = []

    # add elements
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # add remaining elements
    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list

def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        left = mergesort(left)
        right = mergesort(right)

        return merge(left, right)
    else:
        return A


def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


def selection_sort(A):
    for i in range(len(A)):
        # find index of minimum after i
        min_index = i
        for j in range(i,len(A)):
            if A[j] < A[min_index]:
                min_index = j
        # put i
        A[i], A[min_index] = A[min_index], A[i]

    return A
