import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox

class WhatsAppSenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Sender")

        self.contact_name_label = tk.Label(root, text="Contact Name:")
        self.contact_name_label.pack()

        self.contact_name_entry = tk.Entry(root)
        self.contact_name_entry.pack()

        self.message_label = tk.Label(root, text="Message:")
        self.message_label.pack()

        self.message_entry = tk.Entry(root)
        self.message_entry.pack()

        self.send_button = tk.Button(root, text="Send Message", command=self.send_whatsapp_message)
        self.send_button.pack()

    def is_connected(self):
        try:
            requests.get('https://www.google.com/')
            return True
        except requests.ConnectionError:
            return False

    def start_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def login_whatsapp(self, driver):
        driver.get('https://web.whatsapp.com/')
        messagebox.showinfo("WhatsApp Sender", "Scan the QR code and press OK to continue")

    def find_contact(self, driver, contact_name):
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
            search_box.send_keys(contact_name)
            time.sleep(2)

            contact = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]')))
            contact.click()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.close_browser(driver)

    def send_message(self, driver, message):
        try:
            message_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')))
            message_box.send_keys(message)

            send_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
            send_button.click()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.close_browser(driver)

    def close_browser(self, driver):
        driver.quit()

    def send_whatsapp_message(self):
        contact_name = self.contact_name_entry.get()
        message = self.message_entry.get()

        if not self.is_connected():
            messagebox.showerror("Error", "No internet connection available.")
        else:
            driver = self.start_browser()
            self.login_whatsapp(driver)
            self.find_contact(driver, contact_name)
            self.send_message(driver, message)
            self.close_browser(driver)


if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppSenderGUI(root)
    root.mainloop()
