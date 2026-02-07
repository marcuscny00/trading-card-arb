import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import yaml
from pathlib import Path

headers = {
    "User-Agent" : (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome//120.0.0.0 Safari/537.36"
    )
}

# read sites.yaml for sites
def load_sites_config():
    config_path = Path(__file__).resolve().parents[1]/"config"/"sites.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
def fetch_html(url,headers,timeout = 10):

    try:
        response = requests.get(url, headers=headers, timeout = timeout )
        response.raise_for_status()
        return response.content
    
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}") 
    except Timeout:
        print(f"[TIMEOUT] {url}")
    except RequestException as req_err:
        print(f"Request error occurred: {req_err}")