# backend/app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Konfiguracja bazy danych PostgreSQL - ustaw user, pass, db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost:5432/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/messages', methods=['POST'])
def create_message():
    try:
        data = request.get_json()
        content = data.get('content', None)

        if content is not None:
            new_message = Message(content=content)
            db.session.add(new_message)
            db.session.commit()

            return jsonify({'message': 'Message added successfully'}), 201
        else:
            return jsonify({'error': 'Content cannot be empty'}), 400

    except Exception as e:
        app.logger.error(f'Error handling POST request: {str(e)}')
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    try:
        messages = Message.query.all()
        message_list = [{'id': message.id, 'content': message.content, 'created_at': message.created_at} for message in messages]
        return jsonify({'messages': message_list}), 200

    except Exception as e:
        app.logger.error(f'Error handling GET request: {str(e)}')
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
