# str = "abcdefg"
#
# for i in range(len(str)):
#     print(str[i])
# for x in str:
#     print(x, end=' ')
#
# for i in range(0, len(str), 2):
#     print(str[i])
#

def solution(arr):
    left = 0
    right = len(arr)-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 5, 3, 10, 8]
print(solution(arr))