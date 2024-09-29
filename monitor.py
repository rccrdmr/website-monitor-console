# monitor.py

import requests
import time
import threading
from colorama import Fore, Style, init

init()

def check_website(website, interval):
    headers = {}
    
    while True:
        try:
            response = requests.get(website, headers=headers)
            response_time = round(response.elapsed.total_seconds() * 1000)
            
            if response.status_code == 200:
                print(Fore.GREEN + f"Website {website} is UP. Response time: {response_time} ms." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + f"Website {website} is DOWN. Status Code: {response.status_code}" + Style.RESET_ALL)
        
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Website {website} is DOWN. Error: {e}" + Style.RESET_ALL)
        
        time.sleep(interval)

def start_monitoring(website_data):
    for website, interval in website_data.items():
        thread = threading.Thread(target=check_website, args=(website, interval), daemon=True)
        thread.start()