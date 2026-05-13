import csv

csv_file = r"D:\桌面\cloud compute\mini-project2\Comp3006J MiniProject 2 Dataset.csv"

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    for row in reader:
        sensor_type = row[5]  # 第6列
        print(f"{sensor_type}\t1")  # 只输出这一行，供 Reducer 用