from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def handle_sum():
    '''
    recieves payload
    {
        'num1': int,
        'num2': int
    }
    '''

    data = request.get_json()
    return jsonify({'result': data['num1'] + data['num2']})




if __name__ == '__main__':
    app.run(debug=True)

