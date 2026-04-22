import requests

def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print("\n[+] Security Headers Check:\n")

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security"
        ]

        for header in security_headers:
            if header in headers:
                print(f"[✔] {header} is present")
            else:
                print(f"[✘] {header} is missing")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Enter a URL (e.g. https://example.com): ")
    check_headers(target)
