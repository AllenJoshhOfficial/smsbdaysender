from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create a ChromeOptions object
chrome_options = Options()

# Add options to the ChromeOptions object
chrome_options.add_argument('--disable-extensions')

# Pass the ChromeOptions object to the Chrome driver constructor
driver = webdriver.Chrome(options=chrome_options)
