import requests

def check_headers(url):
    """Check for missing security headers."""
    response = requests.get(url)
    headers = [
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'X-Content-Type-Options',
        'X-Frame-Options',
        'X-XSS-Protection',
    ]
    missing_headers = [header for header in headers if header not in response.headers]
    return missing_headers

def check_ssl_tls(url):
    """Check SSL/TLS configuration."""
    try:
        response = requests.get(url, verify=True)
        return "SSL/TLS seems to be properly configured."
    except requests.exceptions.SSLError as e:
        return f"SSL/TLS error: {str(e)}"

def check_common_paths(base_url, paths):
    """Check for exposed common paths."""
    exposed_paths = []
    for path in paths:
        response = requests.get(base_url + path)
        if response.status_code == 200:
            exposed_paths.append(path)
    return exposed_paths

def check_rate_limiting(url, threshold=100):
    """Check for rate limiting."""
    for _ in range(threshold):
        response = requests.get(url)
        if response.status_code == 429:
            return True
    return False

def main():
    base_url = input("Enter the URL you want to check: ")

    # Check for missing security headers
    missing = check_headers(base_url)
    if missing:
        print("Missing headers:", missing)
    else:
        print("All security headers are present.")

    # Check SSL/TLS configuration
    result = check_ssl_tls(base_url)
    print(result)

    # Check for exposed common paths
    common_paths = [
        "/.git",
        "/config.php",
        "/db.php",
        "/backup.zip",
        "/backup.sql",
        "/.htaccess",
        "/phpinfo.php",
        "/admin",
        "/phpmyadmin"
    ]
    exposed = check_common_paths(base_url, common_paths)
    if exposed:
        print("Exposed paths:", exposed)
    else:
        print("No common sensitive paths found.")

    # Check for rate limiting
    is_rate_limited = check_rate_limiting(base_url + "/api/some_endpoint")
    print("Rate limiting in place:", is_rate_limited)

if __name__ == "__main__":
    main()
