import csv
count=0
data=[]
data.append(["index","year","title","attribute","us"])
year=input("何年:")

#0→受け、1→攻め
#タイトルで「c.」を入力すると終了する

while(1):

    print(count)
    title=input("タイトル:")
    if title=="c.":
        break
    else:
        seme=input("攻め:")
        data.append([count,year,title,seme,1])
        count+=1
        uke=input("受け:")
        data.append([count,year,title,uke,0])
        count+=1

with open("BL_data_"+year+".csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)

    for d in data:
        writer.writerow(d)
