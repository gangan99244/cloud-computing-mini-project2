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
    key, value = parts
    counts[key] += int(value)

for key, count in counts.items():
    print(f"{key}\t{count}")