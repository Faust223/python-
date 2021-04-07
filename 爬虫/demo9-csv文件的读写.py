import csv

# csv文件读写
# csv文件一般可以当做excel 表格 二维列表

with open("a.csv","w",encoding="utf-8",newline="") as file:
    csvWriter = csv.writer(file)
    # 可以一次性写入一行
    # csvWriter.writerows[()]
    info = [
        ['aa', 'bb', 'cc'],
        ['dd', 'ee', 'ff']
    ]
    csvWriter.writerows(info)


