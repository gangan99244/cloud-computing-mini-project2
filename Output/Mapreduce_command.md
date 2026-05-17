cd C:\Users\26673\Desktop\assignment2

REM 清理旧输出
hdfs dfs -rm -r /output/job1
hdfs dfs -rm -r /output/job2
hdfs dfs -rm -r /output/job3_step1
hdfs dfs -rm -r /output/job3_top10

REM Job 1: Sensor 类型统计
hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /input/Comp3006J_MiniProject2_Dataset.csv -output /output/job1 -mapper "python mapper.py" -reducer "python reducer.py" -file mapreduce/job1_sensor_count/mapper.py -file mapreduce/job1_sensor_count/reducer.py

REM Job 2: 按大楼统计 WARNING + ERROR
hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /input/Comp3006J_MiniProject2_Dataset.csv -output /output/job2 -mapper "python mapper.py" -reducer "python reducer.py" -file mapreduce/job2_warning_by_building/mapper.py -file mapreduce/job2_warning_by_building/reducer.py

REM Job 3 Step 1: 统计每个设备日志数
hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /input/Comp3006J_MiniProject2_Dataset.csv -output /output/job3_step1 -mapper "python mapper.py" -reducer "python reducer.py" -file mapreduce/job3_top_devices/mapper.py -file mapreduce/job3_top_devices/reducer.py

REM Job 3 Step 2: 取 Top 10
hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /output/job3_step1 -output /output/job3_top10 -mapper "python top10_sort.py" -reducer "NONE" -file mapreduce/job3_top_devices/top10_sort.py

REM 查看结果
hdfs dfs -cat /output/job1/part-00000
hdfs dfs -cat /output/job2/part-00000
hdfs dfs -cat /output/job3_top10/part-00000
