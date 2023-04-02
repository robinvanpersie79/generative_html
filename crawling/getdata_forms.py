import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://freefrontend.com/css-forms/#google_vignette')


downloads = driver.find_elements(By.CLASS_NAME, 'download')

# x = str(continue_link)
# print(continue_link)

print(downloads)


links = []

for i in downloads:
    links.append(i.get_attribute('href'))


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
}


successfuls = 0
for link in links:
    try:
        foldername = link.split('/')[-1].replace('.zip', '')
        os.makedirs(foldername, exist_ok=True)
        import requests
        import zipfile
        import io

        reqq = requests.get(link, headers=headers)

        z = zipfile.ZipFile(io.BytesIO(reqq.content))
        z.extractall(foldername)
        print(link, 'created')
        successfuls += 1
    except:
        print(link, 'failed')

print(successfuls)
