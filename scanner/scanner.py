import subprocess
import json

def run_nmap_scan(target):
    try:
        # Menjalankan perintah Nmap
        command = ['nmap', '-sV', '--script=vuln', target]
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Mengembalikan output Nmap
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error occurred: {e}"

def scan_target(url):
    print(f"Scanning {url} for vulnerabilities...")
    scan_results = run_nmap_scan(url)
    return scan_results
