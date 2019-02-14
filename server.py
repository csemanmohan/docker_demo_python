from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def reply():
    """
    method for getting file downloaded from s3
    :return: reply
    """
    res = "Hello World"
    return res


app.run(debug=True, host='0.0.0.0', port=5858)
