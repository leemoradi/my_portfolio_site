#!/usr/bin/env python3
"""
Main runner script for the legislation tracker
Consolidates all functionality into one simple interface
"""

import sys
import subprocess
import os

def show_menu():
    """Display the main menu"""
    print("\n🏛️  Congressional Legislation Tracker")
    print("=" * 40)
    print("1. 📊 Fetch Bills & Committees (Full Update)")
    print("2. 📋 Fetch Bills Only")
    print("3. 🏛️  Generate Committee Data")
    print("4. 🔄 Start Live Updates")
    print("5. 📅 Start Monthly Scheduler")
    print("6. 🧪 Generate Test Data")
    print("7. 📖 View README")
    print("8. 🚪 Exit")
    print("=" * 40)

def run_command(command, description):
    """Run a command with error handling"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ Command not found: {command}")
        return False

def main():
    """Main menu loop"""
    while True:
        show_menu()
        
        try:
            choice = input("\nSelect an option (1-8): ").strip()
            
            if choice == "1":
                # Full update
                run_command("python combined_data_fetch.py", "Full data update")
                
            elif choice == "2":
                # Bills only
                run_command("python main_fast.py", "Bill data fetch")
                
            elif choice == "3":
                # Committee data
                run_command("python realistic_committee_data.py", "Committee data generation")
                
            elif choice == "4":
                # Live updates
                print("\n🔄 Starting live updates...")
                print("📊 Dashboard will be available at: http://localhost:8000")
                print("⏰ Updates every 30 seconds (press Ctrl+C to stop)")
                run_command("python live_update.py", "Live updates")
                
            elif choice == "5":
                # Monthly scheduler
                print("\n📅 Starting monthly scheduler...")
                print("⏰ Will automatically reset data on the 1st of every month")
                print("💡 Press Ctrl+C to stop")
                run_command("python monthly_reset.py", "Monthly scheduler")
                
            elif choice == "6":
                # Test data
                run_command("python main_fast.py", "Test data generation")
                
            elif choice == "7":
                # View README
                if os.path.exists("README.md"):
                    with open("README.md", "r") as f:
                        print("\n" + f.read())
                else:
                    print("❌ README.md not found")
                    
            elif choice == "8":
                print("\n👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid option. Please select 1-8.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 