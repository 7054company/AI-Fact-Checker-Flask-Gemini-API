from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = 'AIzaSyBK_GYb6nfjIZ8OlHT4xgguA5NeCSLqGmU'

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({'error': 'Missing query'}), 400

    prompt = f"""
You are an AI fact checker. Given a statement from a user, search your latest knowledge and verify whether it is true, false, or unverified.
Explain briefly why. The user asked:
\"{query}\"
"""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        reply = (
            data.get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "No answer found.")
        )

        return jsonify({'result': reply})

    except requests.exceptions.RequestException as e:
        print('Gemini API error:', e)
        return jsonify({
            'error': 'Error from Gemini API',
            'detail': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)