import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(creds)

sheet = client.open("Chennai Meetups").sheet1

sheet.clear()

with open("meetups.csv", newline="", encoding="utf-8") as file:

    reader = csv.reader(file)

    for row in reader:
        sheet.append_row(row)

print("Google Sheet Updated Successfully!")