import requests
import argparse
from datetime import datetime

def check_headers(url):
    findings = []

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print(f"\n[+] Scanning {url}\n")

        security_headers = {
            "Content-Security-Policy": "Prevents XSS attacks",
            "X-Frame-Options": "Prevents clickjacking",
            "X-XSS-Protection": "Basic XSS protection",
            "Strict-Transport-Security": "Forces HTTPS usage"
        }

        for header, risk in security_headers.items():
            if header in headers:
                result = f"[OK] {header} is present"
                print(result)
                findings.append(result)
            else:
                result = f"[HIGH] Missing {header} → Risk: {risk}"
                print(result)
                findings.append(result)

        # Extra checks
        if not url.startswith("https"):
            msg = "[MEDIUM] Site is not using HTTPS"
            print(msg)
            findings.append(msg)

        server = headers.get("Server")
        if server:
            msg = f"[LOW] Server header exposed: {server}"
            print(msg)
            findings.append(msg)

        status = f"[INFO] Status Code: {response.status_code}"
        print(status)
        findings.append(status)

        return findings

    except Exception as e:
        error_msg = f"[ERROR] {e}"
        print(error_msg)
        return [error_msg]


def save_report(url, findings):
    filename = f"report_{url.replace('https://','').replace('http://','').replace('/','_')}.txt"

    with open(filename, "w") as f:
        f.write("Web Security Scan Report\n")
        f.write(f"Target: {url}\n")
        f.write(f"Date: {datetime.now()}\n\n")

        for item in findings:
            f.write(item + "\n")

    print(f"\n[+] Report saved as {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Web Security Scanner")
    parser.add_argument("url", help="Target URL (e.g. https://example.com)")
    args = parser.parse_args()

    results = check_headers(args.url)
    save_report(args.url, results)
