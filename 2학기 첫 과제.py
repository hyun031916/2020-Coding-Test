# #1. 문자열을 대체하는 함수를 작성하시오
# def 문자열대체(string, old, new):
#     a= str()
#     for i in string:
#         if(i!=old):
#             a+=i
#         else:
#             a+= new
#     return a
#
# phone_number = "010-1111-2222"
# a = 문자열대체(phone_number, "-", " ")
# print(a)
#
# 2. 문자열을 list 형태로 쪼개시오
def 문자열쪼개기(string, sep):
    li = list()
    li+=string[:-3]
    li+=string[4:8]
    li+=string[9:]
    return li


phone_number = "010-1111-2222"
a = 문자열쪼개기(phone_number, "-")
print(a)
#
#3. list 특정위치에 특정값을 삽입하시오
# def 아이템삽입(src, index, object):
#     result = src[:index]
#     result+=object
#     for i in range(index, len(src)):
#         result+=(src[i])
#     return result
#
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# a = 아이템삽입(movie_rank, 1, "슈퍼맨")

# print(a)
#
# #4. list 특정값을 삭제하시오
# def 특정아이템삭제(src, object):
#     count = 0
#     for j in src:
#         count += 1
#     for i in range(count):
#        if(src[i]==object):
#            return src[:i]+src[i+1:]
#
# movie_rank = ['럭키', '스플릿', '럭키', '배트맨']
# a = 특정아이템삭제(movie_rank, "럭키")
#
# print(a)

# #5. list 특정값을 삭제하시오
# def 특정아이템모두삭제(src, object):
#     a = list(); count = 0
#     for j in src:
#         count += 1
#     for i in range(count):
#         if(src[i]!=object):
#             a.append(src[i])
#     return a
#
#
# movie_rank = ['럭키', '스플릿', '럭키', '배트맨']
# a = 특정아이템모두삭제(movie_rank, "럭키")
#
# print(a)
#
# #6. list에 있는 값들의 평균을 구하시오
# def 평균(src):
#     sum = 0; count = 0
#     for i in src:
#         count +=1
#         sum += i
#     return sum/count
#
#
# 리스트 = [1, 2, 3, 4, 5]
# a = 평균(리스트)
#
# print(a)

# #7. list에 있는 문자들을 다음의 결과가 나오도록 함수를 작성하시오
# def 조인(string, iterable):
#     a = str()
#     for s in iterable:
#         a += s
#         if(s!=iterable[-1]):
#             a+= string
#     return a
#
#
# 리스트 = ["내", "pc", "지키미"]
# a = 조인("/", 리스트)
#
# print(a)
