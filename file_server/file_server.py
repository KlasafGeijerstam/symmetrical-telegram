from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'data' in request.files:
        f = request.files['data']
        data = f.read()
        print('Received', len(data), 'bytes of data')
    else:
        print('No file submitted')

    return 'Ok!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
