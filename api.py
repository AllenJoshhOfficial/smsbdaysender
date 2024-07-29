from openwa import WhatsAPIDriver


driver = WhatsAPIDriver()

input('Scan the QR code and press Enter to continue: ')


contact_name = 'Joe'
contact = driver.get_chat_from_phone_number(contact_name)


message = 'Hello, this message was sent using wa-automate-python!'
contact.send_message(message)

driver.quit()
