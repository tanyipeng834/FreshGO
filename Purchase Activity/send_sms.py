from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4c8e5c738c049c5bcc512e752ca425cb"
# Your Auth Token from twilio.com/console
auth_token  = "0de17d77804336049f9b66aef6fd685a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+6593486088", 
    from_="+15056579402",
    body="Hey, there is a delivery request available! Click the link to accept: hello.com")

print(message.sid)