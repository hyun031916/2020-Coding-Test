def solution(password):
    answer = False
    upperCnt = 0
    lowerCnt = 0
    disitCnt = 0
    for p in password:
        if(p.isupper()):
            upperCnt = upperCnt +1
        if(p.islower()):
            lowerCnt = lowerCnt +1
        if (p.isdigit()):
            disitCnt = lowerCnt + 1
    if upperCnt >= 1 and lowerCnt >= 2 and disitCnt >= 2:
        answer = True
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
password1 = "helloworld"
ret1 = solution(password1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "Hello123"
ret2 = solution(password2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")