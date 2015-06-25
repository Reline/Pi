__author__ = 'Nathan'

import smtplib
import getpass

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)

print("Login")
username = input("Username: ")
password = input("Password: ") # password = getpass.getpass("Password: ")
server_ssl.login(username, password)
print("Login successful\n")

# get email content from user
fromaddr = input("From: ")
toaddr = input("To: ")
subject = input("Subject: ")
msg = input("Message: ")

text = "From: " + fromaddr + "\nTo: " + toaddr + "\nSubject: " + subject + "\n\n" + msg

# send email
print("Sending mail...")
server_ssl.sendmail(fromaddr, toaddr, text)
print("Send successful")
server_ssl.close()

