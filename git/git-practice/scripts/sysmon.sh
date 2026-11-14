#!/bin/bash
# sysmon.sh - appends CPU load, memory and disk usage to a log file
# Usage: ./sysmon.sh [log_file]

LOG_FILE="${1:-$HOME/sysmon.log}"

timestamp=$(date '+%Y-%m-%d %H:%M:%S')
load=$(awk '{print $1}' /proc/loadavg)
mem=$(free -m | awk '/^Mem:/ {printf "%.0f", $3/$2*100}')
disk=$(df / | awk 'NR==2 {print $5}')

echo "$timestamp load=$load mem=${mem}% disk=$disk" >> "$LOG_FILE"
