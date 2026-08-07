from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Meetup Chennai page
driver.get("https://www.meetup.com/find/?location=Chennai")

# Wait for page to load
time.sleep(10)

# Get all links on the page
cards = driver.find_elements(By.TAG_NAME, "a")

meetups = []

for card in cards:
    try:
        text = card.text.strip()

        if text == "":
            continue

        lines = text.split("\n")

        # Ignore small links
        if len(lines) < 2:
            continue

        # -------------------------------
        # FIX: Skip price if it appears first
        # -------------------------------
        title = lines[0].strip()

        if title.startswith("$") and len(lines) > 1:
            title = lines[1].strip()

        # Skip if title is still a price
        if title.startswith("$"):
            continue

        date = ""
        host = ""
        venue = "Chennai"

        # Try to identify date and host
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

# Remove duplicates
unique = []
seen = set()

for row in meetups:
    key = tuple(row)

    if key not in seen:
        seen.add(key)
        unique.append(row)

# Save CSV
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