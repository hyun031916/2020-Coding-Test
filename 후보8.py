def solution(sentence):
	result= []
    for sen in sentence:
        temp=""
        for s in sen:
            if s in "?,.!":
                temp+=s
        if temp=="":
            result.append("특정한 문자가 없다.")
        else:
            result.append(temp)
    return result

sentence = []
n = int(input())
for i in range(n):
	sentence.append(input())
result = solution(sentence)
for r in result:
	print(r)
