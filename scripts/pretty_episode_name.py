#    .o88b.   .d8888.   d888888b 
#   d8P  Y8   88'  YP     `88'   
#   8P        `8bo.        88    
#   8b          `Y8b.      88    
#   Y8b  d8   db   8D     .88.   
#    `Y88P'   `8888Y'   Y888888P 

# Author - https://github.com/akigugale

import os
import re
import time

#getting path of directory containing files to rename
path = input('Enter path of folder : ')
os.chdir(path)

print("*** FILES IN DIRECTORY ARE *** \n\n")
time.sleep(2)
for i in os.listdir():
	print(i)


ftype = input('\n\nEnter extension of file type: ')
l = [] #list with all files to rename
lnew = [] #list with all new names
name_part1 = input('Enter prefix of new name : ')


for x in os.listdir():
	if os.path.splitext(x)[-1] == ftype: #only for files of specific type
		l.append(x)

for i in l:
	name_part2 = re.findall("S..E..", i) #get season and ep name from orignal name for name suffix
	new_name = name_part1 + ' - ' + name_part2[0] + ftype
	lnew.append(new_name)

print("\n\n*** List of NEW names *** \n")
time.sleep(2)
for j in range(len(l)):
	print(l[j], '--->', lnew[j])

#renaming
confirmation = input("\n\nDo you wish to Rename the files [Yes/No] [Y/N] :: ")
if confirmation in ['Yes','Y','y','yes'] :
	print('\nrenaming..')
	for k in range(len(l)):
		os.rename(l[k], lnew[k])


print("\nTHANK YOU :)\n")
