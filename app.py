from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route to render the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle chat messages
@app.route('/api/chat', methods=['POST'])
def handle_chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({"error": "No message provided"}), 400

        response = "I'm sorry, I didn't understand that."

        if "hello" in message.lower():
            response = "Hello! How can I assist you today?"
        elif "capital" in message.lower() and "canada" in message.lower():
            response = "The capital of Canada is Ottawa."
        elif "space" in message.lower():
            response = "Did you know that space is completely silent? There is no atmosphere in space, so sound has no medium to travel through."
        elif "president" in message.lower() and "united states" in message.lower():
            response = "The current President of the United States is Joe Biden."

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
