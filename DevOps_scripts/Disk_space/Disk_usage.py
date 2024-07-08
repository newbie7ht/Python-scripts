# Disk Usage Monitoring
#This script checks the disk usage and prints a warning if it exceeds a threshold.

import shutil

def check_disk_usage(threshold):
    total, used, free = shutil.disk_usage("/")
    usage_percentage = (used / total) * 100
    if usage_percentage > threshold:
        print(f"Disk usage is above {threshold}%: {usage_percentage:.2f}%")

disk_usage_threshold = 80  # 80%
check_disk_usage(disk_usage_threshold)


############################output############################
#Disk usage is above 80%: 82.50%
