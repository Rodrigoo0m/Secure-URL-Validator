import requests
import urllib.parse

def is_url_safe(url):
    try:
        # Parse a URL to extract the domain for reputation check
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # URLVoid API (you can use other services as well)
        urlvoid_api_key = 'YOUR_API_KEY_HERE'
        urlvoid_url = f"https://api.urlvoid.com/api1000/{urlvoid_api_key}/host/{domain}/"
        
        # Make request to URLVoid API
        response = requests.get(urlvoid_url)
        
        # Check response from URLVoid API
        if response.status_code == 200:
            result = response.json()
            if result.get('detections'):
                return False, result['detections']
            else:
                return True, "URL is safe"
        else:
            return False, f"Error checking URL: {response.status_code}"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    url_to_check = "https://example.com"
    safe, message = is_url_safe(url_to_check)
    if safe:
        print(f"The URL '{url_to_check}' is safe.")
    else:
        print(f"The URL '{url_to_check}' is potentially unsafe. Reasons: {message}")
