#!/usr/bin/env python
# coding: utf-8

# In[4]:


import smtplib
#Smtp - Simple message Transfer protocol 
#protocol - set of rules which internet should obey
import getpass
#Getting the password from user
from email.mime.text import MIMEText   
#getpass is used for getting the password from the user
def send_email():
    sender_address= #Enter your Mail address in single/double quotes
    #getting password from the user
    password=getpass.getpass() 
    #Subject which is used in 
    subject='Full Stack web development'
    msg=" We are pleased to announce that we will be starting the full stack web development batch"
    #server Intialization
    server=smtplib.SMTP('smtp.gmail.com',587)
    #587- Port Number - Gmail 
    #577 -Portnumber  - Yahoo
    # Different port number different domain
    #Starting server
    server.starttls()
    #Server Login
    server.login(sender_address,password)
    # Drafting the message 
    msg=MIMEText(msg)
    #Subject of the mail 
    msg['Subject']=subject
    #from  address
    msg['From']=sender_address
    #to address
    msg['To']='mohanranjith16@gmail.com'
    #setting the high priority of the mail , Importance
    msg.set_param('importance','high value')
    # Receipient mail address
    recipient = #Enter the receipient Mail address in single/double quotes
    #sender mail parameter
    server.sendmail(sender_address,recipient,msg.as_string())
 #Calling the function1   
send_email()


# In[ ]:




