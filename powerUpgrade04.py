# import math

def solution(n):
    # Write code here.
    arr=[[0 for j in range(n)]for i in range(n)]
    answer = 0
    for i in arr:
        cnt = 0
        for j in i:
            cnt2 = 0
            if cnt%2==0 & cnt == 0:
                arr[cnt][cnt2]==cnt+cnt2+1
                print(arr[cnt][cnt2])
            else:
                arr[cnt][cnt2]==(n*2+1)-(cnt+cnt2)
            if cnt==cnt2:
                answer += arr[cnt][cnt2]
            cnt2 += 1
        cnt+=1
    return answer


# The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

n2 = 2
ret2 = solution(n2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
