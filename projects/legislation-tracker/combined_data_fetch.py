#!/usr/bin/env python3
"""
Combined data fetching script for bills and committees
Runs both bill analysis and committee analysis in one execution
"""

import subprocess
import json
import os
from datetime import datetime

def fetch_all_data():
    """Fetch both bill and committee data"""
    print("🚀 Starting Combined Data Fetch...")
    print("=" * 50)
    
    try:
        # Fetch bill data
        print("📊 Fetching bill data...")
        bill_result = subprocess.run(['python', 'main_fast.py'], 
                                   capture_output=True, text=True)
        
        if bill_result.returncode == 0:
            print("✅ Bill data fetched successfully!")
        else:
            print(f"❌ Bill data fetch failed: {bill_result.stderr}")
        
        # Generate realistic committee data
        print("\n🏛️  Generating committee data...")
        committee_result = subprocess.run(['python', 'realistic_committee_data.py'], 
                                        capture_output=True, text=True)
        
        if committee_result.returncode == 0:
            print("✅ Committee data generated successfully!")
        else:
            print(f"❌ Committee data generation failed: {committee_result.stderr}")
        
        # Display summary
        print("\n📊 Data Summary:")
        print("-" * 30)
        
        # Check bill data
        try:
            with open('data/latest_bills.json', 'r') as f:
                bill_data = json.load(f)
                print(f"📋 Bills: {bill_data.get('total_bills', 0)} total")
                print(f"🏛️  House: {bill_data.get('house_bills', 0)} bills")
                print(f"🏛️  Senate: {bill_data.get('senate_bills', 0)} bills")
        except Exception as e:
            print(f"⚠️  Could not read bill data: {e}")
        
        # Check committee data
        try:
            with open('data/committee_data.json', 'r') as f:
                committee_data = json.load(f)
                summary = committee_data.get('summary', {})
                print(f"📋 Committees: {summary.get('total_committees', 0)} total")
                print(f"🏛️  House: {summary.get('house_committees', 0)} committees")
                print(f"🏛️  Senate: {summary.get('senate_committees', 0)} committees")
                print(f"📄 Bills Processed: {summary.get('total_bills_processed', 0)} total")
        except Exception as e:
            print(f"⚠️  Could not read committee data: {e}")
        
        print(f"\n⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("✅ Combined data fetch completed!")
        
    except Exception as e:
        print(f"❌ Error during combined data fetch: {e}")

if __name__ == "__main__":
    fetch_all_data() 