import time
import os

from appium import webdriver

caps = {

  "lt:options": {
    "w3c": True,
    "deviceName": "iPhone 14 Plus",
    "platformName": "ios",
    "platformVersion": "16",
    "isRealMobile": True,
    "app": "lt://APP1016043281709659296280310",  # Replace this with the APP ID of your uploaded app
    "build": "Example Test ",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True,
  }

}
username = os.getenv("LT_USERNAME")
password = os.getenv("LT_ACCESS_KEY")


gridUrl = "mobile-hub.lambdatest.com/wd/hub"

url = "https://"+username+":"+password+"@"+gridUrl
driver = webdriver.Remote(desired_capabilities = caps, command_executor = url)
print("driver created")
driver.execute_script("lambda-status=passed")
time.sleep(17)
driver.quit()