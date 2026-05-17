PS C:\Users\26673\Desktop\assignment2\py>  python task4_ray_anomaly.py
============================================================
Task 4 - Ray Anomaly Detection
============================================================
[INFO] Reading from S3: s3://mini-project2-iot-log/Comp3006J MiniProject 2 Dataset.csv
[INFO] Total rows: 50000
[INFO] Split into 4 batches (~12500 rows each)
2026-05-12 14:36:22,508 INFO worker.py:2012 -- Started a local Ray instance.
D:\Program Files\Python311\Lib\site-packages\ray\_private\worker.py:2051: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
  warnings.warn(
[INFO] Ray started. Dashboard: http://127.0.0.1:8265
[INFO] Anomalous devices found: 95
============================================================
device_id,building,reason
D0001,Library,repeated errors; repeated high temperature
D0002,Library,repeated errors; repeated high temperature
D0003,Library,repeated errors; repeated high temperature
D0004,Library,repeated errors; repeated high temperature
D0005,Library,repeated high temperature
D0006,Library,repeated errors; repeated high temperature
D0007,Library,repeated errors; repeated high temperature
D0008,Library,repeated errors; repeated high temperature
D0009,Library,low battery; repeated errors; repeated high temperature
D0010,Library,repeated errors; repeated high temperature
D0022,Library,repeated errors
D0038,Library,repeated errors
D0044,Library,low battery
D0048,Library,low battery
D0090,Library,repeated errors
D0095,Library,repeated errors
D0101,Library,repeated errors
D0102,Library,repeated errors
D0103,Library,repeated errors
D0104,Library,repeated errors
D0105,Library,repeated errors
D0106,Library,repeated errors
D0107,Library,repeated errors
D0108,Library,repeated errors
D0109,Engineering,repeated errors
D0110,Engineering,repeated errors
D0124,Engineering,low battery
D0146,Engineering,repeated errors
D0164,Engineering,repeated errors
D0166,Engineering,low battery
D0167,Engineering,repeated errors
D0179,Engineering,low battery
D0190,Engineering,repeated errors
D0201,Engineering,low battery
D0209,Engineering,repeated errors
D0221,Science,low battery
D0222,Science,low battery
D0223,Science,low battery
D0224,Science,low battery
D0225,Science,low battery
D0226,Science,low battery
D0227,Science,low battery
D0228,Science,low battery
D0229,Science,low battery
D0230,Science,low battery
D0231,Science,low battery
D0232,Science,low battery
D0233,Science,low battery
D0234,Science,low battery
D0235,Science,low battery
D0245,Science,repeated errors
D0252,Science,repeated errors
D0256,Science,low battery; repeated errors
D0259,Science,repeated errors
D0270,Science,low battery; repeated errors
D0274,Science,low battery
D0283,Science,repeated errors
D0290,Science,low battery; repeated errors
D0296,Science,repeated errors
D0301,Science,repeated errors
D0302,Science,repeated errors
D0303,Science,repeated errors
D0304,Science,repeated errors
D0305,Science,repeated errors
D0306,Science,repeated errors
D0307,Science,repeated errors
D0308,Science,repeated errors
D0309,Science,repeated errors
D0310,Science,repeated errors
D0311,Science,repeated errors
D0312,Science,repeated errors
D0313,Science,repeated errors
D0314,Science,repeated errors
D0315,Science,repeated errors
D0330,Business,repeated errors
D0341,Business,repeated errors
D0342,Business,low battery
D0373,Business,repeated errors
D0380,Business,low battery
D0382,Business,repeated errors
D0413,Business,repeated errors
D0420,Business,repeated errors
D0431,Business,repeated errors
D0435,Arts,repeated errors
D0436,Arts,low battery
D0440,Arts,repeated errors
D0494,Arts,low battery
D0513,Arts,low battery
D0516,Arts,repeated errors
D0519,Arts,repeated errors
D0525,Arts,repeated errors
D0597,SportsCentre,repeated errors
D0604,SportsCentre,low battery
D0614,SportsCentre,low battery
D0620,SportsCentre,low battery
PS C:\Users\26673\Desktop\assignment2\py> 