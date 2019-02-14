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


app.run(debug=True, port=5858)
