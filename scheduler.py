import schedule
import time
import subprocess

def job():
    print("Running Meetup Tracker...")

    subprocess.run(["python", "scraper.py"])
    subprocess.run(["python", "upload.py"])

    print("Google Sheet Updated!")

# Run every 1 hour
schedule.every(1).hours.do(job)

# Run once immediately
job()

while True:
    schedule.run_pending()
    time.sleep(10)