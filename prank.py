#Epic Prank
import smtplib

f = open('prank.txt','r')
messages = f.readlines()
messageNum = int(messages[0])

f.close()

f = open('prank.txt','w')
messages[0] = str(int(messages[0]) + 1) + '\n'
f.writelines(messages)
f.close()

# Credentials (if needed)  
username = 'galen.c.caldwell'  
password = 'galenfacts'  
  
# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)
fromaddr = 'galen.c.caldwell@gmail.com'  
toaddrs1 = 'joewledger@gmail.com'
toaddrs  = '2064995563@txt.att.net'


msg = messages[messageNum]
server.sendmail(fromaddr, toaddrs, msg)  
server.sendmail(fromaddr,toaddrs1,msg)
server.quit()  


