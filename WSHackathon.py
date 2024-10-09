# scraping/hackathons.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

print("hello world")

# SQLAlchemy base setup
Base = declarative_base()

# class code model for database storage - this is just a mapping to my existing hackathons table
class HackathonEvent(Base):

    # name of the table basically...
    __tablename__ = 'hackathon_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)

# set up mysql db connection
DATABASE_URL = "mysql+mysqlconnector://root:(DB PASSWORD INCLUDED IN A SEPARATE FILE)@localhost:3306/hackathons"
print("Setting up database connection...")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
print("Database connection established.")

class ScrapHackathon:
    # function to web scrape and databasing
    def hackathons():
        try:
            # path to chromedriver to open chrome and scrape
            chrome_driver_path = r"C:\Users\rodri\OneDrive\Área de Trabalho\ClubWebsiteProject\chromedriver-win64\chromedriver.exe"
            # declaring a user agent for web scraping
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # run Chrome in headless mode
            chrome_options.add_argument("--log-level=3")  # suppress logging
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

            # create a service object with the path above
            service = Service(executable_path=chrome_driver_path)
            # initialize chrome driver
            print("Initializing Chrome driver...")
            driver = webdriver.Chrome(service=service, options=chrome_options)
            #URL to scrape
            print("Driver initialized, navigating to URL...")
            driver.get("https://mlh.io/seasons/2025/events")
            # timer to wait page to load, the random will create random delays from 1 to 3 seconds
            time.sleep(random.uniform(1, 3))

            # find class name to scrape data from
            # event name
            elements = driver.find_elements(By.CLASS_NAME, "event-name")
            # event date
            date = driver.find_elements(By.CLASS_NAME, "event-date")
            # event location
            locations = driver.find_elements(By.CLASS_NAME, "event-location")

            # looper to extract and print event names (limited to 10)
            for i in range(min(len(elements), len(date), 5)):
                event_name = elements[i].text
                event_date = date[i].text
                # city and state of the event
                city = locations[i].find_element(By.CSS_SELECTOR, '[itemprop="city"]').text
                state = locations[i].find_element(By.CSS_SELECTOR, '[itemprop="state"]').text
                print(f"{event_name} || {event_date} || {city}, {state}")

                # add everything to the db
                event = HackathonEvent(name=event_name, date=event_date, city=city, state=state) 
                session.add(event)

                # timer so the scraping doesnt scrape everything at the same time
                time.sleep(random.uniform(1, 5))

            # commiting the changes into the db
            session.commit()
            # exiting browser
            driver.quit()

            return "scraping ended"

        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
            return "Scraping failed!"

    hackathons()
