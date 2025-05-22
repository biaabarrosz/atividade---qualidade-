from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200
 
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data}), 200
 
if __name__ == '__main__':
    app.run(debug=True)