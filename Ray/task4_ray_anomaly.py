#!/usr/bin/env python3
"""Task 4 - Ray anomaly detection for IoT devices."""

import argparse
import csv
import io
import os
import sys
import time
from collections import defaultdict

import ray

S3_BUCKET = "mini-project2-iot-log"
S3_KEY = "Comp3006J MiniProject 2 Dataset.csv"
LOCAL_CSV = os.path.join(os.path.dirname(__file__), "..", "Comp3006J_MiniProject2_Dataset.csv")


def read_rows_from_s3():
    import boto3
    s3 = boto3.client("s3")
    resp = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
    body = resp["Body"].read().decode("utf-8")
    reader = csv.DictReader(io.StringIO(body))
    return list(reader)


def read_rows_from_local():
    path = os.path.abspath(LOCAL_CSV)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


@ray.remote
def detect_anomalies_batch(rows):
    device_info = {}
    error_count = defaultdict(int)
    high_temp_count = defaultdict(int)
    low_battery_devices = set()

    for row in rows:
        did = row["device_id"]
        building = row["building"]
        status = row["status"]
        sensor_type = row["sensor_type"]
        value = row["value"]
        battery = row["battery_level"]

        device_info[did] = building

        # low battery
        try:
            if float(battery) < 20:
                low_battery_devices.add(did)
        except (ValueError, TypeError):
            pass

        # ERROR status
        if status == "ERROR":
            error_count[did] += 1

        # high temperature
        if sensor_type == "temperature":
            try:
                if float(value) > 32:
                    high_temp_count[did] += 1
            except (ValueError, TypeError):
                pass

    # collect anomalies
    anomalies = {}
    for did, building in device_info.items():
        reasons = set()
        if did in low_battery_devices:
            reasons.add("low battery")
        if error_count[did] >= 3:
            reasons.add("repeated errors")
        if high_temp_count[did] >= 3:
            reasons.add("repeated high temperature")
        if reasons:
            anomalies[did] = {"building": building, "reasons": reasons}

    return anomalies


def merge_results(batch_results):
    merged = {}
    for partial in batch_results:
        for did, info in partial.items():
            if did not in merged:
                merged[did] = {"building": info["building"], "reasons": set(info["reasons"])}
            else:
                merged[did]["reasons"].update(info["reasons"])
    return merged


def print_results(anomalies):
    writer = csv.writer(sys.stdout)
    writer.writerow(["device_id", "building", "reason"])
    for did in sorted(anomalies):
        info = anomalies[did]
        reason = "; ".join(sorted(info["reasons"]))
        writer.writerow([did, info["building"], reason])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true", help="Read from local CSV")
    parser.add_argument("--batches", type=int, default=4, help="Number of batches")
    args = parser.parse_args()

    print("Task 4 - Ray Anomaly Detection", file=sys.stderr)

    t0 = time.time()
    if args.local:
        print(f"Reading from local: {LOCAL_CSV}", file=sys.stderr)
        rows = read_rows_from_local()
    else:
        print(f"Reading from S3: {S3_BUCKET}/{S3_KEY}", file=sys.stderr)
        rows = read_rows_from_s3()

    total = len(rows)
    print(f"Total rows: {total}", file=sys.stderr)

    n_batches = args.batches
    batch_size = (total + n_batches - 1) // n_batches
    batches = [rows[i:i + batch_size] for i in range(0, total, batch_size)]

    t2 = time.time()
    ray.init(ignore_reinit_error=True)
    print(f"Ray init: {time.time() - t2:.2f}s", file=sys.stderr)

    t3 = time.time()
    futures = [detect_anomalies_batch.remote(b) for b in batches]
    batch_results = ray.get(futures)
    print(f"Execution: {time.time() - t3:.2f}s", file=sys.stderr)

    anomalies = merge_results(batch_results)
    print(f"Found {len(anomalies)} abnormal devices", file=sys.stderr)

    print_results(anomalies)
    print(f"Total runtime: {time.time() - t0:.2f}s", file=sys.stderr)

    ray.shutdown()


if __name__ == "__main__":
    main()