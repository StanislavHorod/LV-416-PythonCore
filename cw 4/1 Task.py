def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    pos=0 
    neg=0
    for i in range(len(arr)):
        if arr[i]>0:
            pos+=1
        else:
            neg+=arr[i]
    return [pos, neg]