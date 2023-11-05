#!/usr/bin/python

import pexpect

PROMPT = ['# ', '>>>', '> ', '\$ ']


def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print (child.before)


def connect(user, host, password):
	ssh_newkey = 'Are u sure you want to contineu connecting!'
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
	host = '192.168.1.7'
	user = 'msfadmin'
	password = 'msfadmin'
	child = connect(user,host,password)
	#permission denied
	#send_command(child, 'cat /etc/shadow | grep root;ps')
	send_command(child, 'ls;ps')


main()
