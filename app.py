from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name


if __name__ == '__main__':
    app.run(debug=True)
