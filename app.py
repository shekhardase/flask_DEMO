# app.py
# This is your main backend file.

from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# --- Backend API Endpoint ---
# This is a simple API that the frontend can call.


@app.route('/api/message')
def get_message():
    """
    This function runs when a request is made to /api/message.
    It returns a JSON object.
    """
    # In a real app, you might get this data from a database.
    message_data = {
        "sender": "Backend",
        "text": "Hello from the Flask backend!"
    }
    return jsonify(message_data)


# --- Frontend Route ---
# This serves the main HTML page.
@app.route('/')
def index():
    """
    This function runs when a user visits the main URL.
    It renders and returns the index.html file.
    """
    # Flask will look for this file in a 'templates' folder.
    return render_template('index.html')


# --- Main execution block ---
if __name__ == '__main__':
    # The host='0.0.0.0' makes the app accessible from outside the container.
    # The default port is 5000.
    app.run(host='0.0.0.0', port=5000, debug=True)
