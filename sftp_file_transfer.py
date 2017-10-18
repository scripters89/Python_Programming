# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:10:29 2017

@author: mashiksa
"""
Paramiko Documents : https://github.com/paramiko/paramiko
	
import paramiko 
hostname = 'xxxx.com'
username = 'xxxxx'
password = 'xxxxx'
port = 22

# Both Source/Destination path should include File Name 
source_path = 'C:/dkdk/kdkd.txt'
destination_path = '/home/test/kdkd.txt'

#Creating SSH Client
ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname = hostname, port = port, username = username, password = password)

#Connecting using private keyfile
#pkey = '/keyfile/location/filename'
#p_key_file = paramiko.RSAKey.from_private_key_file(pkey, password = passphrase)
#ssh = paramiko.SSHClient()
#ssh.connect(hostname = hostname, port = portno, pkey = p_key_file)

#Creating sftp session thru ssh
sftp = ssh2.open_sftp()
sftp.put(localpath = soruce_path,remotepath = destination_path, confirm = True)

#Closing Connection.
ssh2.close()