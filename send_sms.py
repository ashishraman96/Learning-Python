from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC78df972baae63eb22634a95070a1f90a"
# Your Auth Token from twilio.com/console
auth_token  = "8cac867322a4be6d8976dff22e13f434"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919738273353", #the number to which the message is to be sent
    from_="+14159171969", #twillio number
    body="Hello from Python!")

print(message.sid)
