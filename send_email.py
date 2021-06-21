import smtplib

def send_email():
   
   message = f"""From: From Person {sender}
   To To Person {recv}
   Subject: Face Found
   this indicates that the face has been found 
   """ 
   try:
      smtpObj = smtplib.SMTP(smtpserv,port=smtpport)
      smtpObj.login(sender, password)
      smtpObj.sendmail(sender, receivers, message)         
      print("Successfully sent email")
   except SMTPException:
      print("Error: unable to send email")



print("Enter email credentials")
sender = input("Enter sender email")
recv =input("Enter reciever email")
recv = list(recv)
password = input("Enter_Your_Password_Here")
smtpport = int(input("enter smtp port"))
smtpserv =input("Enter smtp server address")

