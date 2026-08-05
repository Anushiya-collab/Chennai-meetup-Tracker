import subprocess

print("Starting Meetup Tracker...")

subprocess.run(["python", "scraper.py"])
subprocess.run(["python", "upload.py"])

print("Google Sheet Updated Successfully!")