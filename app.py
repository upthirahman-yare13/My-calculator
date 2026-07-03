from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# Firebase Integration (Isticmaalka Environment Variables)
# Xogtaan waxaad ku dari doontaa Vercel Environment Variables
cred = credentials.Certificate({
    "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
    "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
})
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def api_calculate():
    data = request.json
    n1, n2, op = float(data['num1']), float(data['num2']), data['operation']
    
    # Xisaabinta
    res = 0
    if op == '+': res = n1 + n2
    elif op == '-': res = n1 - n2
    elif op == '*': res = n1 * n2
    elif op == '/': res = n1 / n2 if n2 != 0 else 0
    
    # Ku kaydi Firestore
    db.collection('calculations').add({
        'num1': n1,
        'num2': n2,
        'operation': op,
        'result': res
    })
    
    return jsonify({"result": res})

if __name__ == '__main__':
    app.run(debug=True)
