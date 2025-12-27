
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from src.openai_generator import generate_openai_response, clear_session
from src.data.data import format_psychometric_data

load_dotenv()

app = Flask(__name__)

@app.route('/api_home', methods=['GET'])
def api_home():
    """Health check endpoint"""
    return jsonify({
        "status": "success",
        "status_code": 200,
        "message": "API is working"
    })


@app.route('/api/generate', methods=['POST'])
def api_generate():
    """Generate psychometric insights using OpenAI"""
    data = request.json

    if not data or 'test_id' not in data:
        return jsonify({'status': 'error', 'message': 'test_id is required'}), 400

    test_id = data['test_id']

    try:
        # Fetch psychometric test data
        dynamic_api_url = f"https://wasabigaming.vercel.app/api/v1/psychometric-test/{test_id}"
        api_response = requests.get(dynamic_api_url, timeout=10)
        api_response.raise_for_status()
        raw_test_data = api_response.json()

        # Format data for OpenAI
        formatted_data = format_psychometric_data(raw_test_data)
        session_id = test_id  # Use test_id as session

        # Generate concise psychometric insights
        response_text = generate_openai_response(
            user_message=formatted_data["text"],
            session_id=session_id
        )

        # Optionally clear session after response to avoid memory buildup
        clear_session(session_id)

        return jsonify({
            'status': 'success',
            'test_id': test_id,
            'result': response_text
        })

    except requests.exceptions.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': 'Failed to fetch test data',
            'details': str(e)
        }), 502

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
