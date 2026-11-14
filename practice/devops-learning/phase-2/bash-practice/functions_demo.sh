#!/bin/bash

check_status() {
	service_name="$1"
	status="$2"
	if [ "$status" = "running" ]; then
		echo "$service_name is healthy"
	else 
		echo "$service_name is DOWN"
	fi
}

check_status "nginx" "running"
check_status "postgres" "stopped"


for service in nginx postgres redis; do
	check_status "$service" "running"
done

count=1
while [ "$count" -le 3 ]; do
	echo "Attempt $count"
	count=$((count + 1))
done
