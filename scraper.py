# Importing the libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


import time
import json

from urllib.parse import urlencode

# Setting Chrome to Headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


# API Key
# API_KEY = "50b8f3f5aa496da275bd7c3cd12acae4"
API_KEY = 'ec1607a437b99410026bbe9523f15ad4'


# Function for rotating Pxoxy with URL
def get_scraperapi_url(url):
    """
        Converts url into API request for ScraperAPI.
    """
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


# Setting Options for Driver
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
#driver = webdriver.Chrome(options=chrome_options)

# Scraping per ID inputs
phone_complete = []
email_complete = []
id_complete = []


start_id = int(input("Please enter the Beginning ID number and press 'Enter': "))
end_id = int(input("Please enter the Ending ID number and press 'Enter': "))

start_time = time.time()

for id_no in range(start_id, (end_id+1)):
#for id_no in range(124339, 124340):
#for id_no in range(1, 2):

    id_complete.append(id_no)
    driver.get(get_scraperapi_url(f"https://apps.calbar.ca.gov/attorney/Licensee/Detail/{id_no}"))
    time.sleep(1)

    try:
        phone_selector = '.nostyle+ p'
        phone = driver.find_element(By.CSS_SELECTOR, phone_selector)

        lawyer_phone = phone.text.split("|")[0].split(":")[1].strip()
        time.sleep(2)
        phone_complete.append(lawyer_phone)
    except NoSuchElementException:
        phone_complete.append("NaN")
    #except TimeoutException:
        #phone_complete.append("NaN")

    email_list = []
    #try:
        #for i in range(19):
            #if driver.find_element(By.ID, f'e{i}').text.strip():
                #email_list.append(driver.find_element(By.ID, f'e{i}').text.strip())
        #time.sleep(3)
        #email_complete.append(email_list)

    try:
        email_list = [driver.find_element(By.ID, f'e{i}').text.strip() for i in range(19) if driver.find_element(By.ID, f'e{i}').text.strip() ]
        email_complete.append(email_list)
    except NoSuchElementException:
        email_complete.append("NaN")

    print(f"Successfully scraped {id_no}....")
    time.sleep(1)

lawyer_dict = {
    "ID": id_complete,
    "Phone": phone_complete,
    "Email": email_complete
}

with open(f"{str(id_complete[0])}___{str(id_complete[-1])}.json", "w") as outfile:
    json.dump(lawyer_dict, outfile)

# print(lawyer_dict)

driver.quit()

duration = round(time.time() - start_time)

#print(f"Total Time Taken: {duration} Secs")
#print(f" Number of Pages: {len(id_complete)} Pages")
#print(f" Time per Page is: {duration/len(id_complete)} Secs")

print(f"The file '{start_id}__{end_id}.json' has been successfully created."
      f"You can copy the scraped file")
