import schedule
import time
import os

def job():
    print("Running scraper...")
    os.system("python scraper.py")

    print("Uploading to Google Sheets...")
    os.system("python upload.py")

    print("Update completed!")

# Run every 1 hour
schedule.every(1).hours.do(job)

print("Scheduler started... Press Ctrl+C to stop.")

# Run once immediately
job()

while True:
    schedule.run_pending()
    time.sleep(10)