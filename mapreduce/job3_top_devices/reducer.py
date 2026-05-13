import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    device, value = parts
    counts[device] += int(value)

# 排序取前10
top10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

for device, count in top10:
    print(f"{device}\t{count}")