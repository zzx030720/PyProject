def deflength(str):
    length = 0
    for i in str:
        length += 1
    return length

str = input("请输入字符串：")
print(f"字符串长度为{deflength(str)}")