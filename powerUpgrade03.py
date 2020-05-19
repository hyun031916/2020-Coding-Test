def solution(num):
   # 코드 작성부분
   answer = str(num+1)  #"9950000"
   for i in range(len(answer)-1):
        answer = answer.replace("0", "1")
   return answer


#The following is code to output testcase.
num = 9949999
ret = solution(num)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
