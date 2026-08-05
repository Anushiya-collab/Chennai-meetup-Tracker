# 📍 Chennai Meetup Tracker

A Python-based automation project that scrapes upcoming meetup events in Chennai and automatically uploads the collected data to Google Sheets.

## 📖 Overview

The Chennai Meetup Tracker helps users collect information about meetup events without manually visiting websites. It uses Selenium for web scraping, stores the extracted data in a CSV file, and uploads the results to a Google Sheet for easy access and analysis.

## ✨ Features

- 🔍 Scrapes meetup event details from the web
- 📅 Collects event names, dates, and other available information
- 📄 Saves data to a CSV file
- ☁️ Automatically uploads data to Google Sheets
- ⏰ Supports scheduled execution for regular updates

## 🛠️ Technologies Used

- Python 3
- Selenium
- Google Sheets API
- gspread
- CSV
- Git & GitHub

## 📂 Project Structure

```
Chennai-meetup-Tracker/
│
├── scraper.py          # Scrapes meetup data
├── upload.py           # Uploads CSV data to Google Sheets
├── scheduler.py        # Automates execution
├── meetups.csv         # Scraped meetup data
├── .gitignore
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Anushiya-collab/Chennai-meetup-Tracker.git
```

### 2. Navigate to the project folder

```bash
cd Chennai-meetup-Tracker
```

### 3. Install required packages

```bash
pip install selenium gspread google-auth
```

### 4. Configure Google Sheets

Create a Google Cloud Service Account and download the credentials file.

> **Note:** The `credentials.json` file is intentionally excluded from this repository for security reasons.

### 5. Run the scraper

```bash
python scraper.py
```

### 6. Upload data to Google Sheets

```bash
python upload.py
```

### 7. Run the scheduler (optional)

```bash
python scheduler.py
```

## 📊 Sample Output

The project generates:

- `meetups.csv` containing scraped meetup data.
- An automatically updated Google Sheet with the same information.

## 📸 Screenshots

You can add screenshots here later.

Example:

```
screenshots/
├── scraper_output.png
├── google_sheet.png
└── terminal_output.png
```

## 🔮 Future Enhancements

- Add a graphical dashboard
- Export data to Excel
- Email notifications for new events
- Support multiple cities
- Improve error handling and logging
- Deploy as a cloud-based application

## 👩‍💻 Author

**Anushiya D**

GitHub: https://github.com/Anushiya-collab

---

⭐ If you found this project useful, feel free to star this repository!
