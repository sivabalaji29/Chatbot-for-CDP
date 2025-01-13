import logging
import os
import requests
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Headers to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# CDP Documentation URLs
cdp_docs = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def is_valid_url(url):
    """Validate if the provided URL is in the correct format."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def fetch_documentation():
    """Fetch documentation from the given URLs and save it as HTML files in the db folder."""
    
    # Create the 'db' folder if it doesn't exist
    if not os.path.exists('db'):
        os.makedirs('db')

    for cdp, url in cdp_docs.items():
        if not is_valid_url(url):
            logging.error(f"Invalid URL for {cdp}: {url}")
            continue

        try:
            logging.info(f"Fetching {cdp} documentation from {url}")
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            logging.info(f"Successfully fetched {cdp} documentation.")
            
            # Save the fetched content to an HTML file inside 'db' folder
            filename = os.path.join('db', f"{cdp}_documentation.html")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(response.text)
            logging.info(f"Saved {cdp} documentation to {filename}")
        
        except requests.exceptions.HTTPError as e:
            logging.error(f"Error processing {cdp}: {e}")
        except requests.exceptions.Timeout:
            logging.error(f"Timeout while fetching {cdp} documentation.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error processing {cdp}: {e}")

if __name__ == "__main__":
    fetch_documentation()
