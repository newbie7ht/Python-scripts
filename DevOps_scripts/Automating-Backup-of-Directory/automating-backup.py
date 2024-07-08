#Automating Backup
#This script automates the backup of a directory, creating a timestamped copy.

import shutil
import os
from datetime import datetime

def backup_directory(src_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    shutil.copytree(src_dir, backup_path)
    print(f"Backup completed: {backup_path}")

source_directory = "/path/to/source"
backup_directory = "/path/to/backup"
backup_directory(source_directory, backup_directory)


########################output######################################
#Backup completed: /path/to/backup/backup_20240701120000
