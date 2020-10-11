def solution(calorie):
   min_cal = 0
   answer = 0
   min_cal = calorie[0]
   for cal in calorie:
       if cal > min_cal:
           answer += cal - min_cal
       min_cal = min(min_cal, cal)
   return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

def solution(classes, m):
   answer = 0
   for students in classes:
       answer += students // m
       if students // m != 0:
           answer += 1
   return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

