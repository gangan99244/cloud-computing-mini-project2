import oss2
import csv

# 使用 ECS 实例角色访问 OSS
auth = oss2.Auth()  # ECS 实例角色会自动提供临时凭证
endpoint = 'oss-cn-beijing.aliyuncs.com'  # 修改为你的 OSS 区域
bucket_name = 'mini-project2'
bucket = oss2.Bucket(auth, endpoint, bucket_name)
object_key = 'Comp3006J MiniProject 2 Dataset.csv'

# 读取 CSV
data = bucket.get_object(object_key).read().decode('utf-8').splitlines()
reader = csv.reader(data)
next(reader)  # 跳过表头

# 输出 <sensor_type,1>
for row in reader:
    sensor_type = row[5]
    print(f"{sensor_type}\t1")