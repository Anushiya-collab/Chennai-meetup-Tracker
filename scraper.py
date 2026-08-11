from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

# ----------------------------
# Chrome Options
# ----------------------------
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ----------------------------
# Open Meetup Chennai Page
# ----------------------------
driver.get("https://www.meetup.com/find/?location=Chennai")

time.sleep(10)

# ----------------------------
# Get all links
# ----------------------------
cards = driver.find_elements(By.TAG_NAME, "a")

meetups = []

for card in cards:

    try:
        text = card.text.strip()

        if text == "":
            continue

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        if len(lines) < 2:
            continue

        # ----------------------------
        # Find Title
        # ----------------------------
        title = ""

        for line in lines:

            lower = line.lower()

            # Skip prices
            if line.startswith("$"):
                continue

            # Skip host line
            if lower.startswith("by"):
                continue

            # Skip unwanted text
            if "member" in lower:
                continue

            if "attendee" in lower:
                continue

            if "seat" in lower:
                continue

            if lower == "waitlist":
                continue

            if lower == "join":
                continue

            if "rsvp" in lower:
                continue

            title = line
            break

        if title == "":
            continue

        # ----------------------------
        # Find Host & Date
        # ----------------------------
        host = ""
        date = ""
        venue = "Chennai"

        for line in lines:

            lower = line.lower()

            if lower.startswith("by"):
                host = line.replace("by", "").strip()

            elif any(month in lower for month in [
                "jan","feb","mar","apr","may","jun",
                "jul","aug","sep","oct","nov","dec"
            ]):
                date = line

        source = card.get_attribute("href")

        # Skip empty links
        if source is None:
            continue

        meetups.append([
            title,
            host,
            venue,
            date,
            source
        ])

    except Exception:
        pass

driver.quit()

# ----------------------------
# Remove Duplicates
# ----------------------------
unique = []
seen = set()

for row in meetups:

    key = tuple(row)

    if key not in seen:
        seen.add(key)
        unique.append(row)

# ----------------------------
# Save CSV
# ----------------------------
with open("meetups.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Title",
        "Host",
        "Venue",
        "Date",
        "Source Link"
    ])

    writer.writerows(unique)

print("===================================")
print("Meetups collected successfully!")
print("Saved as meetups.csv")
print("Total Meetups:", len(unique))
print("===================================")