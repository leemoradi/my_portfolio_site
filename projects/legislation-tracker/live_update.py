import time
import subprocess
import webbrowser
from datetime import datetime

def live_update():
    """Update data and optionally refresh browser"""
    print("🔄 Starting live update mode with REAL congressional data...")
    print("📊 Dashboard available at: http://localhost:8000")
    print("⏰ Updates every 30 seconds (press Ctrl+C to stop)")
    
    # Open browser if not already open
    try:
        webbrowser.open('http://localhost:8000')
    except:
        print("🌐 Please manually open: http://localhost:8000")
    
    try:
        while True:
            print(f"\n🕐 {datetime.now().strftime('%H:%M:%S')} - Fetching real congressional data...")
            
            # Use real congressional data instead of test data
            subprocess.run(['python', 'main_fast.py'], capture_output=True)
            
            print("✅ Real congressional data updated! Refresh your browser to see changes.")
            print("💡 Tip: Use Cmd+R (Mac) or Ctrl+R (Windows) to refresh")
            
            # Wait 30 seconds before next update
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n🛑 Live update stopped.")

if __name__ == "__main__":
    live_update() 