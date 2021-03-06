#!/bin/python3
#coding: utf-8

import re, sys, subprocess, os

if len(sys.argv) != 2:
	print("\n[!] Modo de uso: python3 " + sys.argv[0] + " <ip address>\n")
	sys.exit(1)

def get_ttl(ip_address):
	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
	(out,err) = proc.communicate()
	out = out.split()
	try:
		out = out[12].decode('utf-8')
		ttl_value = re.findall(r"\d{1,3}",out)
		return ttl_value[0]
	except:
		print("Ingrese una IP valida")
		DEVNULL = open(os.devnull, 'wb')
		sys.exit(0)

def get_os(ttl):
	ttl = int(ttl)
	if ttl>=0 and ttl<=64:
		return ("Linux")
	elif ttl>=65 or ttl<=128:
		return ("Windows")
	else:
		return ("Not Found")

if __name__ == '__main__':
	ip_address = sys.argv[1]
	ttl = get_ttl(ip_address)
	os_name = get_os(ttl)
	print("%s (ttl -> %s): %s" % (ip_address,ttl,os_name))
