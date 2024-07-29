from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = 'AC47cb80f791abc0cea3e9de217b21f796'
auth_token = 'af556a28d7552686813c21a969e77d82'

# Create a Twilio client
client = Client(account_sid, auth_token)

# List of recipients and their phone numbers
recipients = [
    {'name': 'Recipient 1', 'phone': '7200511101'},
    # Add more recipients as needed
]

# Message to be sent
message_body = "Hello, this is your SMS message."

# Loop through recipients and send SMS
for recipient in recipients:
    message = client.messages.create(
        body=f"Hi {recipient['name']}, {message_body}",
        from_='your_twilio_phone_number',
        to=recipient['phone']
    )

    print(f"Message sent to {recipient['name']}, SID: {message.sid}")
