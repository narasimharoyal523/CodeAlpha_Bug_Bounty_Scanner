import requests
from bs4 import BeautifulSoup

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        missing_headers = []
        important_headers = [
            'Content-Security-Policy',
            'X-Frame-Options',
            'X-XSS-Protection',
            'Strict-Transport-Security',
            'Referrer-Policy'
        ]

        for header in important_headers:
            if header not in headers:
                missing_headers.append(header)

        return missing_headers
    except Exception as e:
        return ["Error checking headers: " + str(e)]

def test_xss_vulnerability(url):
    xss_payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url + "?q=" + xss_payload, timeout=5)
        if xss_payload in response.text:
            return True
    except:
        return False
    return False

def test_sql_injection(url):
    payload = "' OR '1'='1"
    try:
        response = requests.get(url + "?id=" + payload, timeout=5)
        error_signatures = ["you have an error in your sql", "sql syntax", "mysql_fetch", "ORA-"]
        for error in error_signatures:
            if error.lower() in response.text.lower():
                return True
    except:
        return False
    return False
