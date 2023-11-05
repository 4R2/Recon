#!usr/bin/python

import ftplib

def anonlogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymus', 'anonymus')
		print ("[*] " + hostname + " FTP Anonymus login succeeded :)")
		ftp.quit()
		return True
#	except Exception,e:
	except:
		print ("[-] " + hostname + " FTP Anonymus login failed :(")



#host = raw_input("Enter IP Address: ")
host = input("Enter IP Address: ")
anonlogin(host)
