import os
import logging
from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore

# Habeynta Logging-ka
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Firebase configuration oo la xoojiyey
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
    firebase_admin.initialize_app(cred)
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
        
        # Hubinta xogta (Validation)
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
        
        n1 = float(data['num1'])
        n2 = float(data['num2'])
        op = data['operation']
        
        # Xisaabinta
        operations = {
            '+': n1 + n2,
            '-': n1 - n2,
            '*': n1 * n2,
            '/': n1 / n2 if n2 != 0 else "Error: Div by Zero"
        }
        
        res = operations.get(op, "Invalid operation")
        
        # Kaydinta Firestore (Optional: Waxaan ku darnay try-except si ayan u carqaladayn xisaabta)
        try:
            db.collection('history').add({
                'num1': n1,
                'num2': n2,
                'operation': op,
                'result': res,
                'timestamp': firestore.SERVER_TIMESTAMP
            })
        except Exception as db_err:
            logger.warning(f"Database save failed: {db_err}")
            
        return jsonify({'result': res})

    except ValueError:
        return jsonify({'error': 'Please enter valid numbers'}), 400
    except Exception as e:
        logger.error(f"Calculation error: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=False) # debug=False ayaan u badalay, waa mid ka amaan badan Production
