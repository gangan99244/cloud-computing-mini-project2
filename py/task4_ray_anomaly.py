#!/usr/bin/env python3
"""
Task 4 - Ray-based IoT Device Anomaly Detection
================================================
Environment: Local Ray on Windows 11

Anomaly conditions (any one triggers alert):
  1. battery_level < 20                         → low battery
  2. status == "ERROR"     >= 3 times per device → repeated errors
  3. sensor_type == "temperature" and value > 32 >= 3 times per device
                                                  → repeated high temperature

Usage:
  python task4_ray_anomaly.py
  python task4_ray_anomaly.py --local          # read from local CSV instead of S3
  python task4_ray_anomaly.py --batches 8      # number of parallel batches (default 4)
"""

import argparse
import csv
import io
import os
import sys
from collections import defaultdict

import ray

# S3 configuration (adjust if using a different S3-compatible service)
S3_BUCKET = "mini-project2-iot-log"
S3_KEY = "Comp3006J MiniProject 2 Dataset.csv"
LOCAL_CSV = os.path.join(os.path.dirname(__file__), "..", "Comp3006J_MiniProject2_Dataset.csv")


def read_rows_from_s3():
    """Read CSV rows from S3 via boto3 (works with any S3-compatible API)."""
    import boto3

    s3 = boto3.client("s3")
    resp = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
    body = resp["Body"].read().decode("utf-8")
    reader = csv.DictReader(io.StringIO(body))
    return list(reader)


def read_rows_from_local():
    """Read CSV rows from the local file."""
    path = os.path.abspath(LOCAL_CSV)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)



# Ray remote task – process one batch of rows
@ray.remote
def detect_anomalies_batch(rows):
    """
    Analyse a batch of sensor rows and return per-device anomaly info.

    Returns: dict  { device_id: {"building": str, "reasons": set[str]} }
    """
    device_info = {}            # device_id -> building
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

        # Condition 1: low battery
        try:
            if float(battery) < 20:
                low_battery_devices.add(did)
        except (ValueError, TypeError):
            pass

        # Condition 2: ERROR status
        if status == "ERROR":
            error_count[did] += 1

        # Condition 3: high temperature
        if sensor_type == "temperature":
            try:
                if float(value) > 32:
                    high_temp_count[did] += 1
            except (ValueError, TypeError):
                pass

    # Collect anomalies
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



# Merge results from all batches
def merge_results(batch_results):
    """Merge anomaly dicts from parallel batches, combining reasons."""
    merged = {}
    for partial in batch_results:
        for did, info in partial.items():
            if did not in merged:
                merged[did] = {"building": info["building"], "reasons": set(info["reasons"])}
            else:
                merged[did]["reasons"].update(info["reasons"])
    return merged


# Output
def print_results(anomalies):
    """Print results as CSV to stdout."""
    writer = csv.writer(sys.stdout)
    writer.writerow(["device_id", "building", "reason"])
    for did in sorted(anomalies):
        info = anomalies[did]
        reason = "; ".join(sorted(info["reasons"]))
        writer.writerow([did, info["building"], reason])


# Main
def main():
    parser = argparse.ArgumentParser(description="Ray Anomaly Detection")
    parser.add_argument("--local", action="store_true",
                        help="Read from local CSV instead of S3")
    parser.add_argument("--batches", type=int, default=4,
                        help="Number of parallel batches (default 4)")
    args = parser.parse_args()

    # --- 0. Environment info ---
    print("=" * 60, file=sys.stderr)
    print("Task 4 - Ray Anomaly Detection", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    # --- 1. Read data ---
    if args.local:
        print(f"[INFO] Reading from local file: {os.path.abspath(LOCAL_CSV)}", file=sys.stderr)
        rows = read_rows_from_local()
    else:
        print(f"[INFO] Reading from S3: s3://{S3_BUCKET}/{S3_KEY}", file=sys.stderr)
        rows = read_rows_from_s3()

    total = len(rows)
    print(f"[INFO] Total rows: {total}", file=sys.stderr)

    # --- 2. Split into batches ---
    n_batches = args.batches
    batch_size = (total + n_batches - 1) // n_batches
    batches = [rows[i:i + batch_size] for i in range(0, total, batch_size)]
    print(f"[INFO] Split into {len(batches)} batches (~{batch_size} rows each)", file=sys.stderr)

    # --- 3. Initialize Ray & launch parallel tasks ---
    ray.init(ignore_reinit_error=True)
    print(f"[INFO] Ray started. Dashboard: http://127.0.0.1:8265", file=sys.stderr)

    futures = [detect_anomalies_batch.remote(b) for b in batches]
    batch_results = ray.get(futures)

    # --- 4. Merge & output ---
    anomalies = merge_results(batch_results)
    print(f"[INFO] Anomalous devices found: {len(anomalies)}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    print_results(anomalies)

    ray.shutdown()


if __name__ == "__main__":
    main()
