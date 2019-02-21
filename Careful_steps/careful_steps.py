#!/usr/bin/python

import zipfile,rarfile
#Make sure you install those modules to python

from os import system


#Set the path of the 'archives' folder after unzipping 'f8ba...' zip file
#path = "/root/Desktop/Csa-Checkpoint/Careful_steps/archives/unzipme."

def zip_and_rar(file):
	full_path = "/root/Desktop/Csa-Checkpoint/Careful_steps/archives/unzipme."+str(file)
	if zipfile.is_zipfile(full_path):
		f.write(zipfile.ZipFile(full_path).comment+"\n")
	elif rarfile.is_rarfile(full_path):
		f.write(rarfile.RarFile(full_path).comment+"\n")


def letters_and_numbers(): 
	f = open("almost_there.txt","r")
	list = f.read().splitlines()
	f.close()
	list2 = [x for x in list if x!='']
	for i in list2:
		a = i.split(",")
		letter.append(a[0])
		num.append(a[-1])


def get_flag():
	f = open("flag.txt","a")
	count = 0
	for i in range(120):
		f.write(letter[count])
		count += int(num[count])
	f.close()


f = open("almost_there.txt","a")
for file in range(2000):
	zip_and_rar(file)
f.close()

letter = []
num = []
letters_and_numbers()
get_flag()

#Notice the new file created called 'flag.txt', if the script doesn't automatically
#print what's in the file just open the file, you will see the flag there.

system("cat /root/Desktop/Csa-Checkpoint/Careful_steps/flag.txt")
system("echo ''")

