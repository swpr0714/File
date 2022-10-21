box=[[1,2,3],[23,18,30]]        #[[Num],[Volume]]
item=[[1,2,3,4,5],[4,6,2,8,1]]  #[[Num],[Volume]]
type = []
num = []
box_type = input("請輸入箱子種類(1~3):")
NumofType = input("請輸入欲放入物品種類數(1~5):")
for i in range(1,int(NumofType)+1,1):
    temp_type, temp_num = map(int,input("請輸入欲放入物品種類"+str(i)+"和物品數量:").split())
    type.append(temp_type)
    num.append(temp_num)
sum_vol = 0
for i in range (1,int(NumofType)+1,1):
    sum_vol+=item[1][int(type[i-1])-1]*int(num[i-1])
print("物品總體積為",sum_vol)
if(sum_vol<=box[1][int(box_type)-1]):
    print("可以放入箱子"+box_type)
else:
    print("不可以放入箱子"+box_type)
