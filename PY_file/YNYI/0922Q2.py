# 第二題
cname=input("請輸入中文姓名：")
ename=input("請輸入英文姓名：")
dep=input("請輸入科系英文縮寫：")
id=input("請輸入學號：")
tel=input("請輸入聯絡電話:")
deg=int(id[3:5])
print(cname+ "\t" +ename)
print("NCKU "+dep,deg+104)
print("Phone: +886 "+tel[1:4]+" "+tel[4:7]+" "+tel[7:10])
print("Email: "+id+"@gs.ncku.edu.tw")

