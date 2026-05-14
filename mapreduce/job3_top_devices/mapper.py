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

# 输出 <device_id,1>
for row in reader:
    device_id = row[1]
    print(f"{device_id}\t1")