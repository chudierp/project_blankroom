from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask running, working on React connection'

if __name__ == '__main__':
    app.run()