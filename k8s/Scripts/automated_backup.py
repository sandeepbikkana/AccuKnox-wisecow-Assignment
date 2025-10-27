#!/usr/bin/env python3
"""
Automated Backup Script
1. Creates a local backup of a directory.
2. Uploads the backup to an AWS S3 bucket.
3. Logs success or failure.
"""

import os
import shutil
import boto3
import datetime
from botocore.exceptions import NoCredentialsError, ClientError


SOURCE_DIR = "/home/ec2-user/mydata"         
BACKUP_DIR = "/home/ec2-user/backups"        
S3_BUCKET = "my-backup-bucket-name"         
AWS_REGION = "ap-south-1"                    
LOG_FILE = "backup_report.log"

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")
    print(message)

def create_local_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}")

    try:
        shutil.copytree(SOURCE_DIR, backup_path)
        log_message(f" Local backup created at {backup_path}")
        return backup_path
    except Exception as e:
        log_message(f" Local backup failed: {e}")
        return None

def upload_to_s3(local_path):
    s3_client = boto3.client("s3", region_name=AWS_REGION)
    try:
        for root, _, files in os.walk(local_path):
            for file in files:
                full_path = os.path.join(root, file)
                s3_key = os.path.relpath(full_path, BACKUP_DIR)
                s3_client.upload_file(full_path, S3_BUCKET, s3_key)
                log_message(f" Uploaded {file} → s3://{S3_BUCKET}/{s3_key}")
        log_message(" All files uploaded successfully to S3.")
    except (NoCredentialsError, ClientError) as e:
        log_message(f" S3 Upload failed: {e}")

def main():
    log_message(" Starting Backup Process ")
    local_backup = create_local_backup()
    if local_backup:
        upload_to_s3(local_backup)
    log_message(" Backup Process Complete \n")

if __name__ == "__main__":
    main()
