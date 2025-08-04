import requests
import os
import json
from datetime import datetime, timedelta, timezone
from config import API_KEY

# -----------------------------
# Config
# -----------------------------

BASE_URL = "https://api.congress.gov/v3"
DATA_DIR = "data"
SAVE_PATH = os.path.join(DATA_DIR, "latest_bills.json")

# -----------------------------
# Test Data Generation
# -----------------------------

def generate_test_data():
    """Generate test data when API calls fail or for development"""
    print("🧪 Generating test data for development...")
    
    test_bills = [
        {
            "number": "901",
            "title": "LIONs Act of 2025",
            "congress": "119",
            "chamber": "House",
            "latestAction": {"text": "Introduced in House", "actionDate": "2025-07-29"}
        },
        {
            "number": "349", 
            "title": "A resolution designating the week of August 3 through August 9, 2025, as 'National Health Center Week'",
            "congress": "119",
            "chamber": "House",
            "latestAction": {"text": "Introduced in House", "actionDate": "2025-07-30"}
        },
        {
            "number": "4016",
            "title": "Department of Defense Appropriations Act, 2026",
            "congress": "119", 
            "chamber": "House",
            "latestAction": {"text": "Introduced in House", "actionDate": "2025-07-28"}
        },
        {
            "number": "S. 2501",
            "title": "Climate Action Now Act",
            "congress": "119",
            "chamber": "Senate", 
            "latestAction": {"text": "Introduced in Senate", "actionDate": "2025-07-29"}
        },
        {
            "number": "S. 2502",
            "title": "Education for All Act",
            "congress": "119",
            "chamber": "Senate",
            "latestAction": {"text": "Introduced in Senate", "actionDate": "2025-07-30"}
        }
    ]
    
    # Calculate date range
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    
    data = {
        "total_bills": len(test_bills),
        "house_bills": len([b for b in test_bills if b["chamber"] == "House"]),
        "senate_bills": len([b for b in test_bills if b["chamber"] == "Senate"]),
        "date_range": {
            "from": week_ago.strftime("%Y-%m-%d"),
            "to": today.strftime("%Y-%m-%d")
        },
        "bills": test_bills
    }
    
    return data

# -----------------------------
# Optimized Bill Fetching
# -----------------------------
def get_recent_bills_fast(days=30, congress="119"):
    headers = {
        "X-API-Key": API_KEY,
        "Accept": "application/json"
    }

    all_bills = []
    chambers = ["house", "senate"]
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)

    for chamber in chambers:
        print(f"📊 Fetching bills from {chamber.title()}...")
        
        # Use larger limit and sort by latest action date
        url = f"{BASE_URL}/bill?limit=100&congress={congress}&chamber={chamber}&sort=latestAction&sortOrder=desc"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"❌ Error fetching {chamber}: {response.status_code}")
            continue

        results = response.json().get("bills", [])
        print(f"📋 Found {len(results)} total bills from {chamber.title()}")
        
        bills = []

        for bill in results:
            # Use latestAction.actionDate as primary date, fallback to introducedDate
            action_date = bill.get("latestAction", {}).get("actionDate")
            intro_date = bill.get("introducedDate")
            
            # Prefer action_date if available, otherwise use intro_date
            date_to_check = action_date or intro_date
            
            if not date_to_check:
                continue

            try:
                date_obj = datetime.strptime(date_to_check, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            except ValueError:
                continue

            if date_obj >= cutoff_date:
                bill["chamber"] = chamber.title()
                bills.append(bill)
            else:
                # Stop once we hit bills older than cutoff
                break

        print(f"✅ Found {len(bills)} recent bills from {chamber.title()}")
        all_bills.extend(bills)

    return all_bills

# -----------------------------
# Display Bills in Console
# -----------------------------

def display_bills(bills):
    print(f"\n📋 Total Bills Found: {len(bills)}")
    print("=" * 60)
    
    # Group by chamber
    house_bills = [b for b in bills if b.get("chamber") == "House"]
    senate_bills = [b for b in bills if b.get("chamber") == "Senate"]
    
    print(f"🏛️  House Bills: {len(house_bills)}")
    print(f"🏛️  Senate Bills: {len(senate_bills)}\n")
    
    for bill in bills:
        number = bill.get('number', 'N/A')
        title = bill.get('title') or bill.get('titleWithoutDiacritics') or 'No Title'
        congress = bill.get('congress', 'N/A')
        chamber = bill.get('chamber', 'Unknown')
        latest_action = bill.get('latestAction', {}).get('text', 'N/A')

        print(f"📄 {chamber} {number} | {title} ({congress}th Congress)")
        print(f"  ➤ Latest Action: {latest_action}\n")

# -----------------------------
# Save Bills to JSON File
# -----------------------------

def save_bills_to_json(bills):
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Create summary data
    summary = {
        "total_bills": len(bills),
        "house_bills": len([b for b in bills if b.get("chamber") == "House"]),
        "senate_bills": len([b for b in bills if b.get("chamber") == "Senate"]),
        "date_range": {
            "from": min([b.get("latestAction", {}).get("actionDate") or b.get("introducedDate") for b in bills if b.get("latestAction", {}).get("actionDate") or b.get("introducedDate")], default="Unknown"),
            "to": max([b.get("latestAction", {}).get("actionDate") or b.get("introducedDate") for b in bills if b.get("latestAction", {}).get("actionDate") or b.get("introducedDate")], default="Unknown")
        },
        "bills": bills
    }
    
    with open(SAVE_PATH, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"✅ Saved {len(bills)} bills to {SAVE_PATH}")

# -----------------------------
# Main Execution
# -----------------------------

def main():
    """Main function to fetch and save recent bills"""
    print("🚀 Starting Bill Fetch...")
    print("=" * 50)
    
    try:
        # Try to fetch real data
        bills = get_recent_bills_fast()
        
        if bills:
            # Display bills
            display_bills(bills)
            
            # Save bills
            save_bills_to_json(bills)
            
            print("\n✅ Bill fetch completed successfully!")
        else:
            print("⚠️  No real bills found, using test data...")
            # Use test data as fallback
            test_data = generate_test_data()
            save_bills_to_json(test_data["bills"])
            display_bills(test_data["bills"])
            print("\n✅ Test data generated and saved!")
            
    except Exception as e:
        print(f"❌ Error during bill fetch: {e}")
        print("🔄 Falling back to test data...")
        test_data = generate_test_data()
        save_bills_to_json(test_data["bills"])
        display_bills(test_data["bills"])
        print("\n✅ Test data generated and saved!")

if __name__ == "__main__":
    main() 