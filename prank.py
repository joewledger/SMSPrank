#Epic Prank
import smtplib
import os
import argparse
import platform
import sys
#Crontab for Unix based systems
import crontab

parser = argparse.ArgumentParser(description='Credentials and facts reciever information')
parser.add_argument("username")
parser.add_argument("password")
parser.add_argument("from_address")
parser.add_argument("to_address")
parser.add_argument("reciever_name")
args = parser.parse_args()

op_system = platform.system()
#Windows Task Scheduler
if(op_system == "Windows"):
	#check if task has been scheduled, if not schedule it
	if(os.system("schtasks /QUERY /TN Prank") != 0):
		py_exe = "C:\Python" + sys.version[0:3].replace(".","") + "\python.exe"
		py_file = os.path.realpath(__file__)
		os.system('schtasks /Create /SC HOURLY /TN Prank /TR "%s %s" %s %s %s %s %s' 
			% (py_exe,py_file, args.username,args.password,args.from_address,arg.to_address,args.reciever_name))
else:
	#Crontab for Unix based systems 
	if(op_system == "Linux" or op_system == "Darwin"):
		print('UNIX')
		#check if task has been scheduled, if not schedule it
	else: 
		print("Only Windows, Mac, and Linux are supported")

messageNum = 0
messages = []
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open('prank.txt',"r+") as f:
	messages = f.readlines()
	messageNum = int(messages[0])
	messages[0] = str(messageNum + 1) + '\n'
	f.seek(0)
	f.writelines(messages)
	f.truncate()

# Credentials (if needed)  
username = args.username
password = args.password

# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)
fromaddr = args.from_address 
toaddrs = args.to_address

msg = messages[messageNum].replace("{name}", args.reciever_name)
server.sendmail(fromaddr,toaddrs,msg)
server.quit()