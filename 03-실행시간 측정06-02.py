import time
import numpy as np

record = list()
for i in range(30):
    start = time.time() #시작 시점

    for i in range(1000000):
        200%10%3
    end = time.time()   #끝 시점
    record.append(end-start)

print("차이의 평균\t\t", np.mean(record))
print("차이의 표준편차\t", np.std(record))