from endpoints import data
from flask import Flask, jsonify, request, make_response
from time import ctime

today = ctime()
app = Flask(__name__)
info = data()

@app.route('/api/v1/get', methods=['GET'])
def getter():
    get = info.get_all()
    return jsonify({'Orders': get})

@app.route('/api/v1/post', methods=['POST'])
def poster():
    info.poster()
    return jsonify({'Msg':'Order Created'})

@app.route('/api/v1/update/<int:id>', methods=['PUT'])
def make_update(id):
    info.update()
    return jsonify({'msg':'Successfully Updated'})

if __name__=='__main__':
    app.run(debug=True)