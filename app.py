from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Portfolio</h1><p>This is my first real Flask project.</p>"

@app.route('/bio')
def bio():
    return """
    <h1>About Me</h1>
    <p><strong>Name:</strong> Mohammed Ubaid</p>
    <p><strong>Skills:</strong> Python, Flask, SQL, Git</p>
    <p><strong>Introduction:</strong> I am an aspiring software engineer, currently building my project.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
