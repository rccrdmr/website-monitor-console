# main.py

from input_handler import gather_website_info
from monitor import start_monitoring
import time

def main():
    website_data = gather_website_info()

    print("\nStarting website monitoring... Press Ctrl+C to stop.")
    start_monitoring(website_data)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()