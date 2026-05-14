import oss2
import csv

auth = oss2.Auth()
endpoint = 'oss-cn-beijing.aliyuncs.com'
bucket_name = 'mini-project2'
bucket = oss2.Bucket(auth, endpoint, bucket_name)
object_key = 'Comp3006J MiniProject 2 Dataset.csv'

data = bucket.get_object(object_key).read().decode('utf-8').splitlines()
reader = csv.reader(data)
next(reader)

# 输出 <building,1> 只针对 WARNING/ERROR
for row in reader:
    status = row[8]
    building = row[2]
    if status in ('WARNING', 'ERROR'):
        print(f"{building}\t1")