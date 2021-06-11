#!/bin/bash

for i in {0..255};do
	timeout 1 bash -c "ping -c 1 192.168.100.$i > /dev/null 2>&1" && echo "Host: 192.168.100.${i} - ACTIVE" &
done; wait
