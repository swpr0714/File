# 第一題
password = input("請輸入密碼(必須為10位以上)：")
st = int(input("開頭處:"))
end = int(input("結尾處:"))
length = len(password)
print(password[st-1:length-end+1])
