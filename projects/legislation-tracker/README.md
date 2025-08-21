# Legislation Tracker

A comprehensive web application that tracks recent bills and committee activity in the U.S. Congress using the Congress.gov API.

## Quick Start

### Option 1: Interactive Menu (Recommended)
```bash
python run.py
```
This opens an interactive menu with all options.

### Option 2: Direct Commands
```bash
# Full update (bills + committees)
python combined_data_fetch.py

# Bills only
python main_fast.py

# Committee data only
python realistic_committee_data.py

# Live updates
python live_update.py

# Monthly scheduler
python monthly_reset.py
```

## 📁 Project Structure

```
legislation-tracker/
├── run.py                    # Main interactive runner
├── main_fast.py              # Bill fetching (with test data fallback)
├── realistic_committee_data.py # Committee data generation
├── combined_data_fetch.py    # Combined bill + committee fetching
├── monthly_reset.py          # Smart scheduler with daily/monthly updates
├── live_update.py            # Live data updates
├── config.py                 # API configuration
├── requirements.txt          # Python dependencies
├── data/
│   ├── latest_bills.json    # Generated bill data
│   └── committee_data.json  # Generated committee data
├── site/
│   ├── index.html           # Main dashboard
│   ├── committee_dashboard.html # Enhanced committee dashboard
│   ├── index_auto.html      # Auto-refresh dashboard
│   ├── dashboard.html       # Landing page
│   ├── server.py            # Custom server (no file listings)
│   └── script.js            # Frontend JavaScript
└── README.md                # This file
```

## Features

- **Dual Chamber Support**: Fetches bills from both House and Senate
- **Committee Analysis**: Tracks committee activity and bill processing
- **Real-time Statistics**: Displays total bill count, chamber breakdown, and committee metrics
- **Interactive Charts**: 
  - Committee activity chart (top 10 most active committees)
  - Committee types distribution (pie chart)
- **Date Range Display**: Shows the actual date range of bills being tracked
- **Modern UI**: Clean, responsive design with card-based layout
- **Automatic Scheduling**: Daily updates and monthly resets
- **Live Updates**: Real-time data refresh capabilities
- **Enhanced Dashboard**: Combined bill and committee analysis
- **Test Data Fallback**: Automatic fallback to test data when API fails

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   - Get a free API key from [Congress.gov](https://api.congress.gov/)
   - Add it to `config.py`:
     ```python
     API_KEY = "your_api_key_here"
     ```

3. **Run the Application**:
   ```bash
   python run.py
   ```

4. **View the Dashboard**:
   - Open `site/index.html` in your browser
   - Or serve it with a local server:
     ```bash
     cd site && python server.py
     ```

## Dashboard Options

- **Main Dashboard**: `http://localhost:8000` - Bill tracking and analysis
- **Committee Dashboard**: `http://localhost:8000/committee_dashboard.html` - Enhanced view with committee analysis
- **Auto-Refresh Dashboard**: `http://localhost:8000/index_auto.html` - Auto-refreshing version

## Automatic Scheduling

### Daily Updates
The system automatically updates data three times per day:
- **9:00 AM** - Morning update
- **3:00 PM** - Afternoon update  
- **9:00 PM** - Evening update

### Monthly Resets
On the **1st of every month at 6:00 AM**, the system:
- Resets data collection completely
- Fetches fresh congressional data (bills + committees)
- Provides comprehensive monthly statistics

### Running the Scheduler
```bash
python monthly_reset.py
```

This will start the smart scheduler that handles both daily updates and monthly resets automatically.

## Data Structure

### Bill Data (`data/latest_bills.json`)
```json
{
  "total_bills": 200,
  "house_bills": 100,
  "senate_bills": 100,
  "date_range": {
    "from": "2025-07-29",
    "to": "2025-07-30"
  },
  "bills": [...]
}
```

### Committee Data (`data/committee_data.json`)
```json
{
  "committees": {
    "HSAS": {
      "name": "Armed Services Committee",
      "chamber": "House",
      "type": "Standing",
      "bill_count": 25,
      "system_code": "HSAS"
    }
  },
  "committee_types": {
    "Standing": {
      "count": 20,
      "chambers": {"House": 10, "Senate": 10}
    }
  },
  "summary": {
    "total_committees": 20,
    "house_committees": 10,
    "senate_committees": 10
  }
}
```

## Recent Improvements

### ✅ Implemented
- **Interactive Runner**: New `run.py` with menu interface
- **Test Data Integration**: Automatic fallback when API fails
- **Dual Chamber Fetching**: Now pulls bills from both House and Senate
- **Committee Analysis**: New dataset tracking committee activity and bill processing
- **Enhanced Statistics**: Shows total bills, House bills, Senate bills, and committee metrics
- **Improved UI**: Modern card-based layout with better styling
- **Committee Visualizations**: Activity charts and type distribution
- **Better Data Organization**: Structured JSON with summary statistics
- **Automatic Scheduling**: Daily updates and monthly resets
- **Clean User Interface**: No file listings, direct dashboard access
- **Combined Data Fetching**: Single script for bills and committees

### Future Enhancements
- **Interactive Filtering**: Filter by time range or topic
- **Deployment**: GitHub Pages or Netlify deployment
- **Bill Details**: Click to view full bill information
- **Search Functionality**: Search bills by title or sponsor
- **Email Notifications**: Get notified of new bills
- **Historical Data**: Track bills over time
- **Committee Details**: Deep dive into specific committee activity

## API Usage

The application uses the Congress.gov API v3:
- **Bill Endpoint**: `https://api.congress.gov/v3/bill`
- **Committee Endpoint**: `https://api.congress.gov/v3/committee`
- **Parameters**: congress, chamber, limit, offset
- **Rate Limit**: 1000 requests per hour (free tier)

## Technologies Used

- **Backend**: Python, Requests library, Schedule library
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js
- **API**: Congress.gov API v3
- **Scheduling**: Python Schedule library
