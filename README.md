# SpeedCoach → Concept2-Compatible API Integration

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Flask](https://img.shields.io/badge/Flask-API-green.svg) ![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)

This project bridges the gap between on-water rowing data and indoor ergometer analytics. It converts **NK SpeedCoach** 
telemetry data into a format identical to the **Concept2 Logbook API**, allowing on-water sessions to be visualized in 
dashboards originally built for indoor rowing (the API from Concept2.

---

## 📖 Context & Motivation

Concept2 provides a powerful ecosystem for visualizing and analyzing indoor rowing data. However, 
on-water rowers using the **NK SpeedCoach** often find their data isolated from these tools.

**The Goal:** To enable seamless integration of on-water data into Concept2-based visualization tools.

**The Origin:** This project was specifically developed to support the performance dashboard created 
by **Toni** for the **Clarkson Crew**. By mimicking the Concept2 API structure, this tool allows the 
Clarkson Crew dashboard to display performance metrics for both ergometer sessions and boat trainings 
without requiring much modification to the frontend code.


This project solves that gap by:

1.  **Importing SpeedCoach CSV/XLSX data**
2.  **Normalizing it into a MySQL database**
3.  **Serving it through a custom API**
4.  **Formatting the output so it matches Concept2's official API
    structure**

This allows external apps designed for Concept2 data to accept real
on-water rowing files with no modification.

------------------------------------------------------------------------

## 📦 Project Structure

    Final_project_IA626_Speedcoach/
    │
    ├── API.py                 # Flask API that outputs Concept2-style JSON
    ├── import_data.py         # SpeedCoach parser → database loader
    ├── upload.py              # Utility for uploading and processing data files
    ├── database_creation.sql  # Database schema definition
    ├── config_example.yml     # User configuration (API key, DB settings, etc.)
    ├── ExampleAPIOutput.json  # Sample Concept2-style API result
    ├── temp_generaldata.csv   # Intermediate processed data
    ├── temp_strokedata.csv    # Intermediate processed stroke data
    └── test_client.py         # Local testing tool for API endpoints

------------------------------------------------------------------------

## ⚙️ How It Works

### **1. Import Data**

SpeedCoach files (`.csv`) are parsed by `import_data.py`.

The script extracts: 
- workout session metadata\
- split data\
- stroke-level telemetry (pace, rate, distance, HR, etc.)

The data is inserted into a structured MySQL database using the schema
in `database_creation.sql`.

------------------------------------------------------------------------

### **2. Serve the Data via API**

`API.py` exposes endpoints such as:

    /api/workouts
    /api/workouts/<id>

These endpoints output JSON formatted the same way Concept2 formats erg
data, for seamless integration.

Example fields:

``` json
{
  "id": 123,
  "date": "2025-09-20T16:03:00Z",
  "distance": 5678,
  "workout": [...],
  "strokes": [...]
}
```

------------------------------------------------------------------------

## 🛠️ Configuration

Edit `config.yml`:

``` yaml
db:
  user: 'username'
  pw: 'userPW'
  host: 'host_URL'
  db: 'data_base'
poll_user: 'user'

BASE_URL: "http://0.0.0.0:0000"
API_KEY: "0000"
```

A template is provided in `config_example.yml`.

------------------------------------------------------------------------

## ▶️ Running the Project

### **1. Install Requirements**

    pip install flask pymysql pyyaml pandas openpyxl

### **2. Create the database**

    mysql < database_creation.sql

### **3. Import SpeedCoach data**

    python import_data.py

### **4. Start the API server**

    python API.py

------------------------------------------------------------------------

## 📊 Output Example

See `ExampleAPIOutput.json` see the output of the API.

------------------------------------------------------------------------

## 🧩 Integration With External Projects

Any app that currently consumes Concept2's Logbook API can now directly
consume:

    GET /api/workouts
    GET /api/workouts/<workout_id>

This makes it ideal for: - custom visualizations\
- training dashboards\
- performance analytics\
- rowing team monitoring tools

------------------------------------------------------------------------

## 🤝 Future Improvements


