from openwa import WhatsAPIDriver

# Create a WhatsAPIDriver object
driver = WhatsAPIDriver()

# Wait for the user to scan the QR code
input('Scan the QR code and press Enter to continue: ')

# Find the contact you want to send the message to
contact_name = 'Joe'
contact = driver.get_chat_from_phone_number(contact_name)

# Send the message
message = 'Hello, this message was sent using wa-automate-python!'
contact.send_message(message)

# Close the browser window
driver.quit()
