#!/bin/bash
#Made by HackeMate

ip=$1
if [ $ip ]; then
	for i in {0..65535}
        	do
                	echo "" > /dev/tcp/$ip/$i && echo "[*] Port ${i}: Open"
        	done 2>/dev/null
else
	echo "./nmapbyme.sh <ip_address>"
fi
