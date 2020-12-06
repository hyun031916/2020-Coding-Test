#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(time_table, n):
    #여기에 코드를 작성해주세요.
    answer = 0
    arr = [0 for _ in range(n)]
    for i, j in enumerate(time_table):
        arr[i % n] += j
    answer = max(arr)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
time_table3 = [3, 7, 4, 10, 8]
n3 = 5
ret3 = solution(time_table3, n3)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")
