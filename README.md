
# Security Checker

A simple Python script to check for some common security vulnerabilities in web applications.

## Features

- Checks for missing security headers.
- Validates SSL/TLS configuration.
- Searches for exposed common paths that might be sensitive.
- Checks if rate limiting is applied on a specific endpoint.

## Requirements

- Python 3.9
- `requests` library

You can install the required libraries using the following command:

```
pip install requests
```

## Usage


1. Run the script:

   ```
   python app.py
   ```

2. Enter the base URL you want to check.

3. Wait for the script to run its checks and review the results.

## What It Checks

1. **Security Headers**: This checks for the following headers:
   - Strict-Transport-Security
   - Content-Security-Policy
   - X-Content-Type-Options
   - X-Frame-Options
   - X-XSS-Protection

2. **SSL/TLS Configuration**: Verifies the SSL/TLS configuration for the entered URL.

3. **Common Paths**: Looks for some potentially sensitive paths like:
   - /.git
   - /config.php
   - /db.php
   ... and others

4. **Rate Limiting**: Checks if rate limiting is applied to the endpoint `/api/some_endpoint`.

## Note

This is a basic security checker and does not guarantee finding all vulnerabilities. It is recommended to always use comprehensive security tools and practices to ensure the safety of your web applications.

