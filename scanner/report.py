import json

def generate_report(scan_results, target):
    report = {
        "target": target,
        "vulnerabilities": scan_results
    }

    # Menyimpan laporan ke file JSON
    report_file = f"{target.replace('http://', '').replace('https://', '').replace('/', '_')}_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=4)

    print(f"Report saved to {report_file}")
