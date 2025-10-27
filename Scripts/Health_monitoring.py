#!/usr/bin/env python3
import psutil
import datetime

CPU_THRESHOLD = 80       
MEM_THRESHOLD = 80       
DISK_THRESHOLD = 80      

LOG_FILE = "system_health.log"

def log_message(message):
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    log_message(f"CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk: {disk_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        log_message(f" High CPU usage detected: {cpu_usage}%")
    if memory_usage > MEM_THRESHOLD:
        log_message(f" High Memory usage detected: {memory_usage}%")
    if disk_usage > DISK_THRESHOLD:
        log_message(f" Disk usage critical: {disk_usage}%")

def list_top_processes(limit=5):
    log_message("\nTop running processes:")
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']),
                       key=lambda p: p.info['cpu_percent'],
                       reverse=True)
    for proc in processes[:limit]:
        log_message(f"PID {proc.info['pid']} | {proc.info['name']} | CPU: {proc.info['cpu_percent']}%")

if __name__ == "__main__":
    log_message(" System Health Check Started ")
    check_system_health()
    list_top_processes()
    log_message(" System Health Check Complete \n")
