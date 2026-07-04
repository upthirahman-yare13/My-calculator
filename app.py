import os
import logging
from flask import Flask, request, jsonify, render_template
from firebase_admin import credentials, firestore, initialize_app
from calculator import Calculator

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
calc = Calculator() # Halkan ayaan ka soo dhex wacnay class-ka calculator

# Firebase Setup
def get_firebase_credentials():
    return {
        "type": "service_account",
        "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
        "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.environ.get("FIREBASE_PRIVATE_KEY", "").replace('\\n', '\n'),
        "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL")
    }

try:
    cred = credentials.Certificate(get_firebase_credentials())
    initialize_app(cred)
    db = firestore.client()
    logger.info("Firebase initialization successful.")
except Exception as e:
    logger.error(f"Firebase initialization failed: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        n1, n2 = float(data['num1']), float(data['num2'])
        op = data['operation']
        
        # Isticmaalka Calculator class
        if op == '+': res = calc.add(n1, n2)
        elif op == '-': res = calc.subtract(n1, n2)
        elif op == '*': res = calc.multiply(n1, n2)
        elif op == '/': res = calc.divide(n1, n2)
        else: return jsonify({'error': 'Operation invalid'}), 400
        
        # Kaydinta Firestore
        db.collection('history').add({
            'n1': n1, 'n2': n2, 'op': op, 'res': res, 
            'timestamp': firestore.SERVER_TIMESTAMP
        })
        
        return jsonify({'result': res})
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)
