from flask import Flask, request, jsonify
from scanner.scanner import scan_target  # Perubahan ini
from scanner.report import generate_report

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_website():
    url = request.json.get('url')
    
    # Memindai target menggunakan Nmap
    scan_results = scan_target(url)

    # Menghasilkan laporan dari hasil pemindaian
    generate_report(scan_results, url)

    return jsonify({'status': 'scan completed', 'results': scan_results}), 200

if __name__ == '__main__':
    app.run(debug=True)
