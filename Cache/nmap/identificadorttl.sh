#!/bin/bash
#./scriptbtgp.sh <ip_address>
#Falta añadirle un menú
ip_address=$1
ping -c 1 $ip_address > hola.txt
a=$(cat hola.txt | head -2 | tail -1 | awk '{print $6}' | tr 'ttl=' ' ' | tr -d "    ")
if [ $a == "64" ] || [$a == "63" ]; then
	echo "Linux"
elif [ $a == "128" ] || [ $a == "127" ]; then
	echo "Windows"
else
	echo "F"
fi
rm hola.txt
