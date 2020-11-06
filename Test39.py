# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(height):
    # 여기에 코드를 작성해주세요.
    count = 0
    for i in range(len(height)):
         for j in range(len(height)):
            if i > 0:
               if not(height[i-1][j] > height[i][j]):
                  continue
            if j > 0:
               if not(height[i][j-1] > height[i][j]):
                  continue
            if i < (len(height)-1):
               if not(height[i+1][j]>height[i][j]):
                   continue
            if j < (len(height)-1):
                if not(height[i][j+1]>height[i][j]):
                    continue
            print(height[i][j])
            count+=1
    return count

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

height = [[4, 7, 2, 5], [5, 7, 2, 1], [6, 3, 8, 4], [2, 4, 7, 3]]
ret = solution(height)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
