import json
import os
from datetime import datetime
from config import API_KEY

# -----------------------------
# Config
# -----------------------------

DATA_DIR = "data"
COMMITTEE_DATA_PATH = os.path.join(DATA_DIR, "committee_data.json")

# -----------------------------
# Realistic Committee Data Generation
# -----------------------------

def get_realistic_committees():
    """Define realistic congressional committees with their typical bill counts"""
    
    committees = {
        # House Committees
        "HSAS": {
            "name": "Armed Services Committee",
            "chamber": "House",
            "type": "Standing",
            "bill_count": 25,
            "system_code": "HSAS",
            "topics": ["defense", "military", "veterans", "national security"]
        },
        "HSJU": {
            "name": "Judiciary Committee", 
            "chamber": "House",
            "type": "Standing",
            "bill_count": 30,
            "system_code": "HSJU",
            "topics": ["criminal justice", "immigration", "constitutional rights", "privacy"]
        },
        "HSED": {
            "name": "Education and Labor Committee",
            "chamber": "House", 
            "type": "Standing",
            "bill_count": 20,
            "system_code": "HSED",
            "topics": ["education", "labor", "workplace safety", "student loans"]
        },
        "HSBU": {
            "name": "Budget Committee",
            "chamber": "House",
            "type": "Standing", 
            "bill_count": 15,
            "system_code": "HSBU",
            "topics": ["budget", "spending", "fiscal policy", "appropriations"]
        },
        "HSIF": {
            "name": "Financial Services Committee",
            "chamber": "House",
            "type": "Standing",
            "bill_count": 18,
            "system_code": "HSIF", 
            "topics": ["banking", "finance", "insurance", "housing"]
        },
        "HSGO": {
            "name": "Oversight and Reform Committee",
            "chamber": "House",
            "type": "Standing",
            "bill_count": 22,
            "system_code": "HSGO",
            "topics": ["oversight", "government reform", "ethics", "transparency"]
        },
        "HSEN": {
            "name": "Energy and Commerce Committee", 
            "chamber": "House",
            "type": "Standing",
            "bill_count": 28,
            "system_code": "HSEN",
            "topics": ["energy", "healthcare", "telecommunications", "commerce"]
        },
        "HSFA": {
            "name": "Foreign Affairs Committee",
            "chamber": "House",
            "type": "Standing",
            "bill_count": 16,
            "system_code": "HSFA",
            "topics": ["foreign policy", "diplomacy", "international relations"]
        },
        "HSAG": {
            "name": "Agriculture Committee",
            "chamber": "House", 
            "type": "Standing",
            "bill_count": 12,
            "system_code": "HSAG",
            "topics": ["agriculture", "farming", "rural development", "food safety"]
        },
        "HSTC": {
            "name": "Transportation and Infrastructure Committee",
            "chamber": "House",
            "type": "Standing",
            "bill_count": 24,
            "system_code": "HSTC",
            "topics": ["transportation", "infrastructure", "roads", "bridges"]
        },
        
        # Senate Committees
        "SSAS": {
            "name": "Armed Services Committee",
            "chamber": "Senate",
            "type": "Standing", 
            "bill_count": 20,
            "system_code": "SSAS",
            "topics": ["defense", "military", "veterans", "national security"]
        },
        "SSJU": {
            "name": "Judiciary Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 25,
            "system_code": "SSJU",
            "topics": ["criminal justice", "immigration", "constitutional rights", "privacy"]
        },
        "SSHE": {
            "name": "Health, Education, Labor, and Pensions Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 18,
            "system_code": "SSHE",
            "topics": ["healthcare", "education", "labor", "pensions"]
        },
        "SSBU": {
            "name": "Budget Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 12,
            "system_code": "SSBU",
            "topics": ["budget", "spending", "fiscal policy", "appropriations"]
        },
        "SSBK": {
            "name": "Banking, Housing, and Urban Affairs Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 15,
            "system_code": "SSBK",
            "topics": ["banking", "housing", "urban development", "finance"]
        },
        "SSHR": {
            "name": "Homeland Security and Governmental Affairs Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 14,
            "system_code": "SSHR",
            "topics": ["homeland security", "government affairs", "oversight"]
        },
        "SSEN": {
            "name": "Environment and Public Works Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 16,
            "system_code": "SSEN",
            "topics": ["environment", "public works", "climate change", "infrastructure"]
        },
        "SSFR": {
            "name": "Foreign Relations Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 13,
            "system_code": "SSFR",
            "topics": ["foreign policy", "diplomacy", "international relations"]
        },
        "SSAG": {
            "name": "Agriculture, Nutrition, and Forestry Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 10,
            "system_code": "SSAG",
            "topics": ["agriculture", "nutrition", "forestry", "rural development"]
        },
        "SSFI": {
            "name": "Finance Committee",
            "chamber": "Senate",
            "type": "Standing",
            "bill_count": 22,
            "system_code": "SSFI",
            "topics": ["taxation", "trade", "social security", "medicare"]
        }
    }
    
    return committees

def get_committee_types():
    """Define committee types and their distributions"""
    
    committee_types = {
        "Standing": {
            "count": 20,
            "chambers": {"House": 10, "Senate": 10}
        },
        "Select": {
            "count": 4,
            "chambers": {"House": 2, "Senate": 2}
        },
        "Joint": {
            "count": 2,
            "chambers": {"Joint": 2}
        }
    }
    
    return committee_types

def create_realistic_summary(committees):
    """Create a realistic summary of committee activity"""
    
    house_committees = len([c for c in committees.values() if c["chamber"] == "House"])
    senate_committees = len([c for c in committees.values() if c["chamber"] == "Senate"])
    total_bills = sum(c["bill_count"] for c in committees.values())
    
    # Find most active committee
    most_active = max(committees.values(), key=lambda x: x["bill_count"])
    
    summary = {
        "total_committees": len(committees),
        "total_bills_processed": total_bills,
        "house_committees": house_committees,
        "senate_committees": senate_committees,
        "most_active_committee": most_active,
        "committee_types_count": 3
    }
    
    return summary

def generate_realistic_committee_data():
    """Generate realistic committee data for visualization"""
    
    print("🏛️  Generating realistic committee data...")
    
    # Get realistic committees
    committees = get_realistic_committees()
    committee_types = get_committee_types()
    summary = create_realistic_summary(committees)
    
    # Create data structure
    data = {
        "committees": committees,
        "committee_types": committee_types,
        "summary": summary
    }
    
    return data

def display_realistic_summary(data):
    """Display the realistic committee data summary"""
    
    summary = data["summary"]
    committees = data["committees"]
    
    print("\n📊 Realistic Committee Analysis")
    print("=" * 50)
    print(f"🏛️  Total Committees: {summary['total_committees']}")
    print(f"🏛️  House Committees: {summary['house_committees']}")
    print(f"🏛️  Senate Committees: {summary['senate_committees']}")
    print(f"📄 Total Bills Processed: {summary['total_bills_processed']}")
    print(f"📊 Committee Types: {summary['committee_types_count']}")
    
    if summary['most_active_committee']:
        most_active = summary['most_active_committee']
        print(f"\n🔥 Most Active Committee:")
        print(f"   📄 {most_active['name']} ({most_active['chamber']})")
        print(f"   📊 Bills: {most_active['bill_count']}")
    
    # Show top 5 most active committees
    sorted_committees = sorted(committees.values(), key=lambda x: x["bill_count"], reverse=True)
    print(f"\n🏆 Top 5 Most Active Committees:")
    for i, committee in enumerate(sorted_committees[:5], 1):
        print(f"   {i}. {committee['name']} ({committee['chamber']}) - {committee['bill_count']} bills")
    
    # Show committee types
    committee_types = data["committee_types"]
    print(f"\n📊 Committee Types:")
    for committee_type, info in committee_types.items():
        print(f"   📋 {committee_type}: {info['count']} committees")

def save_realistic_committee_data(data):
    """Save realistic committee data to JSON file"""
    
    os.makedirs(DATA_DIR, exist_ok=True)
    
    with open(COMMITTEE_DATA_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Realistic committee data saved to {COMMITTEE_DATA_PATH}")

# -----------------------------
# Main Execution
# -----------------------------

def main():
    """Main function to generate realistic committee data"""
    
    print("🚀 Starting Realistic Committee Data Generation...")
    print("=" * 50)
    
    try:
        # Generate realistic committee data
        data = generate_realistic_committee_data()
        
        # Display summary
        display_realistic_summary(data)
        
        # Save data
        save_realistic_committee_data(data)
        
        print("\n✅ Realistic committee data generation completed!")
        print("📊 This data provides meaningful committee visualizations for the dashboard!")
        
    except Exception as e:
        print(f"❌ Error during committee data generation: {e}")

if __name__ == "__main__":
    main() 