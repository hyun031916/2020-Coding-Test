def change(st):
    arr = ""
    for i in st:
        if i.isdigit():
            i = "삐"
        arr += i
    return arr


c = change("152번 버스가 옵니다.")
print(c)