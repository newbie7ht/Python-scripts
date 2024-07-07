#!/bin/bash

LOG_FILE="/path/to/your/logfile.log"
ALERT_EMAIL="your.email@example.com"

# Function to send an alert email
send_alert() {
    local error_message=$1
    echo "Subject: Error Detected in Log File" | sendmail -v $ALERT_EMAIL
    echo "Error detected: $error_message" | sendmail -v $ALERT_EMAIL
}

# Start tailing the log file
tail -F $LOG_FILE | while read line; do
    # Check if the line contains the word "ERROR"
    if echo "$line" | grep -q "ERROR"; then
        send_alert "$line"
    fi
done

