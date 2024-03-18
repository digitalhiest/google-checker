import argparse
import requests
from colorama import init, Fore

def display_logo():
    print(Fore.GREEN + "Google API Client Checker")

def display_usage():
    usage = """
    Usage:
    python script_name.py client_id client_secret
    """
    print(Fore.RED + usage)

def check_google_client(client_id, client_secret):
    try:
        # Verify Google Client ID and Secret by making a request
        url = "https://oauth2.googleapis.com/tokeninfo"
        params = {"client_id": client_id, "client_secret": client_secret}
        response = requests.post(url, data=params)
        if response.status_code == 200:
            print(Fore.GREEN + "[+] Google Client ID and Secret are valid.")
        else:
            print(Fore.RED + "[-] Failed to verify Google Client ID and Secret.")
    except Exception as e:
        print(Fore.RED + f"[-] An error occurred: {e}")

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama
    display_logo()

    parser = argparse.ArgumentParser(description="Google API Client Checker")
    parser.add_argument("client_id", help="Google Client ID")
    parser.add_argument("client_secret", help="Google Client Secret")
    args = parser.parse_args()

    if args.client_id and args.client_secret:
        check_google_client(args.client_id, args.client_secret)
    else:
        display_usage()
