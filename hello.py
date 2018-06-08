from flask import *
app = Flask(__name__)

@app.route("/")
def hello():
    message = "yoooooooowwwwww"
    return render_template('index.html', message=message)

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory('images', path)

if __name__ == "__main__":
    app.run()
