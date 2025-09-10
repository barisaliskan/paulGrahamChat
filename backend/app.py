from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
from paul_graham import PaulGrahamAgent

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize Paul Graham Agent
pg_agent = PaulGrahamAgent()

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "success",
        "message": "Paul Graham Agent Backend is running!",
        "version": "1.0.0"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        
        # Validate request
        if not data or 'message' not in data:
            return jsonify({
                "status": "error",
                "message": "Message is required"
            }), 400
        
        user_message = data['message']
        api_key = data.get('api_key')
        
        if not api_key:
            return jsonify({
                "status": "error",
                "message": "OpenAI API key is required"
            }), 400
        
        # Get conversation history
        conversation_history = data.get('history', [])
        
        # Generate response using Paul Graham Agent
        response = pg_agent.generate_response(
            user_message=user_message,
            api_key=api_key,
            conversation_history=conversation_history
        )
        
        return jsonify({
            "status": "success",
            "response": response,
            "timestamp": pg_agent.get_timestamp()
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error generating response: {str(e)}"
        }), 500

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    """Clear conversation history"""
    return jsonify({
        "status": "success",
        "message": "Conversation cleared"
    })

@app.route('/api/info', methods=['GET'])
def get_agent_info():
    """Get information about Paul Graham"""
    return jsonify({
        "status": "success",
        "info": {
            "name": "Paul Graham",
            "role": "Co-founder of Y Combinator",
            "expertise": [
                "Startups and entrepreneurship",
                "Programming (Lisp, Python)",
                "Writing and essays",
                "Venture capital",
                "Technology trends"
            ],
            "famous_essays": [
                "How to Start a Startup",
                "Do Things that Don't Scale", 
                "Maker's Schedule, Manager's Schedule",
                "The Python Paradox"
            ]
        }
    })

if __name__ == '__main__':
    print(" Paul Graham Agent Backend Starting...")
    print(" Backend running on: http://localhost:5000")
    print(" API Endpoints:")
    print("   GET  /                  - Health check")
    print("   POST /api/chat          - Chat with Paul Graham")
    print("   POST /api/clear         - Clear conversation")
    print("   GET  /api/info          - Agent information")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
