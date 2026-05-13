import csv

csv_file = r"D:\桌面\cloud compute\mini-project2\Comp3006J MiniProject 2 Dataset.csv"

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    for row in reader:
        device_id = row[1]  # 第2列
        print(f"{device_id}\t1")