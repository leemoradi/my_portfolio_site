import schedule
import time
import subprocess
import os
from datetime import datetime, timedelta
import json

def daily_update():
    """Daily data update - fetches fresh congressional data"""
    print(f"\n🕐 {datetime.now().strftime('%H:%M:%S')} - Daily Update")
    print("📊 Fetching fresh congressional data...")
    
    try:
        # Run the combined data collection script
        result = subprocess.run(['python', 'combined_data_fetch.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Daily update completed!")
        else:
            print(f"❌ Daily update failed: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Error during daily update: {e}")

def monthly_data_reset():
    """Monthly data reset - comprehensive refresh on the 1st of each month"""
    # Only run on the first of the month
    if datetime.now().day != 1:
        return
    
    print(f"\n🔄 Monthly Data Reset - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("📊 Comprehensive data refresh for the new month...")
    
    try:
        # Run the combined data collection script
        result = subprocess.run(['python', 'combined_data_fetch.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Monthly reset completed successfully!")
            
            # Show summary of new data
            try:
                # Bill data summary
                with open('data/latest_bills.json', 'r') as f:
                    bill_data = json.load(f)
                    print(f"📋 Total Bills: {bill_data.get('total_bills', 0)}")
                    print(f"🏛️  House Bills: {bill_data.get('house_bills', 0)}")
                    print(f"🏛️  Senate Bills: {bill_data.get('senate_bills', 0)}")
                    print(f"📅 Date Range: {bill_data.get('date_range', {}).get('from', 'Unknown')} to {bill_data.get('date_range', {}).get('to', 'Unknown')}")
                
                # Committee data summary
                with open('data/committee_data.json', 'r') as f:
                    committee_data = json.load(f)
                    summary = committee_data.get('summary', {})
                    print(f"📋 Total Committees: {summary.get('total_committees', 0)}")
                    print(f"🏛️  House Committees: {summary.get('house_committees', 0)}")
                    print(f"🏛️  Senate Committees: {summary.get('senate_committees', 0)}")
                    
            except Exception as e:
                print(f"⚠️  Could not read updated data: {e}")
        else:
            print(f"❌ Monthly reset failed: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Error during monthly reset: {e}")

def setup_schedule():
    """Set up the schedule for daily updates and monthly resets"""
    print("📅 Setting up smart scheduler...")
    
    # Daily updates at 9:00 AM, 3:00 PM, and 9:00 PM
    schedule.every().day.at("09:00").do(daily_update)
    schedule.every().day.at("15:00").do(daily_update)
    schedule.every().day.at("21:00").do(daily_update)
    
    # Monthly reset check at 6:00 AM every day (will only run on 1st)
    schedule.every().day.at("06:00").do(monthly_data_reset)
    
    print("✅ Schedule configured:")
    print("   📅 Daily updates: 9:00 AM, 3:00 PM, 9:00 PM")
    print("   🔄 Monthly reset: 1st of every month at 6:00 AM")
    
    # Run initial update
    print("🕐 Running initial update...")
    daily_update()

def run_scheduler():
    """Run the scheduler continuously"""
    print("🚀 Starting smart scheduler...")
    print("📊 Dashboard available at: http://localhost:8000")
    print("⏰ Automatic updates running in background")
    print("💡 Press Ctrl+C to stop")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    # Set up the schedule
    setup_schedule()
    
    try:
        run_scheduler()
    except KeyboardInterrupt:
        print("\n🛑 Smart scheduler stopped.") 