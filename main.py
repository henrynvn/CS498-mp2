from flask import Flask, request, jsonify

app = Flask(__name__)
seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():
    return str(seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    global seed_value
    data = request.get_json()
    if data and 'num' in data and isinstance(data['num'], int):
        seed_value = data['num']
        return '', 204
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
