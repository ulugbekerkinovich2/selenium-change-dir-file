import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)
driver.get('chrome://settings/content/pdfDocuments')
time.sleep(5)
# driver.find_element(By.XPATH,
#                     '/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[5]/settings-privacy-page//settings-animated-pages/settings-subpage[2]/div/settings-radio-group/settings-collapse-radio-button[1]//div/div[2]/div[1]').click()
# but.click()
# driver.find_element(By.ID, 'borderWrapper').click()
driver.get('https://intranet.ytit.uz/course/view.php?id=3513')
time.sleep(1)
url_link = []
lists = []
folder_link = []
youtube_links = []
elems = driver.find_elements(By.TAG_NAME, 'a')
for i in elems:
    links = i.get_attribute('href')
    print(i.get_attribute('href'))
    print(links)
