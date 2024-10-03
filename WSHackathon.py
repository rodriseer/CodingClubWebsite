from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time

class Hackathons:
    # link (URL) to scrape
    URL = "https://mlh.io/seasons/2025/events"

    def __init__(self):
        # path to chromedriver to open chrome and scrape
        chrome_driver_path = r"C:\Users\rodri\OneDrive\Área de Trabalho\ClubWebsiteProject\chromedriver-win64\chromedriver.exe"

        # declaring a user agent for web scraping
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # run Chrome in headless mode
        chrome_options.add_argument("--log-level=3")  # suppress logging
        chrome_options.add_argument("--disable-accelerated-2d-canvas")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # create a service object with the path above
        service = Service(executable_path=chrome_driver_path)
        # initialize chrome driver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def scrape_hackathons(self):
        # open webpage
        self.driver.get(self.URL)
        # timer to wait page to load, the random will create random delays from 1 to 3 seconds
        time.sleep(random.uniform(1, 3))

        # find class name to scrape data from
        # event name
        elements = self.driver.find_elements(By.CLASS_NAME, "event-name")
        # event date
        date = self.driver.find_elements(By.CLASS_NAME, "event-date")
        # event location
        locations = self.driver.find_elements(By.CLASS_NAME, "event-location")

        # looper to extract and print event names (limited to 10)
        for i in range(min(len(elements), len(date), 10)):
            event_name = elements[i].text
            event_date = date[i].text
            # city and state of the event
            city = locations[i].find_element(By.CSS_SELECTOR, '[itemprop="city"]').text
            state = locations[i].find_element(By.CSS_SELECTOR, '[itemprop="state"]').text
            print(f"{event_name} || {event_date} || {city}, {state}")
            time.sleep(random.uniform(1, 5))

        # exiting browser
        self.driver.quit()

# create instances of classes
hackathon_scraper = Hackathons()
hackathon_scraper.scrape_hackathons()
