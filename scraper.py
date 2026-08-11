import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("https://www.meetup.com/find/?location=Chennai")

time.sleep(10)

cards = driver.find_elements(By.CSS_SELECTOR, 'a[data-event-label="Event Card"]')

meetups = []

for card in cards:

    try:

        title = card.find_element(By.TAG_NAME, "h3").text.strip()

        if not title:
            continue

        # Ignore unwanted titles
        if title.lower() in ["waitlist", "9 seats left"]:
            continue

        # Date
        try:
            date = card.find_element(By.TAG_NAME, "time").text.strip()
        except:
            date = ""

        # Host
        host = ""

        divs = card.find_elements(By.TAG_NAME, "div")

        for d in divs:

            txt = d.text.strip()

            if txt.startswith("by "):
                host = txt.replace("by ", "")
                break

        source = card.get_attribute("href")

        meetups.append([
            title,
            host,
            "Chennai",
            date,
            source
        ])

    except:
        pass

driver.quit()

# Remove duplicates
unique = []
seen = set()

for row in meetups:

    if tuple(row) not in seen:
        seen.add(tuple(row))
        unique.append(row)

with open(
    "meetups.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Title",
        "Host",
        "Venue",
        "Date",
        "Source Link"
    ])

    writer.writerows(unique)

print("Meetups:", len(unique))