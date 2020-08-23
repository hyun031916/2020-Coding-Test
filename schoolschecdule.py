def day_to_num(day):
    num_list = ["월", "화", "수", "목", "금"]
    num = 0;
    for i in num_list:
        if(i == day)
            return num
        num += 1

def func_a(day, period):
    array = [
        ["서버구축운영", "서버구축운영", "서버구축운영", "영어", "Java", "Java", "DS"],
        ["수학I", "영어I", "Java", "Java", "Python", "Python", "Python"],
        ["C++", "C++", "수학I", "과학", "운동과 건강", "동아리/자치", "동아리/자치"],
        ["DS", "DS", "음악", "과학", "운동과 건강", "수학I", "Java"],
        ["과학", "수학I", "C++", "C++", "국어", "국어", "영어I"]
    ]
    list = []
    a = 0; b = 0
    for i in array:
        if(a==day):
            for j in i:
                if(b==period):
                    return j
                b+=1
        a+=1

day = input("원하는 요일을 입력하세요(월-금) : ")
period = int(input("원하는 교시를 입력하세요 :  "))
day_num = day_to_num(day)
print(func_a(day_num, (period-1)))
