C:\Users\26673\Desktop\assignment2>cd C:\Users\26673\Desktop\assignment2

C:\Users\26673\Desktop\assignment2>
C:\Users\26673\Desktop\assignment2>REM 清理旧输出

C:\Users\26673\Desktop\assignment2>hdfs dfs -rm -r /output/job1
Deleted /output/job1

C:\Users\26673\Desktop\assignment2>hdfs dfs -rm -r /output/job2
Deleted /output/job2

C:\Users\26673\Desktop\assignment2>hdfs dfs -rm -r /output/job3_step1
Deleted /output/job3_step1

C:\Users\26673\Desktop\assignment2>hdfs dfs -rm -r /output/job3_top10
Deleted /output/job3_top10

C:\Users\26673\Desktop\assignment2>
C:\Users\26673\Desktop\assignment2>REM Job 1: Sensor 类型统计

C:\Users\26673\Desktop\assignment2>hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /input/Comp3006J_MiniProject2_Dataset.csv -output /output/job1 -mapper "python mapper.py" -reducer "python reducer.py" -file mapreduce/job1_sensor_count/mapper.py -file mapreduce/job1_sensor_count/reducer.py
2026-05-14 13:00:10,579 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [mapreduce/job1_sensor_count/mapper.py, mapreduce/job1_sensor_count/reducer.py] [] C:\Users\26673\AppData\Local\Temp\streamjob9521537373137949807.jar tmpDir=null
2026-05-14 13:00:11,110 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2026-05-14 13:00:11,191 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2026-05-14 13:00:11,191 INFO impl.MetricsSystemImpl: JobTracker metrics system started
2026-05-14 13:00:11,207 WARN impl.MetricsSystemImpl: JobTracker metrics system already initialized!
2026-05-14 13:00:11,377 INFO mapred.FileInputFormat: Total input files to process : 1
2026-05-14 13:00:11,418 INFO mapreduce.JobSubmitter: number of splits:1
2026-05-14 13:00:11,506 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_local904832124_0001
2026-05-14 13:00:11,506 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-05-14 13:00:11,730 INFO mapred.LocalDistributedCacheManager: Localized file:/C:/Users/26673/Desktop/assignment2/mapreduce/job1_sensor_count/mapper.py as file:/C:/Users/26673/hadoop/tmp/mapred/local/job_local904832124_0001_29864c2d-b78d-45c8-8220-7d4037ef5bef/mapper.py
2026-05-14 13:00:11,748 INFO mapred.LocalDistributedCacheManager: Localized file:/C:/Users/26673/Desktop/assignment2/mapreduce/job1_sensor_count/reducer.py as file:/C:/Users/26673/hadoop/tmp/mapred/local/job_local904832124_0001_bc737395-0712-4235-9022-c00b5c0719b4/reducer.py
2026-05-14 13:00:11,804 INFO mapreduce.Job: The url to track the job: http://localhost:8080/
2026-05-14 13:00:11,806 INFO mapred.LocalJobRunner: OutputCommitter set in config null
2026-05-14 13:00:11,808 INFO mapreduce.Job: Running job: job_local904832124_0001
2026-05-14 13:00:11,811 INFO mapred.LocalJobRunner: OutputCommitter is org.apache.hadoop.mapred.FileOutputCommitter
2026-05-14 13:00:11,821 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:11,821 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:11,855 INFO mapred.LocalJobRunner: Waiting for map tasks
2026-05-14 13:00:11,857 INFO mapred.LocalJobRunner: Starting task: attempt_local904832124_0001_m_000000_0
2026-05-14 13:00:11,871 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:11,871 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:11,875 INFO util.ProcfsBasedProcessTree: ProcfsBasedProcessTree currently is supported only on Linux.
2026-05-14 13:00:11,894 INFO mapred.Task:  Using ResourceCalculatorProcessTree : org.apache.hadoop.yarn.util.WindowsBasedProcessTree@1bcf4ab8
2026-05-14 13:00:11,901 INFO mapred.MapTask: Processing split: hdfs://localhost:9000/input/Comp3006J_MiniProject2_Dataset.csv:0+3616957
2026-05-14 13:00:11,912 INFO mapred.MapTask: numReduceTasks: 1
2026-05-14 13:00:11,934 INFO mapred.MapTask: (EQUATOR) 0 kvi 26214396(104857584)
2026-05-14 13:00:11,934 INFO mapred.MapTask: mapreduce.task.io.sort.mb: 100
2026-05-14 13:00:11,934 INFO mapred.MapTask: soft limit at 83886080
2026-05-14 13:00:11,934 INFO mapred.MapTask: bufstart = 0; bufvoid = 104857600
2026-05-14 13:00:11,935 INFO mapred.MapTask: kvstart = 26214396; length = 6553600
2026-05-14 13:00:11,937 INFO mapred.MapTask: Map output collector class = org.apache.hadoop.mapred.MapTask$MapOutputBuffer
2026-05-14 13:00:11,961 INFO streaming.PipeMapRed: PipeMapRed exec [python, mapper.py]
2026-05-14 13:00:11,964 INFO Configuration.deprecation: mapred.work.output.dir is deprecated. Instead, use mapreduce.task.output.dir
2026-05-14 13:00:11,964 INFO Configuration.deprecation: mapred.local.dir is deprecated. Instead, use mapreduce.cluster.local.dir
2026-05-14 13:00:11,964 INFO Configuration.deprecation: map.input.file is deprecated. Instead, use mapreduce.map.input.file
2026-05-14 13:00:11,965 INFO Configuration.deprecation: map.input.length is deprecated. Instead, use mapreduce.map.input.length
2026-05-14 13:00:11,965 INFO Configuration.deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
2026-05-14 13:00:11,965 INFO Configuration.deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
2026-05-14 13:00:11,966 INFO Configuration.deprecation: map.input.start is deprecated. Instead, use mapreduce.map.input.start
2026-05-14 13:00:11,966 INFO Configuration.deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
2026-05-14 13:00:11,966 INFO Configuration.deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
2026-05-14 13:00:11,966 INFO Configuration.deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
2026-05-14 13:00:11,966 INFO Configuration.deprecation: mapred.skip.on is deprecated. Instead, use mapreduce.job.skiprecords
2026-05-14 13:00:11,967 INFO Configuration.deprecation: user.name is deprecated. Instead, use mapreduce.job.user.name
2026-05-14 13:00:12,012 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,012 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,013 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,017 INFO streaming.PipeMapRed: R/W/S=1000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,025 INFO streaming.PipeMapRed: Records R/W=3662/1
2026-05-14 13:00:12,047 INFO streaming.PipeMapRed: R/W/S=10000/7995/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,143 INFO streaming.PipeMapRed: MRErrorThread done
2026-05-14 13:00:12,144 INFO streaming.PipeMapRed: mapRedFinished
2026-05-14 13:00:12,146 INFO mapred.LocalJobRunner:
2026-05-14 13:00:12,146 INFO mapred.MapTask: Starting flush of map output
2026-05-14 13:00:12,146 INFO mapred.MapTask: Spilling map output
2026-05-14 13:00:12,147 INFO mapred.MapTask: bufstart = 0; bufend = 562217; bufvoid = 104857600
2026-05-14 13:00:12,147 INFO mapred.MapTask: kvstart = 26214396(104857584); kvend = 26014400(104057600); length = 199997/6553600
2026-05-14 13:00:12,191 INFO mapred.MapTask: Finished spill 0
2026-05-14 13:00:12,204 INFO mapred.Task: Task:attempt_local904832124_0001_m_000000_0 is done. And is in the process of committing
2026-05-14 13:00:12,207 INFO mapred.LocalJobRunner: Records R/W=3662/1
2026-05-14 13:00:12,207 INFO mapred.Task: Task 'attempt_local904832124_0001_m_000000_0' done.
2026-05-14 13:00:12,210 INFO mapred.Task: Final Counters for attempt_local904832124_0001_m_000000_0: Counters: 23
        File System Counters
                FILE: Number of bytes read=1385
                FILE: Number of bytes written=1309604
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=3616957
                HDFS: Number of bytes written=0
                HDFS: Number of read operations=5
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=1
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=50001
                Map output records=50000
                Map output bytes=562217
                Map output materialized bytes=662223
                Input split bytes=114
                Combine input records=0
                Spilled Records=50000
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=3
                Total committed heap usage (bytes)=193986560
        File Input Format Counters
                Bytes Read=3616957
2026-05-14 13:00:12,210 INFO mapred.LocalJobRunner: Finishing task: attempt_local904832124_0001_m_000000_0
2026-05-14 13:00:12,211 INFO mapred.LocalJobRunner: map task executor complete.
2026-05-14 13:00:12,212 INFO mapred.LocalJobRunner: Waiting for reduce tasks
2026-05-14 13:00:12,213 INFO mapred.LocalJobRunner: Starting task: attempt_local904832124_0001_r_000000_0
2026-05-14 13:00:12,217 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:12,217 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:12,218 INFO util.ProcfsBasedProcessTree: ProcfsBasedProcessTree currently is supported only on Linux.
2026-05-14 13:00:12,236 INFO mapred.Task:  Using ResourceCalculatorProcessTree : org.apache.hadoop.yarn.util.WindowsBasedProcessTree@5124e4b8
2026-05-14 13:00:12,238 INFO mapred.ReduceTask: Using ShuffleConsumerPlugin: org.apache.hadoop.mapreduce.task.reduce.Shuffle@67a3da8c
2026-05-14 13:00:12,239 WARN impl.MetricsSystemImpl: JobTracker metrics system already initialized!
2026-05-14 13:00:12,249 INFO reduce.MergeManagerImpl: MergerManager: memoryLimit=375809632, maxSingleShuffleLimit=93952408, mergeThreshold=248034368, ioSortFactor=10, memToMemMergeOutputsThreshold=10
2026-05-14 13:00:12,250 INFO reduce.EventFetcher: attempt_local904832124_0001_r_000000_0 Thread started: EventFetcher for fetching Map Completion Events
2026-05-14 13:00:12,266 INFO reduce.LocalFetcher: localfetcher#1 about to shuffle output of map attempt_local904832124_0001_m_000000_0 decomp: 662219 len: 662223 to MEMORY
2026-05-14 13:00:12,277 INFO reduce.InMemoryMapOutput: Read 662219 bytes from map-output for attempt_local904832124_0001_m_000000_0
2026-05-14 13:00:12,278 INFO reduce.MergeManagerImpl: closeInMemoryFile -> map-output of size: 662219, inMemoryMapOutputs.size() -> 1, commitMemory -> 0, usedMemory ->662219
2026-05-14 13:00:12,279 INFO reduce.EventFetcher: EventFetcher is interrupted.. Returning
2026-05-14 13:00:12,279 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:12,281 INFO reduce.MergeManagerImpl: finalMerge called with 1 in-memory map-outputs and 0 on-disk map-outputs
2026-05-14 13:00:12,287 INFO mapred.Merger: Merging 1 sorted segments
2026-05-14 13:00:12,288 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 662205 bytes
2026-05-14 13:00:12,310 INFO reduce.MergeManagerImpl: Merged 1 segments, 662219 bytes to disk to satisfy reduce memory limit
2026-05-14 13:00:12,310 INFO reduce.MergeManagerImpl: Merging 1 files, 662223 bytes from disk
2026-05-14 13:00:12,311 INFO reduce.MergeManagerImpl: Merging 0 segments, 0 bytes from memory into reduce
2026-05-14 13:00:12,311 INFO mapred.Merger: Merging 1 sorted segments
2026-05-14 13:00:12,322 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 662205 bytes
2026-05-14 13:00:12,323 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:12,341 INFO streaming.PipeMapRed: PipeMapRed exec [python, reducer.py]
2026-05-14 13:00:12,343 INFO Configuration.deprecation: mapred.job.tracker is deprecated. Instead, use mapreduce.jobtracker.address
2026-05-14 13:00:12,344 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
2026-05-14 13:00:12,371 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,371 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,373 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,375 INFO streaming.PipeMapRed: R/W/S=1000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,391 INFO streaming.PipeMapRed: R/W/S=10000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:12,429 INFO streaming.PipeMapRed: Records R/W=50000/1
2026-05-14 13:00:12,432 INFO streaming.PipeMapRed: MRErrorThread done
2026-05-14 13:00:12,433 INFO streaming.PipeMapRed: mapRedFinished
2026-05-14 13:00:12,509 INFO mapred.Task: Task:attempt_local904832124_0001_r_000000_0 is done. And is in the process of committing
2026-05-14 13:00:12,511 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:12,511 INFO mapred.Task: Task attempt_local904832124_0001_r_000000_0 is allowed to commit now
2026-05-14 13:00:12,529 INFO output.FileOutputCommitter: Saved output of task 'attempt_local904832124_0001_r_000000_0' to hdfs://localhost:9000/output/job1
2026-05-14 13:00:12,530 INFO mapred.LocalJobRunner: Records R/W=50000/1 > reduce
2026-05-14 13:00:12,530 INFO mapred.Task: Task 'attempt_local904832124_0001_r_000000_0' done.
2026-05-14 13:00:12,532 INFO mapred.Task: Final Counters for attempt_local904832124_0001_r_000000_0: Counters: 30
        File System Counters
                FILE: Number of bytes read=1325863
                FILE: Number of bytes written=1971827
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=3616957
                HDFS: Number of bytes written=84
                HDFS: Number of read operations=10
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=3
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Combine input records=0
                Combine output records=0
                Reduce input groups=6
                Reduce shuffle bytes=662223
                Reduce input records=50000
                Reduce output records=6
                Spilled Records=50000
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=0
                Total committed heap usage (bytes)=193986560
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Output Format Counters
                Bytes Written=84
2026-05-14 13:00:12,532 INFO mapred.LocalJobRunner: Finishing task: attempt_local904832124_0001_r_000000_0
2026-05-14 13:00:12,532 INFO mapred.LocalJobRunner: reduce task executor complete.
2026-05-14 13:00:12,820 INFO mapreduce.Job: Job job_local904832124_0001 running in uber mode : false
2026-05-14 13:00:12,822 INFO mapreduce.Job:  map 100% reduce 100%
2026-05-14 13:00:12,824 INFO mapreduce.Job: Job job_local904832124_0001 completed successfully
2026-05-14 13:00:12,829 INFO mapreduce.Job: Counters: 36
        File System Counters
                FILE: Number of bytes read=1327248
                FILE: Number of bytes written=3281431
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=7233914
                HDFS: Number of bytes written=84
                HDFS: Number of read operations=15
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=4
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=50001
                Map output records=50000
                Map output bytes=562217
                Map output materialized bytes=662223
                Input split bytes=114
                Combine input records=0
                Combine output records=0
                Reduce input groups=6
                Reduce shuffle bytes=662223
                Reduce input records=50000
                Reduce output records=6
                Spilled Records=100000
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=3
                Total committed heap usage (bytes)=387973120
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=3616957
        File Output Format Counters
                Bytes Written=84
2026-05-14 13:00:12,829 INFO streaming.StreamJob: Output directory: /output/job1

C:\Users\26673\Desktop\assignment2>
C:\Users\26673\Desktop\assignment2>REM Job 2: 按大楼统计 WARNING + ERROR

C:\Users\26673\Desktop\assignment2>hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /input/Comp3006J_MiniProject2_Dataset.csv -output /output/job2 -mapper "python mapper.py" -reducer "python reducer.py" -file mapreduce/job2_warning_by_building/mapper.py -file mapreduce/job2_warning_by_building/reducer.py
2026-05-14 13:00:13,594 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [mapreduce/job2_warning_by_building/mapper.py, mapreduce/job2_warning_by_building/reducer.py] [] C:\Users\26673\AppData\Local\Temp\streamjob7746411163635392295.jar tmpDir=null
2026-05-14 13:00:14,110 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2026-05-14 13:00:14,196 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2026-05-14 13:00:14,196 INFO impl.MetricsSystemImpl: JobTracker metrics system started
2026-05-14 13:00:14,207 WARN impl.MetricsSystemImpl: JobTracker metrics system already initialized!
2026-05-14 13:00:14,371 INFO mapred.FileInputFormat: Total input files to process : 1
2026-05-14 13:00:14,408 INFO mapreduce.JobSubmitter: number of splits:1
2026-05-14 13:00:14,494 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_local1094143507_0001
2026-05-14 13:00:14,495 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-05-14 13:00:14,717 INFO mapred.LocalDistributedCacheManager: Localized file:/C:/Users/26673/Desktop/assignment2/mapreduce/job2_warning_by_building/mapper.py as file:/C:/Users/26673/hadoop/tmp/mapred/local/job_local1094143507_0001_5b77dbf8-c63e-4ece-90ab-fd904e25648b/mapper.py
2026-05-14 13:00:14,735 INFO mapred.LocalDistributedCacheManager: Localized file:/C:/Users/26673/Desktop/assignment2/mapreduce/job2_warning_by_building/reducer.py as file:/C:/Users/26673/hadoop/tmp/mapred/local/job_local1094143507_0001_e54a707d-f6be-4745-9af7-49c1134c1f3c/reducer.py
2026-05-14 13:00:14,786 INFO mapreduce.Job: The url to track the job: http://localhost:8080/
2026-05-14 13:00:14,789 INFO mapred.LocalJobRunner: OutputCommitter set in config null
2026-05-14 13:00:14,791 INFO mapreduce.Job: Running job: job_local1094143507_0001
2026-05-14 13:00:14,794 INFO mapred.LocalJobRunner: OutputCommitter is org.apache.hadoop.mapred.FileOutputCommitter
2026-05-14 13:00:14,800 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:14,800 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:14,828 INFO mapred.LocalJobRunner: Waiting for map tasks
2026-05-14 13:00:14,830 INFO mapred.LocalJobRunner: Starting task: attempt_local1094143507_0001_m_000000_0
2026-05-14 13:00:14,846 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:14,846 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:14,850 INFO util.ProcfsBasedProcessTree: ProcfsBasedProcessTree currently is supported only on Linux.
2026-05-14 13:00:14,868 INFO mapred.Task:  Using ResourceCalculatorProcessTree : org.apache.hadoop.yarn.util.WindowsBasedProcessTree@1bcf4ab8
2026-05-14 13:00:14,875 INFO mapred.MapTask: Processing split: hdfs://localhost:9000/input/Comp3006J_MiniProject2_Dataset.csv:0+3616957
2026-05-14 13:00:14,887 INFO mapred.MapTask: numReduceTasks: 1
2026-05-14 13:00:14,910 INFO mapred.MapTask: (EQUATOR) 0 kvi 26214396(104857584)
2026-05-14 13:00:14,910 INFO mapred.MapTask: mapreduce.task.io.sort.mb: 100
2026-05-14 13:00:14,910 INFO mapred.MapTask: soft limit at 83886080
2026-05-14 13:00:14,910 INFO mapred.MapTask: bufstart = 0; bufvoid = 104857600
2026-05-14 13:00:14,910 INFO mapred.MapTask: kvstart = 26214396; length = 6553600
2026-05-14 13:00:14,912 INFO mapred.MapTask: Map output collector class = org.apache.hadoop.mapred.MapTask$MapOutputBuffer
2026-05-14 13:00:14,935 INFO streaming.PipeMapRed: PipeMapRed exec [python, mapper.py]
2026-05-14 13:00:14,938 INFO Configuration.deprecation: mapred.work.output.dir is deprecated. Instead, use mapreduce.task.output.dir
2026-05-14 13:00:14,938 INFO Configuration.deprecation: mapred.local.dir is deprecated. Instead, use mapreduce.cluster.local.dir
2026-05-14 13:00:14,939 INFO Configuration.deprecation: map.input.file is deprecated. Instead, use mapreduce.map.input.file
2026-05-14 13:00:14,939 INFO Configuration.deprecation: map.input.length is deprecated. Instead, use mapreduce.map.input.length
2026-05-14 13:00:14,939 INFO Configuration.deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
2026-05-14 13:00:14,939 INFO Configuration.deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
2026-05-14 13:00:14,940 INFO Configuration.deprecation: map.input.start is deprecated. Instead, use mapreduce.map.input.start
2026-05-14 13:00:14,940 INFO Configuration.deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
2026-05-14 13:00:14,940 INFO Configuration.deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
2026-05-14 13:00:14,940 INFO Configuration.deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
2026-05-14 13:00:14,940 INFO Configuration.deprecation: mapred.skip.on is deprecated. Instead, use mapreduce.job.skiprecords
2026-05-14 13:00:14,941 INFO Configuration.deprecation: user.name is deprecated. Instead, use mapreduce.job.user.name
2026-05-14 13:00:14,995 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:14,995 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:14,995 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:14,998 INFO streaming.PipeMapRed: R/W/S=1000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:15,020 INFO streaming.PipeMapRed: R/W/S=10000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:15,027 INFO streaming.PipeMapRed: Records R/W=12251/1
2026-05-14 13:00:15,112 INFO streaming.PipeMapRed: MRErrorThread done
2026-05-14 13:00:15,114 INFO streaming.PipeMapRed: mapRedFinished
2026-05-14 13:00:15,119 INFO mapred.LocalJobRunner:
2026-05-14 13:00:15,119 INFO mapred.MapTask: Starting flush of map output
2026-05-14 13:00:15,119 INFO mapred.MapTask: Spilling map output
2026-05-14 13:00:15,119 INFO mapred.MapTask: bufstart = 0; bufend = 78772; bufvoid = 104857600
2026-05-14 13:00:15,119 INFO mapred.MapTask: kvstart = 26214396(104857584); kvend = 26185124(104740496); length = 29273/6553600
2026-05-14 13:00:15,148 INFO mapred.MapTask: Finished spill 0
2026-05-14 13:00:15,167 INFO mapred.Task: Task:attempt_local1094143507_0001_m_000000_0 is done. And is in the process of committing
2026-05-14 13:00:15,171 INFO mapred.LocalJobRunner: Records R/W=12251/1
2026-05-14 13:00:15,171 INFO mapred.Task: Task 'attempt_local1094143507_0001_m_000000_0' done.
2026-05-14 13:00:15,177 INFO mapred.Task: Final Counters for attempt_local1094143507_0001_m_000000_0: Counters: 23
        File System Counters
                FILE: Number of bytes read=1432
                FILE: Number of bytes written=744012
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=3616957
                HDFS: Number of bytes written=0
                HDFS: Number of read operations=5
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=1
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=50001
                Map output records=7319
                Map output bytes=78772
                Map output materialized bytes=93416
                Input split bytes=114
                Combine input records=0
                Spilled Records=7319
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=3
                Total committed heap usage (bytes)=186646528
        File Input Format Counters
                Bytes Read=3616957
2026-05-14 13:00:15,177 INFO mapred.LocalJobRunner: Finishing task: attempt_local1094143507_0001_m_000000_0
2026-05-14 13:00:15,177 INFO mapred.LocalJobRunner: map task executor complete.
2026-05-14 13:00:15,181 INFO mapred.LocalJobRunner: Waiting for reduce tasks
2026-05-14 13:00:15,181 INFO mapred.LocalJobRunner: Starting task: attempt_local1094143507_0001_r_000000_0
2026-05-14 13:00:15,187 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:15,187 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:15,188 INFO util.ProcfsBasedProcessTree: ProcfsBasedProcessTree currently is supported only on Linux.
2026-05-14 13:00:15,207 INFO mapred.Task:  Using ResourceCalculatorProcessTree : org.apache.hadoop.yarn.util.WindowsBasedProcessTree@3a07fafd
2026-05-14 13:00:15,210 INFO mapred.ReduceTask: Using ShuffleConsumerPlugin: org.apache.hadoop.mapreduce.task.reduce.Shuffle@76a4e08c
2026-05-14 13:00:15,210 WARN impl.MetricsSystemImpl: JobTracker metrics system already initialized!
2026-05-14 13:00:15,219 INFO reduce.MergeManagerImpl: MergerManager: memoryLimit=375809632, maxSingleShuffleLimit=93952408, mergeThreshold=248034368, ioSortFactor=10, memToMemMergeOutputsThreshold=10
2026-05-14 13:00:15,222 INFO reduce.EventFetcher: attempt_local1094143507_0001_r_000000_0 Thread started: EventFetcher for fetching Map Completion Events
2026-05-14 13:00:15,237 INFO reduce.LocalFetcher: localfetcher#1 about to shuffle output of map attempt_local1094143507_0001_m_000000_0 decomp: 93412 len: 93416 to MEMORY
2026-05-14 13:00:15,263 INFO reduce.InMemoryMapOutput: Read 93412 bytes from map-output for attempt_local1094143507_0001_m_000000_0
2026-05-14 13:00:15,264 INFO reduce.MergeManagerImpl: closeInMemoryFile -> map-output of size: 93412, inMemoryMapOutputs.size() -> 1, commitMemory -> 0, usedMemory ->93412
2026-05-14 13:00:15,265 INFO reduce.EventFetcher: EventFetcher is interrupted.. Returning
2026-05-14 13:00:15,265 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:15,265 INFO reduce.MergeManagerImpl: finalMerge called with 1 in-memory map-outputs and 0 on-disk map-outputs
2026-05-14 13:00:15,271 INFO mapred.Merger: Merging 1 sorted segments
2026-05-14 13:00:15,271 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 93405 bytes
2026-05-14 13:00:15,281 INFO reduce.MergeManagerImpl: Merged 1 segments, 93412 bytes to disk to satisfy reduce memory limit
2026-05-14 13:00:15,282 INFO reduce.MergeManagerImpl: Merging 1 files, 93416 bytes from disk
2026-05-14 13:00:15,283 INFO reduce.MergeManagerImpl: Merging 0 segments, 0 bytes from memory into reduce
2026-05-14 13:00:15,283 INFO mapred.Merger: Merging 1 sorted segments
2026-05-14 13:00:15,308 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 93405 bytes
2026-05-14 13:00:15,309 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:15,328 INFO streaming.PipeMapRed: PipeMapRed exec [python, reducer.py]
2026-05-14 13:00:15,329 INFO Configuration.deprecation: mapred.job.tracker is deprecated. Instead, use mapreduce.jobtracker.address
2026-05-14 13:00:15,331 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
2026-05-14 13:00:15,358 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:15,358 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:15,359 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:15,362 INFO streaming.PipeMapRed: R/W/S=1000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:15,376 INFO streaming.PipeMapRed: Records R/W=7319/1
2026-05-14 13:00:15,378 INFO streaming.PipeMapRed: MRErrorThread done
2026-05-14 13:00:15,378 INFO streaming.PipeMapRed: mapRedFinished
2026-05-14 13:00:15,433 INFO mapred.Task: Task:attempt_local1094143507_0001_r_000000_0 is done. And is in the process of committing
2026-05-14 13:00:15,436 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:15,436 INFO mapred.Task: Task attempt_local1094143507_0001_r_000000_0 is allowed to commit now
2026-05-14 13:00:15,448 INFO output.FileOutputCommitter: Saved output of task 'attempt_local1094143507_0001_r_000000_0' to hdfs://localhost:9000/output/job2
2026-05-14 13:00:15,448 INFO mapred.LocalJobRunner: Records R/W=7319/1 > reduce
2026-05-14 13:00:15,450 INFO mapred.Task: Task 'attempt_local1094143507_0001_r_000000_0' done.
2026-05-14 13:00:15,450 INFO mapred.Task: Final Counters for attempt_local1094143507_0001_r_000000_0: Counters: 30
        File System Counters
                FILE: Number of bytes read=188296
                FILE: Number of bytes written=837428
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=3616957
                HDFS: Number of bytes written=81
                HDFS: Number of read operations=10
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=3
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Combine input records=0
                Combine output records=0
                Reduce input groups=6
                Reduce shuffle bytes=93416
                Reduce input records=7319
                Reduce output records=6
                Spilled Records=7319
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=0
                Total committed heap usage (bytes)=186646528
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Output Format Counters
                Bytes Written=81
2026-05-14 13:00:15,451 INFO mapred.LocalJobRunner: Finishing task: attempt_local1094143507_0001_r_000000_0
2026-05-14 13:00:15,451 INFO mapred.LocalJobRunner: reduce task executor complete.
2026-05-14 13:00:15,800 INFO mapreduce.Job: Job job_local1094143507_0001 running in uber mode : false
2026-05-14 13:00:15,802 INFO mapreduce.Job:  map 100% reduce 100%
2026-05-14 13:00:15,804 INFO mapreduce.Job: Job job_local1094143507_0001 completed successfully
2026-05-14 13:00:15,810 INFO mapreduce.Job: Counters: 36
        File System Counters
                FILE: Number of bytes read=189728
                FILE: Number of bytes written=1581440
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=7233914
                HDFS: Number of bytes written=81
                HDFS: Number of read operations=15
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=4
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=50001
                Map output records=7319
                Map output bytes=78772
                Map output materialized bytes=93416
                Input split bytes=114
                Combine input records=0
                Combine output records=0
                Reduce input groups=6
                Reduce shuffle bytes=93416
                Reduce input records=7319
                Reduce output records=6
                Spilled Records=14638
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=3
                Total committed heap usage (bytes)=373293056
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=3616957
        File Output Format Counters
                Bytes Written=81
2026-05-14 13:00:15,810 INFO streaming.StreamJob: Output directory: /output/job2

C:\Users\26673\Desktop\assignment2>
C:\Users\26673\Desktop\assignment2>REM Job 3 Step 1: 统计每个设备日志数

C:\Users\26673\Desktop\assignment2>hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /input/Comp3006J_MiniProject2_Dataset.csv -output /output/job3_step1 -mapper "python mapper.py" -reducer "python reducer.py" -file mapreduce/job3_top_devices/mapper.py -file mapreduce/job3_top_devices/reducer.py
2026-05-14 13:00:16,628 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [mapreduce/job3_top_devices/mapper.py, mapreduce/job3_top_devices/reducer.py] [] C:\Users\26673\AppData\Local\Temp\streamjob665468042687832579.jar tmpDir=null
2026-05-14 13:00:17,142 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2026-05-14 13:00:17,227 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2026-05-14 13:00:17,227 INFO impl.MetricsSystemImpl: JobTracker metrics system started
2026-05-14 13:00:17,241 WARN impl.MetricsSystemImpl: JobTracker metrics system already initialized!
2026-05-14 13:00:17,402 INFO mapred.FileInputFormat: Total input files to process : 1
2026-05-14 13:00:17,439 INFO mapreduce.JobSubmitter: number of splits:1
2026-05-14 13:00:17,524 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_local1863006855_0001
2026-05-14 13:00:17,524 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-05-14 13:00:17,767 INFO mapred.LocalDistributedCacheManager: Localized file:/C:/Users/26673/Desktop/assignment2/mapreduce/job3_top_devices/mapper.py as file:/C:/Users/26673/hadoop/tmp/mapred/local/job_local1863006855_0001_64ae684e-4ca2-45e5-9f59-3cab0e2bc2b1/mapper.py
2026-05-14 13:00:17,786 INFO mapred.LocalDistributedCacheManager: Localized file:/C:/Users/26673/Desktop/assignment2/mapreduce/job3_top_devices/reducer.py as file:/C:/Users/26673/hadoop/tmp/mapred/local/job_local1863006855_0001_9729390d-e5f7-4bca-a4ab-c418b049d9dd/reducer.py
2026-05-14 13:00:17,843 INFO mapreduce.Job: The url to track the job: http://localhost:8080/
2026-05-14 13:00:17,845 INFO mapred.LocalJobRunner: OutputCommitter set in config null
2026-05-14 13:00:17,847 INFO mapreduce.Job: Running job: job_local1863006855_0001
2026-05-14 13:00:17,851 INFO mapred.LocalJobRunner: OutputCommitter is org.apache.hadoop.mapred.FileOutputCommitter
2026-05-14 13:00:17,858 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:17,858 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:17,884 INFO mapred.LocalJobRunner: Waiting for map tasks
2026-05-14 13:00:17,886 INFO mapred.LocalJobRunner: Starting task: attempt_local1863006855_0001_m_000000_0
2026-05-14 13:00:17,903 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:17,903 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:17,907 INFO util.ProcfsBasedProcessTree: ProcfsBasedProcessTree currently is supported only on Linux.
2026-05-14 13:00:17,925 INFO mapred.Task:  Using ResourceCalculatorProcessTree : org.apache.hadoop.yarn.util.WindowsBasedProcessTree@4a9ef8bd
2026-05-14 13:00:17,931 INFO mapred.MapTask: Processing split: hdfs://localhost:9000/input/Comp3006J_MiniProject2_Dataset.csv:0+3616957
2026-05-14 13:00:17,941 INFO mapred.MapTask: numReduceTasks: 1
2026-05-14 13:00:17,963 INFO mapred.MapTask: (EQUATOR) 0 kvi 26214396(104857584)
2026-05-14 13:00:17,963 INFO mapred.MapTask: mapreduce.task.io.sort.mb: 100
2026-05-14 13:00:17,964 INFO mapred.MapTask: soft limit at 83886080
2026-05-14 13:00:17,964 INFO mapred.MapTask: bufstart = 0; bufvoid = 104857600
2026-05-14 13:00:17,964 INFO mapred.MapTask: kvstart = 26214396; length = 6553600
2026-05-14 13:00:17,966 INFO mapred.MapTask: Map output collector class = org.apache.hadoop.mapred.MapTask$MapOutputBuffer
2026-05-14 13:00:17,990 INFO streaming.PipeMapRed: PipeMapRed exec [python, mapper.py]
2026-05-14 13:00:17,992 INFO Configuration.deprecation: mapred.work.output.dir is deprecated. Instead, use mapreduce.task.output.dir
2026-05-14 13:00:17,993 INFO Configuration.deprecation: mapred.local.dir is deprecated. Instead, use mapreduce.cluster.local.dir
2026-05-14 13:00:17,993 INFO Configuration.deprecation: map.input.file is deprecated. Instead, use mapreduce.map.input.file
2026-05-14 13:00:17,993 INFO Configuration.deprecation: map.input.length is deprecated. Instead, use mapreduce.map.input.length
2026-05-14 13:00:17,994 INFO Configuration.deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
2026-05-14 13:00:17,994 INFO Configuration.deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
2026-05-14 13:00:17,994 INFO Configuration.deprecation: map.input.start is deprecated. Instead, use mapreduce.map.input.start
2026-05-14 13:00:17,994 INFO Configuration.deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
2026-05-14 13:00:17,995 INFO Configuration.deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
2026-05-14 13:00:17,995 INFO Configuration.deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
2026-05-14 13:00:17,995 INFO Configuration.deprecation: mapred.skip.on is deprecated. Instead, use mapreduce.job.skiprecords
2026-05-14 13:00:17,995 INFO Configuration.deprecation: user.name is deprecated. Instead, use mapreduce.job.user.name
2026-05-14 13:00:18,040 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,040 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,041 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,044 INFO streaming.PipeMapRed: R/W/S=1000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,052 INFO streaming.PipeMapRed: Records R/W=3612/1
2026-05-14 13:00:18,076 INFO streaming.PipeMapRed: R/W/S=10000/8190/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,176 INFO streaming.PipeMapRed: MRErrorThread done
2026-05-14 13:00:18,177 INFO streaming.PipeMapRed: mapRedFinished
2026-05-14 13:00:18,180 INFO mapred.LocalJobRunner:
2026-05-14 13:00:18,180 INFO mapred.MapTask: Starting flush of map output
2026-05-14 13:00:18,180 INFO mapred.MapTask: Spilling map output
2026-05-14 13:00:18,180 INFO mapred.MapTask: bufstart = 0; bufend = 400000; bufvoid = 104857600
2026-05-14 13:00:18,180 INFO mapred.MapTask: kvstart = 26214396(104857584); kvend = 26014400(104057600); length = 199997/6553600
2026-05-14 13:00:18,233 INFO mapred.MapTask: Finished spill 0
2026-05-14 13:00:18,255 INFO mapred.Task: Task:attempt_local1863006855_0001_m_000000_0 is done. And is in the process of committing
2026-05-14 13:00:18,258 INFO mapred.LocalJobRunner: Records R/W=3612/1
2026-05-14 13:00:18,259 INFO mapred.Task: Task 'attempt_local1863006855_0001_m_000000_0' done.
2026-05-14 13:00:18,268 INFO mapred.Task: Final Counters for attempt_local1863006855_0001_m_000000_0: Counters: 23
        File System Counters
                FILE: Number of bytes read=1458
                FILE: Number of bytes written=1150574
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=3616957
                HDFS: Number of bytes written=0
                HDFS: Number of read operations=5
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=1
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=50001
                Map output records=50000
                Map output bytes=400000
                Map output materialized bytes=500006
                Input split bytes=114
                Combine input records=0
                Spilled Records=50000
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=0
                Total committed heap usage (bytes)=179306496
        File Input Format Counters
                Bytes Read=3616957
2026-05-14 13:00:18,268 INFO mapred.LocalJobRunner: Finishing task: attempt_local1863006855_0001_m_000000_0
2026-05-14 13:00:18,268 INFO mapred.LocalJobRunner: map task executor complete.
2026-05-14 13:00:18,271 INFO mapred.LocalJobRunner: Waiting for reduce tasks
2026-05-14 13:00:18,272 INFO mapred.LocalJobRunner: Starting task: attempt_local1863006855_0001_r_000000_0
2026-05-14 13:00:18,277 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:18,277 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:18,278 INFO util.ProcfsBasedProcessTree: ProcfsBasedProcessTree currently is supported only on Linux.
2026-05-14 13:00:18,297 INFO mapred.Task:  Using ResourceCalculatorProcessTree : org.apache.hadoop.yarn.util.WindowsBasedProcessTree@3a07fafd
2026-05-14 13:00:18,299 INFO mapred.ReduceTask: Using ShuffleConsumerPlugin: org.apache.hadoop.mapreduce.task.reduce.Shuffle@76a4e08c
2026-05-14 13:00:18,300 WARN impl.MetricsSystemImpl: JobTracker metrics system already initialized!
2026-05-14 13:00:18,309 INFO reduce.MergeManagerImpl: MergerManager: memoryLimit=375809632, maxSingleShuffleLimit=93952408, mergeThreshold=248034368, ioSortFactor=10, memToMemMergeOutputsThreshold=10
2026-05-14 13:00:18,310 INFO reduce.EventFetcher: attempt_local1863006855_0001_r_000000_0 Thread started: EventFetcher for fetching Map Completion Events
2026-05-14 13:00:18,325 INFO reduce.LocalFetcher: localfetcher#1 about to shuffle output of map attempt_local1863006855_0001_m_000000_0 decomp: 500002 len: 500006 to MEMORY
2026-05-14 13:00:18,338 INFO reduce.InMemoryMapOutput: Read 500002 bytes from map-output for attempt_local1863006855_0001_m_000000_0
2026-05-14 13:00:18,339 INFO reduce.MergeManagerImpl: closeInMemoryFile -> map-output of size: 500002, inMemoryMapOutputs.size() -> 1, commitMemory -> 0, usedMemory ->500002
2026-05-14 13:00:18,341 INFO reduce.EventFetcher: EventFetcher is interrupted.. Returning
2026-05-14 13:00:18,341 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:18,343 INFO reduce.MergeManagerImpl: finalMerge called with 1 in-memory map-outputs and 0 on-disk map-outputs
2026-05-14 13:00:18,348 INFO mapred.Merger: Merging 1 sorted segments
2026-05-14 13:00:18,349 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 499994 bytes
2026-05-14 13:00:18,371 INFO reduce.MergeManagerImpl: Merged 1 segments, 500002 bytes to disk to satisfy reduce memory limit
2026-05-14 13:00:18,372 INFO reduce.MergeManagerImpl: Merging 1 files, 500006 bytes from disk
2026-05-14 13:00:18,372 INFO reduce.MergeManagerImpl: Merging 0 segments, 0 bytes from memory into reduce
2026-05-14 13:00:18,372 INFO mapred.Merger: Merging 1 sorted segments
2026-05-14 13:00:18,385 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 499994 bytes
2026-05-14 13:00:18,385 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:18,404 INFO streaming.PipeMapRed: PipeMapRed exec [python, reducer.py]
2026-05-14 13:00:18,407 INFO Configuration.deprecation: mapred.job.tracker is deprecated. Instead, use mapreduce.jobtracker.address
2026-05-14 13:00:18,407 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
2026-05-14 13:00:18,434 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,435 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,436 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,439 INFO streaming.PipeMapRed: R/W/S=1000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,447 INFO streaming.PipeMapRed: R/W/S=10000/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:18,486 INFO streaming.PipeMapRed: Records R/W=50000/1
2026-05-14 13:00:18,488 INFO streaming.PipeMapRed: MRErrorThread done
2026-05-14 13:00:18,489 INFO streaming.PipeMapRed: mapRedFinished
2026-05-14 13:00:18,568 INFO mapred.Task: Task:attempt_local1863006855_0001_r_000000_0 is done. And is in the process of committing
2026-05-14 13:00:18,570 INFO mapred.LocalJobRunner: 1 / 1 copied.
2026-05-14 13:00:18,571 INFO mapred.Task: Task attempt_local1863006855_0001_r_000000_0 is allowed to commit now
2026-05-14 13:00:18,591 INFO output.FileOutputCommitter: Saved output of task 'attempt_local1863006855_0001_r_000000_0' to hdfs://localhost:9000/output/job3_step1
2026-05-14 13:00:18,592 INFO mapred.LocalJobRunner: Records R/W=50000/1 > reduce
2026-05-14 13:00:18,592 INFO mapred.Task: Task 'attempt_local1863006855_0001_r_000000_0' done.
2026-05-14 13:00:18,593 INFO mapred.Task: Final Counters for attempt_local1863006855_0001_r_000000_0: Counters: 30
        File System Counters
                FILE: Number of bytes read=1001502
                FILE: Number of bytes written=1650580
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=3616957
                HDFS: Number of bytes written=100
                HDFS: Number of read operations=10
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=3
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Combine input records=0
                Combine output records=0
                Reduce input groups=648
                Reduce shuffle bytes=500006
                Reduce input records=50000
                Reduce output records=10
                Spilled Records=50000
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=3
                Total committed heap usage (bytes)=179306496
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Output Format Counters
                Bytes Written=100
2026-05-14 13:00:18,593 INFO mapred.LocalJobRunner: Finishing task: attempt_local1863006855_0001_r_000000_0
2026-05-14 13:00:18,593 INFO mapred.LocalJobRunner: reduce task executor complete.
2026-05-14 13:00:18,857 INFO mapreduce.Job: Job job_local1863006855_0001 running in uber mode : false
2026-05-14 13:00:18,859 INFO mapreduce.Job:  map 100% reduce 100%
2026-05-14 13:00:18,861 INFO mapreduce.Job: Job job_local1863006855_0001 completed successfully
2026-05-14 13:00:18,866 INFO mapreduce.Job: Counters: 36
        File System Counters
                FILE: Number of bytes read=1002960
                FILE: Number of bytes written=2801154
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=7233914
                HDFS: Number of bytes written=100
                HDFS: Number of read operations=15
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=4
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=50001
                Map output records=50000
                Map output bytes=400000
                Map output materialized bytes=500006
                Input split bytes=114
                Combine input records=0
                Combine output records=0
                Reduce input groups=648
                Reduce shuffle bytes=500006
                Reduce input records=50000
                Reduce output records=10
                Spilled Records=100000
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=3
                Total committed heap usage (bytes)=358612992
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=3616957
        File Output Format Counters
                Bytes Written=100
2026-05-14 13:00:18,866 INFO streaming.StreamJob: Output directory: /output/job3_step1

C:\Users\26673\Desktop\assignment2>
C:\Users\26673\Desktop\assignment2>REM Job 3 Step 2: 取 Top 10

C:\Users\26673\Desktop\assignment2>hadoop jar C:\development\hadoop\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -input /output/job3_step1 -output /output/job3_top10 -mapper "python top10_sort.py" -reducer "NONE" -file mapreduce/job3_top_devices/top10_sort.py
2026-05-14 13:00:19,651 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [mapreduce/job3_top_devices/top10_sort.py] [] C:\Users\26673\AppData\Local\Temp\streamjob5600566460746359264.jar tmpDir=null
2026-05-14 13:00:20,184 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2026-05-14 13:00:20,271 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2026-05-14 13:00:20,271 INFO impl.MetricsSystemImpl: JobTracker metrics system started
2026-05-14 13:00:20,282 WARN impl.MetricsSystemImpl: JobTracker metrics system already initialized!
2026-05-14 13:00:20,466 INFO mapred.FileInputFormat: Total input files to process : 1
2026-05-14 13:00:20,480 INFO mapreduce.JobSubmitter: number of splits:1
2026-05-14 13:00:20,561 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_local1446293073_0001
2026-05-14 13:00:20,562 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-05-14 13:00:20,779 INFO mapred.LocalDistributedCacheManager: Localized file:/C:/Users/26673/Desktop/assignment2/mapreduce/job3_top_devices/top10_sort.py as file:/C:/Users/26673/hadoop/tmp/mapred/local/job_local1446293073_0001_d995b005-f6d2-46df-a216-9d76c7646e19/top10_sort.py
2026-05-14 13:00:20,835 INFO mapreduce.Job: The url to track the job: http://localhost:8080/
2026-05-14 13:00:20,837 INFO mapred.LocalJobRunner: OutputCommitter set in config null
2026-05-14 13:00:20,840 INFO mapreduce.Job: Running job: job_local1446293073_0001
2026-05-14 13:00:20,844 INFO mapred.LocalJobRunner: OutputCommitter is org.apache.hadoop.mapred.FileOutputCommitter
2026-05-14 13:00:20,852 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:20,852 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:20,878 INFO mapred.LocalJobRunner: Waiting for map tasks
2026-05-14 13:00:20,881 INFO mapred.LocalJobRunner: Starting task: attempt_local1446293073_0001_m_000000_0
2026-05-14 13:00:20,895 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 2
2026-05-14 13:00:20,895 INFO output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2026-05-14 13:00:20,899 INFO util.ProcfsBasedProcessTree: ProcfsBasedProcessTree currently is supported only on Linux.
2026-05-14 13:00:20,918 INFO mapred.Task:  Using ResourceCalculatorProcessTree : org.apache.hadoop.yarn.util.WindowsBasedProcessTree@14afd3c3
2026-05-14 13:00:20,925 INFO mapred.MapTask: Processing split: hdfs://localhost:9000/output/job3_step1/part-00000:0+100
2026-05-14 13:00:20,938 INFO mapred.MapTask: numReduceTasks: 0
2026-05-14 13:00:20,990 INFO streaming.PipeMapRed: PipeMapRed exec [python, top10_sort.py]
2026-05-14 13:00:20,992 INFO Configuration.deprecation: mapred.work.output.dir is deprecated. Instead, use mapreduce.task.output.dir
2026-05-14 13:00:20,993 INFO Configuration.deprecation: mapred.local.dir is deprecated. Instead, use mapreduce.cluster.local.dir
2026-05-14 13:00:20,993 INFO Configuration.deprecation: map.input.file is deprecated. Instead, use mapreduce.map.input.file
2026-05-14 13:00:20,993 INFO Configuration.deprecation: map.input.length is deprecated. Instead, use mapreduce.map.input.length
2026-05-14 13:00:20,993 INFO Configuration.deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
2026-05-14 13:00:20,994 INFO Configuration.deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
2026-05-14 13:00:20,994 INFO Configuration.deprecation: map.input.start is deprecated. Instead, use mapreduce.map.input.start
2026-05-14 13:00:20,994 INFO Configuration.deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
2026-05-14 13:00:20,994 INFO Configuration.deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
2026-05-14 13:00:20,995 INFO Configuration.deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
2026-05-14 13:00:20,995 INFO Configuration.deprecation: mapred.skip.on is deprecated. Instead, use mapreduce.job.skiprecords
2026-05-14 13:00:20,995 INFO Configuration.deprecation: user.name is deprecated. Instead, use mapreduce.job.user.name
2026-05-14 13:00:21,045 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:21,046 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
2026-05-14 13:00:21,048 INFO streaming.PipeMapRed: Records R/W=10/1
2026-05-14 13:00:21,049 INFO streaming.PipeMapRed: MRErrorThread done
2026-05-14 13:00:21,050 INFO streaming.PipeMapRed: mapRedFinished
2026-05-14 13:00:21,052 INFO mapred.LocalJobRunner:
2026-05-14 13:00:21,106 INFO mapred.Task: Task:attempt_local1446293073_0001_m_000000_0 is done. And is in the process of committing
2026-05-14 13:00:21,109 INFO mapred.LocalJobRunner:
2026-05-14 13:00:21,109 INFO mapred.Task: Task attempt_local1446293073_0001_m_000000_0 is allowed to commit now
2026-05-14 13:00:21,118 INFO output.FileOutputCommitter: Saved output of task 'attempt_local1446293073_0001_m_000000_0' to hdfs://localhost:9000/output/job3_top10
2026-05-14 13:00:21,120 INFO mapred.LocalJobRunner: Records R/W=10/1
2026-05-14 13:00:21,120 INFO mapred.Task: Task 'attempt_local1446293073_0001_m_000000_0' done.
2026-05-14 13:00:21,127 INFO mapred.Task: Final Counters for attempt_local1446293073_0001_m_000000_0: Counters: 21
        File System Counters
                FILE: Number of bytes read=875
                FILE: Number of bytes written=648583
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=100
                HDFS: Number of bytes written=100
                HDFS: Number of read operations=9
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=3
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=10
                Map output records=10
                Input split bytes=102
                Spilled Records=0
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=0
                Total committed heap usage (bytes)=80740352
        File Input Format Counters
                Bytes Read=100
        File Output Format Counters
                Bytes Written=100
2026-05-14 13:00:21,127 INFO mapred.LocalJobRunner: Finishing task: attempt_local1446293073_0001_m_000000_0
2026-05-14 13:00:21,127 INFO mapred.LocalJobRunner: map task executor complete.
2026-05-14 13:00:21,853 INFO mapreduce.Job: Job job_local1446293073_0001 running in uber mode : false
2026-05-14 13:00:21,855 INFO mapreduce.Job:  map 100% reduce 0%
2026-05-14 13:00:21,859 INFO mapreduce.Job: Job job_local1446293073_0001 completed successfully
2026-05-14 13:00:21,863 INFO mapreduce.Job: Counters: 21
        File System Counters
                FILE: Number of bytes read=875
                FILE: Number of bytes written=648583
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=100
                HDFS: Number of bytes written=100
                HDFS: Number of read operations=9
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=3
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=10
                Map output records=10
                Input split bytes=102
                Spilled Records=0
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=0
                Total committed heap usage (bytes)=80740352
        File Input Format Counters
                Bytes Read=100
        File Output Format Counters
                Bytes Written=100
2026-05-14 13:00:21,863 INFO streaming.StreamJob: Output directory: /output/job3_top10

C:\Users\26673\Desktop\assignment2>
C:\Users\26673\Desktop\assignment2>REM 查看结果

C:\Users\26673\Desktop\assignment2>hdfs dfs -cat /output/job1/part-00000
air_quality     12661
door    9246
energy  5648
humidity        5757
motion  5510
temperature     11178

C:\Users\26673\Desktop\assignment2>hdfs dfs -cat /output/job2/part-00000
Arts    657
Business        707
Engineering     879
Library 1622
Science 2788
SportsCentre    666

C:\Users\26673\Desktop\assignment2>hdfs dfs -cat /output/job3_top10/part-00000
D0302   695
D0306   678
D0315   674
D0307   673
D0310   670
D0312   668
D0314   668
D0311   663
D0304   657
D0313   657
