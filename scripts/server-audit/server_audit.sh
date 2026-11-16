#!/usr/bin/env bash


set -euo pipefail


hostname=$(hostname)
current_time=$(date '+%Y-%m-%d %H:%M:%S')
uptime_info=$(uptime -p)
disk_threshold=80
warning_count=0


echo "==Server audit =="
echo "Hostname: $hostname"
echo "Time: $current_time"
echo "Uptime: $uptime_info"


disk_info=$(df -h /)

echo 
echo "== Disk space =="
echo "$disk_info"


disk_used=$(df -P / | awk 'NR==2 {gsub("%", "", $5); print $5}')

if (( disk_used >= disk_threshold )); then
    echo "WARNING: disk usage is ${disk_used}%"
    warning_count=$((warning_count + 1))
else
    echo "Disk usage is ${disk_used}% — OK"
fi


memory_info=$(free -h)

echo
echo "== Memory =="
echo "$memory_info"


cpu_cores=$(nproc)
read -r load_1 load_5 load_15 _ < /proc/loadavg

echo
echo "== CPU load =="
echo "Logical CPU cores: $cpu_cores"
echo "Load average (1, 5, 15 min): $load_1, $load_5, $load_15"


services=(ssh cron)

echo
echo "== Services =="

for service_name in "${services[@]}"; do
    service_status=$(systemctl is-active "$service_name" 2>/dev/null || true)

    if [[ "$service_status" == "active" ]]; then
        printf '%-20s %s\n' "$service_name" "$service_status"
    else
        printf 'WARNING: %-12s %s\n' "$service_name" "${service_status:-unknown}"
    fi
done


echo

if (( warning_count == 0 )); then
    echo
    echo "Audit result: OK (no warnings)"
    exit 0
else
    echo
    echo "Audit result: WARNING ($warning_count issue(s))"
    exit 1
fi