#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(score):
    # 여기에 코드를 작성해주세요.
    answer = []
    answer = [0] * len(score)
    for i in range(len(score)):
        answer[i] = sum(map(lambda s: s > score[i], score))+1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
score3 = [1, 2, 3, 4, 7, 5, 6, 8, 9]
ret3 = solution(score3)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret3, " 입니다.")
