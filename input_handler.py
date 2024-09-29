# input_handler.py

def gather_website_info():
    websites = {}

    while True:
        website = input("Enter a website URL (or type 'done' to finish): ").strip()

        if website.lower() == 'done':
            break
        
        if website == '':
            print("Please enter a valid website URL.")
            continue
        if not (website.startswith('http://') or website.startswith('https://')):
            print("Please enter a URL that starts with 'http://' or 'https://'.")
            continue

        while True:
            try:
                interval = int(input(f"Enter the check interval in seconds for {website}: ").strip())
                if interval <= 0:
                    print("Please enter a positive number for the interval.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number for the interval.")

        websites[website] = interval
    
    return websites