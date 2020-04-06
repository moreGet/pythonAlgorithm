# ** QuickSort 퀵정렬 **
# 특정한 값을 기준으로 큰 숫자와 작은 숫자를 나누면 어떨까?
# 특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 뒤에 배열을 반으로 나눕니다.
# 특정 값 기준으로 왼쪽에서 오른쪽으로 가면서 특정 값 보다 큰 값을 찾고
# 반대쪽 은 특정 값 보다 작은 값을 찾는다.
# 그리고 특정값 보다 큰 값과 작은 값을 바꾸어 준다.
# 시간복잡도 NlogN 으로 굉장히 빠르다.

def quickSort(list, start, end):
    pivot = start
    temp = 0
    i = start + 1
    j = end

    ## 원소가 한개인 경우
    if start >= end:
        return

    ## 엇갈릴 때 까지 반복
    while i <= j:
        ## 피벗 값 보다 큰 값
        while (list[i] <= list[pivot]) and i < end:
            i += 1
        ## 피벗 값 보다 작은 값
        while (list[j] >= list[pivot]) and j > start:
            j -= 1
        ## 엇갈린 상태면 키 값과 교체
        if i > j:
            temp = list[j]
            list[j] = list[pivot]
            list[pivot] = temp
        ## 피벗값 보다 큰값 과 작은 값이 존재 할때
        else:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

    quickSort(list, start, j-1)
    quickSort(list, j+1, end)
    return list
            
    
arrayList = [1, 9, 7, 8, 6, 5, 2, 4, 3, 0]

arrayList = quickSort(arrayList, 0, len(arrayList)-1)
print(arrayList)