from flask import Flask, jsonify
from fetch_data import fetch_data
from find_citations import find_citations

app = Flask(__name__)

@app.route('/citations', methods=['GET'])
def get_citations():
    data = fetch_data()
    citations = find_citations(data)
    return jsonify(citations)

if __name__ == "__main__":
    app.run(debug=True)
