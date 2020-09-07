#1
# def letter(license_plate, start, end):
#     result = ""
#     for i in range(start, end+1):
#         result += license_plate[i]
#     return result
#
#
# license_plate = "24가 2210"
# print(license_plate[4:])
# a = letter(license_plate, len(license_plate)-4, len(license_plate))

# #2
# letters = 'python'
#
# print(letters[0]+' '+letters[2])

# #3
# phone_number = "010-1111-2222"
#
# a = phone_number.replace("-", " ")
# print(a)

# #4
# url = "http://sharebook.kr"
# str = url.split(".")
# print(str[-1])
#print(url.split(".")[-1])

# #5.변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# t1 = 'python'
# t2 = 'java'
#
# print((t1+' '+t2+' ')*3)
#
#
# #6.삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
# print(int(상장주식수. replace(",", '')))
#
# #7.다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"
# print(ticker.split("_"))
#
# #8.movie_rank = ["닥터 스트레인지", "스플릿", "럭키"] 리스트에 "배트맨"을 추가하라.
#
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)
#
# #9. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# # "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# def insert_list(index, value, 리스트):
#     # result = 리스트[:index]
#     # for i in range(index, len(리스트)):
#     #     result.append(리스트[i])
#     # return result
#     return 리스트[:index] + value.split(" ")+ 리스트[index:]
#
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '베트맨']
# print(insert_list(1, "슈퍼맨", movie_rank))
# print(movie_rank)

# #10. movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '럭키', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
# print(movie_rank)
#
# #11. 다음 리스트의 합 출력하라
# nums = [1, 2, 3, 4, 5]
#
# print(sum(nums))

#12. 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.

# def 중복제거_갯수(리스트):
#     result = dict()
#     for x in 리스트:
#         result[x] = 1
#     return len(result)
#
#
#
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두",
#         "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))
# print(중복제거_갯수(cook))

# #13. 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# print(sum(nums)/len(nums))
#
# #14. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# nums.reverse()
# print(nums)
# print(nums[::-1])

#15. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#출력 예시 : 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
# print(interest[0]+"/"+interest[1]+'/'+interest[2]+'/'+interest[3]+'/'
#       +interest[4])
# a = "/".join(interest)
# str = ''
# for inter in interest:
#     str += inter+" "
# print(str.replace(" ", "/"))

# #16. 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# # 이를 interest 이름의 리스트로 분리 저장하라.
# interest = string.split('/')
# print(interest)

#17. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
a = sorted(data)
print(a)
print(data)
#
# #18.사용자로부터 입력 받은 시간이 정각인지 판별하라.
# user = "현재시간:02:20"
# if(user[-2:]=='00'):
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")
#

# #19. 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for list in 리스트:
#     if(list[-2:]==".h"):
#         print(list)
#     else:
#         pass

#20. for문을 사용해서 아래와 같이 출력하라.
# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9
for x in range(0, 10, 1):
    print(x/10)
# for i in range(10):
#     print("0.",i)
    
#21. 리스트에 저장된 데이터를 아래와 같이 출력하라.
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(j,"호")

#22. 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여
# 리스트로 반환하는 pickup_even 함수를 구현하라.
def pickup_even(list1):
    result = list()
    for i in list1:
        if i%2==0:
            result.append(i)
    print(result)

pickup_even([3, 4, 5, 6, 7, 8])



        



