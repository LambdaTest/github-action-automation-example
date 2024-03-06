import time
import os

from appium import webdriver


caps = {

  "lt:options": {
    "w3c": True,
    "platformName": "ios",
    "deviceName" : ".*",
    "isRealMobile": True,
    "app": "lt://APP1016043281709659296280310",  # Replace this with the APP ID of your uploaded app
    "build": "Example Test ",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True,
  }

}


gridUrl = "mobile-hub.lambdatest.com/wd/hub"

username = os.getenv("LT_USERNAME")
password = os.getenv("LT_ACCESS_KEY")


url = "https://"+username+":"+password+"@"+gridUrl
driver = webdriver.Remote(desired_capabilities = caps, command_executor = url)
print("driver created")
driver.execute_script("lambda-status=passed")
time.sleep(10)
driver.quit()