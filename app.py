import os
import json
from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# --- Firebase Configuration ---
# Waxaan xogta ka soo qaadaynaa Environment Variables (Vercel)
# Si looga fogaado in JSON-ka si toos ah loo geliyo koodka
firebase_config = {
    "type": "service_account",
    "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
    "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL")
}

# Bilowga Firebase
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def api_calculate():
    data = request.json
    try:
        n1 = float(data['num1'])
        n2 = float(data['num2'])
        op = data['operation']
        
        # Xisaabinta
        if op == '+': res = n1 + n2
        elif op == '-': res = n1 - n2
        elif op == '*': res = n1 * n2
        elif op == '/': res = n1 / n2 if n2 != 0 else 0
        else: res = 0
        
        # Ku kaydinta Firestore
        db.collection('calculations').add({
            'num1': n1,
            'num2': n2,
            'operation': op,
            'result': res
        })
        
        return jsonify({"result": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
