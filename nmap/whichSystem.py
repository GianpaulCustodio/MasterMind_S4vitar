#!/bin/python3
#coding: utf-8

import re, sys, subprocess

if len(sys.argv) != 2:
	print("\n[!] Modo de uso: python3 " + sys.argv[0] + " <ip address>\n")
	sys.exit(1)

def get_ttl(ip_address):
	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
	(out,err) = proc.communicate()
	print(out)

if __name__ == '__main__':
	ip_address = sys.argv[1]
	get_ttl(ip_address)
