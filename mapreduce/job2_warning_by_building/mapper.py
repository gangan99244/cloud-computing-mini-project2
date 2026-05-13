import csv
csv_file = r"D:\桌面\cloud compute\mini-project2\Comp3006J MiniProject 2 Dataset.csv"

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    for row in reader:
        status = row[8]  # 第9列是 status
        building = row[2]  # 第3列是 building
        if status in ('WARNING', 'ERROR'):
            print(f"{building}\t1")