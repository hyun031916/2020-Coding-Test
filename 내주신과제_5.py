#연속으로 중복되는 문자에 대한 문제


def Continuous_duplication(str):
    result = ""
    result += str[0]
    for i in range(1,len(str)):
        if(str[i-1]!=str[i]):
            result += str[i]
    return result
print(Continuous_duplication("Yeeeeah Thx! I mis_s yoooou! kkkk"))

n = int(input())
pibonacci = [0, 1]
while pibonacci[-1] <= n:
    pibonacci.append(pibonacci[-1] + pibonacci[-2])
del pibonacci[-1]
print(pibonacci)


#피보나치 수열
def fib(n):
   a,b=0,1
   while a<n:
    print(a)
    a,b = b, a+b

fib(5)
def Opposit(a):
    b = a[::-1]
    print(b)
    print("덧셈", a, "+", b, "=", int(a)+int(b))
    if(a>b):
        print("뺄셈", a, "-", b, "=", int(a)-int(b))
    elif(b>a):
        print("뺄셈", a, "-", b, "=", int(b) - int(a))


a = (input("정수 입력 : "))
Opposit(a)

# def reverse(text):
#
#     lst = []
#     count = 1
#
#     for i in range(0,len(text)):
#
#         lst.append(text[len(text)-count])
#         count += 1
#
#     lst = ''.join(lst) # join the letters together without a space
#     return lst

# print(reverse(12345))
#
def decimal(num):
    for n in range(2, num+1):
        if(num%n==0 and num!=n):
            return (str(num)+"은 소수가 아닙니다.")
        if(num==n):
            return (str(num)+'은 소수입니다.')

number = (int)(input("숫자를 입력하세요 : "))
print(decimal(number))


# 소수(素數, prime number)는 1보다 크며, 1과 자기 자신으로밖에 나누어떨어지지 않는 정수이다 소수를 구하는 코드를 작성하시오.
#
# 피보나치 수열
#
# 섭씨 / 화씨 서로 변환 (덧셈, 곱셈)
#
# 입력한 숫자와 그 숫자를 뒤집은 숫자의 덧셈/뺄셈 코드를 작성하시오.
# ex) 13
# 뎃셈에 대한 출력 : 13+31 = 44
# 뺄셈에 대한 출력 : 31-13 = 18 (무조건 큰 수에서 작은수가 빼지도록)
#
# 연속으로 중복되는 문자에 대한 문제
# aaaab -> ab
# aaaab -> a4b1
# aaaab -> 연속으로 중복되는 문자가 있으므로 true
# ab -> 연속으로 중복되는 문자가 없으므로 false
