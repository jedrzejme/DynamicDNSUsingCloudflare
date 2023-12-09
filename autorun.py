# Import libraries
import schedule
import time
from configparser import ConfigParser
config = ConfigParser()

# Read config.ini
config.read('config.ini')

interval = int(config.getint('main', 'interval'))
time_unit = config.get('main', 'time_unit')

def ddns():
        # Import libraries
    import requests
    import json
    from configparser import ConfigParser
    config = ConfigParser()

    # Read config.ini
    config.read('config.ini')

    api_token = config.get('main', 'api_token')
    zone_identifier = config.get('main', 'zone_identifier')
    domain = config.get('main', 'domain')
    name = config.get('main', 'name')
    ttl = config.getint('main', 'ttl')
    proxied = config.getboolean('main', 'proxied')

    # Checks if DNS record exists or not
    def check_dns_record():
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

        url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                dns_records = response.json().get('result', [])
                for record in dns_records:
                    if record['name'] == f"{name}.{domain}":
                        return True
                return False
            else:
                print("Failed to retrieve DNS records. Status code:", response.status_code)
                return False
        except requests.RequestException as e:
            print("Error:", e)
            return False

    # Define getting the current IP address
    def get_public_ip():
        try:
            response = requests.get('https://api.ipify.org?format=json')
            if response.status_code == 200:
                data = response.json()
                return data['ip']
            else:
                print("Failed to retrieve IP address. Status code:", response.status_code)
        except requests.RequestException as e:
            print("Error:", e)

    # Creates new DNS record if it doesn't exist
    # Define the new record details
    new_record_data = {
        "type": "A",  # Change this according to the record type (A, CNAME, etc.)
        "name": f"{name}",  # Replace with your record name
        "content": f"{get_public_ip()}",  # Replace with the new IP address
        "ttl": f"{ttl}",  # TTL in seconds
        "proxied": bool(proxied)
    }

    # Construct the URL for the specific DNS record
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/"

    # Define headers with Cloudflare API token and content type
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # Send POST request to create new DNS record if DNS record doesn't exist
    if check_dns_record() == False:
        response = requests.post(url, headers=headers, json=new_record_data)

    # Check the response
    if check_dns_record() == False:
        if response.status_code == 200:
            print("DNS record updated successfully!")
        else:
            print("Failed to update DNS record with status code:", response.status_code)
            print("Error message:")
            print(response.text)
        
    # Gets the DNS record ID
    def get_dns_record_id():
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

        url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                dns_records = response.json().get('result', [])
                for record in dns_records:
                    if record['name'] == f"{name}.{domain}":
                        return record['id']
                print(f"The DNS record for {name} does not exist.")
                return None
            else:
                print("Failed to retrieve DNS records. Status code:", response.status_code)
                return None
        except requests.RequestException as e:
            print("Error:", e)
            return None

    dns_record_id = get_dns_record_id()

    # Edits an existing DNS record if it already exists
    # Define the new record details
    new_record_data = {
        "type": "A",  # Change this according to the record type (A, CNAME, etc.)
        "name": f"{name}",  # Replace with your record name
        "content": f"{get_public_ip()}",  # Replace with the new IP address
        "ttl": f"{ttl}",  # TTL in seconds
        "proxied": bool(proxied)
    }

    # Construct the URL for the specific DNS record
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/{dns_record_id}"

    # Define headers with Cloudflare API token and content type
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # Send PUT request to update the DNS record if it already exists
    if check_dns_record() == True:
        response = requests.put(url, headers=headers, json=new_record_data)

    # Check the response
    if check_dns_record() == True:
        if response.status_code == 200:
            print("DNS record updated successfully!")
        else:
            print("Failed to update DNS record with status code:", response.status_code)
            print("Error message:")
            print(response.text)


# Define running dynamic DNS every "time"
def schedule_job():
    if time_unit == 'seconds':
        schedule.every(interval).seconds.do(ddns)
    elif time_unit == 'minutes':
        schedule.every(interval).minutes.do(ddns)
    elif time_unit == 'hours':
        schedule.every(interval).hours.do(ddns)
    else:
        print("Invalid time unit provided.")

    while True:
        schedule.run_pending()
        time.sleep(1)

# Run dynamic DNS
schedule_job()