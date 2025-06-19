from os import system as sy
sy('pip install --upgrade pip')
sy('pip install selenium requests')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from requests import get
from time import sleep

url = 'https://web-49oa.onrender.com/'
while True:
  try:
      print('đang mở')
      options = Options()
      options.add_argument("--no-first-run")
      options.add_argument("--disable-extensions")
      options.add_argument("--headless=new")
      driver = webdriver.Chrome(options=options)
      print('xong')
      dl = get(url).text; driver.get(url)
      while True:
          print(driver.title); sleep(30)
          if dl != get(url).text:
              print("Page content changed, reloading...")
              dl = get(url).text; driver.get(url)
  except Exception as e:
      print(f"Error: {e}"); sleep(5)
