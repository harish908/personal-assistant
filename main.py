from gemini_llm import GeminiLLM
from service import LLMService
from database import PostgresDB
from flask import Flask, request, jsonify
from urllib.parse import quote, unquote

gemini_llm = GeminiLLM()
db = PostgresDB()
llmService = LLMService(gemini_llm, db)
app = Flask(__name__)

def main():
    db.DBConnect()
    gemini_llm.Connect()

@app.route('/api/transformText', methods=['POST'])
def transformText():
    try:
        data = request.get_json()
        if 'data' in data:
            received_message = data['data']
            llmService.TransformText(received_message)
            response_data = {'status': 'success'}
            return jsonify(response_data)

        else:
            response_data = {'status': 'error', 'errorMessage': 'Missing "data" in the request JSON'}
            return jsonify(response_data), 400

    except Exception as ex:
        response_data = {'status': 'error', 'errorMessage': str(ex)}
        return jsonify(response_data), 500

@app.route('/api/prompt', methods=['GET'])
def prompt():
    try:
        encoded_data = request.args.get('data', '')
        decoded_data = unquote(encoded_data)
        llmResp = llmService.Prompt(decoded_data)
        result = {'status': 'success', 'response': llmResp}
        return jsonify(result)

    except Exception as ex:
        return jsonify({'status': 'error', 'errorMessage': str(ex)}), 500 

if __name__ == '__main__': 
    main()
    app.run(debug=True)