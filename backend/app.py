from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Mengambil data dari Environment Variable (Khas DevOps: Jangan hardcode konfigurasi!)
APP_ENV = os.getenv("APP_ENV", "Development")

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": f"Backend API berjalan di lingkungan: {APP_ENV}"
    })

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    pilihan = data.get('pilihan') if data else None
    if not pilihan:
        return jsonify({"status": "error", "message": "Pilihan vote tidak boleh kosong"}), 400
    
    return jsonify({
        "status": "success",
        "message": f"Vote untuk '{pilihan}' berhasil diterima!"
    })

if __name__ == '__main__':
    # Berjalan di port 5000 dan mendengarkan semua koneksi (0.0.0.0) agar bisa diakses dari luar kontainer
    app.run(host='0.0.0.0', port=5000)