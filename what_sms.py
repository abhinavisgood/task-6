#install pywhatkit
import pywhatkit
from twilio.rest import Client as cl
print("Enter Twilio account credentials and whatsapp credentials for sending sms and whatsapp")
x = input("Enter Twilio Account SID")
y = input("Enter Twilio Account Auth Token")
client = cl (x,y)
recv_mob=input("Enter reciever mob number")
recv_what=input("Enter reciever whatsapp number")
num_pur=input("Enter purchased twilio number")
def send_what_sms():
    # Use 'sendwhatmsg()' function to send message
    pywhatkit.sendwhatmsg(recv_what, "Face found",Hour ,Minute )
    
    # To Confirm Message Send or Not
    print ("Message Sent...")
    
    
    # Sending SMS
    SMS = client.messages.create( from_ = num_pur , to = recv_mob , body = "Your face was detected!!" )
    
    # To Confirm SMS Send or Not
    print ("SMS Sent...")