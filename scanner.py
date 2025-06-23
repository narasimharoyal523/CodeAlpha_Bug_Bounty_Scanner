import json
from utils import check_security_headers, test_sql_injection, test_xss_vulnerability

def scan_website(url):
    print(f"Scanning {url}...\n")
    report = {
        "url": url,
        "security_headers_missing": check_security_headers(url),
        "vulnerable_to_sql_injection": test_sql_injection(url),
        "vulnerable_to_xss": test_xss_vulnerability(url),
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Scan complete! Report saved as 'report.json'.")

if __name__ == "__main__":
    target = input("Enter target URL (e.g., https://example.com): ")
    scan_website(target)
