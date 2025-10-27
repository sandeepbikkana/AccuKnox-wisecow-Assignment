#!/usr/bin/env python3
import psutil
import datetime

# Thresholds
CPU_LIMIT = 80
MEM_LIMIT = 80
DISK_LIMIT = 80
LOG_FILE = "system_health.log"

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")
    print(message)

def main():
    log_message("=== System Health Check ===")

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_LIMIT:
        log_message(f"High CPU Usage: {cpu_usage}%")
    else:
        log_message(f"CPU Usage: {cpu_usage}%")

    # Memory Usage
    memory = psutil.virtual_memory()
    mem_usage = memory.percent
    if mem_usage > MEM_LIMIT:
        log_message(f"High Memory Usage: {mem_usage}%")
    else:
        log_message(f"Memory Usage: {mem_usage}%")

    # Disk Usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_LIMIT:
        log_message(f"Low Disk Space: {disk_usage}% used")
    else:
        log_message(f"Disk Usage: {disk_usage}% used")

    log_message("----------------------------")

if __name__ == "__main__":
    main()
