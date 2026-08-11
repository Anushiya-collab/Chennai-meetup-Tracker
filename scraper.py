from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

# -----------------------------
# Chrome Options
# -----------------------------
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

driver.get("https://www.meetup.com/find/?location=Chennai")
time.sleep(10)

cards = driver.find_elements(By.TAG_NAME, "a")

meetups = []
seen = set()

# Words we don't want as titles
bad_words = [
    "waitlist",
    "join",
    "seat",
    "member",
    "attendee",
    "more to explore",
    "featured",
    "sign in",
    "log in",
    "see all",
    "create",
    "organize",
    "start a group"
]

# Cities we don't want
bad_locations = [
    "seattle",
    "vancouver",
    "bay area",
    "san francisco",
    "new york",
    "los angeles",
    "london",
    "toronto",
    "portland",
    "marysville"
]

for card in cards:

    try:

        text = card.text.strip()

        if not text:
            continue

        lines = [i.strip() for i in text.split("\n") if i.strip()]

        if len(lines) < 2:
            continue

        title = ""

        for line in lines:

            lower = line.lower()

            if line.startswith("$"):
                continue

            if lower.startswith("by"):
                continue

            if any(word in lower for word in bad_words):
                continue

            title = line
            break

        if title == "":
            continue

        # Skip unwanted locations
        if any(city in title.lower() for city in bad_locations):
            continue

        host = ""
        date = ""

        for line in lines:

            lower = line.lower()

            if lower.startswith("by"):
                host = line.replace("by", "").strip()

            if any(month in lower for month in [
                "jan","feb","mar","apr","may","jun",
                "jul","aug","sep","oct","nov","dec"
            ]):
                date = line

        source = card.get_attribute("href")

        if not source:
            continue

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

    except:
        pass

driver.quit()

with open("meetups.csv","w",newline="",encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Title",
        "Host",
        "Venue",
        "Date",
        "Source Link"
    ])

    writer.writerows(meetups)

print("Meetups collected:",len(meetups))