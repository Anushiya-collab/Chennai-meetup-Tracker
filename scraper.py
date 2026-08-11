import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# -----------------------------
# Chrome Options
# -----------------------------
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

# -----------------------------
# Open Meetup Chennai page
# -----------------------------
driver.get("https://www.meetup.com/find/?location=Chennai")

time.sleep(10)

# -----------------------------
# Get only event cards
# -----------------------------
cards = driver.find_elements(By.CSS_SELECTOR, 'a[data-event-label="Event Card"]')

meetups = []
seen = set()

for card in cards:

    try:
        # -----------------------------
        # Title
        # -----------------------------
        title = card.find_element(By.TAG_NAME, "h3").text.strip()

        if not title:
            continue

        # -----------------------------
        # Date
        # -----------------------------
        try:
            date = card.find_element(By.TAG_NAME, "time").text.strip()
        except:
            date = ""

        # -----------------------------
        # Host
        # -----------------------------
        host = ""

        divs = card.find_elements(By.TAG_NAME, "div")

        for d in divs:

            txt = d.text.strip()

            if txt.startswith("by "):

                host = txt.replace("by ", "")

                # Remove line breaks
                host = host.replace("\n", " ")

                # Remove ratings like 4.6 or 3.7
                words = host.split()

                cleaned = []

                for word in words:
                    try:
                        float(word)
                    except ValueError:
                        cleaned.append(word)

                host = " ".join(cleaned)

                break

        # -----------------------------
        # Source Link
        # -----------------------------
        source = card.get_attribute("href")

        row = (
            title,
            host,
            "Chennai",
            date,
            source
        )

        if row not in seen:
            seen.add(row)
            meetups.append(row)

    except Exception:
        pass

driver.quit()

# -----------------------------
# Save CSV
# -----------------------------
with open("meetups.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Title",
        "Host",
        "Venue",
        "Date",
        "Source Link"
    ])

    writer.writerows(meetups)

print("=" * 40)
print("Meetups collected successfully!")
print("Total Meetups:", len(meetups))
print("Saved to meetups.csv")
print("=" * 40)