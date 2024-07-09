#This script monitors a log file and prints a message when it detects an "ERROR".
import time

def tail_log(file_path):
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                # Sleep briefly if no new line is found, then continue
                time.sleep(0.1)
                continue
            if "ERROR" in line:
                # Print the error line if it contains "ERROR"
                print(f"Error detected: {line.strip()}")

# Specify the path to your log file
log_file_path = "/path/to/your/logfile.log"
# Start monitoring the log file
tail_log(log_file_path)

###################output####################
#Error detected: ERROR: Unable to connect to database
#Error detected: ERROR: Out of memory
