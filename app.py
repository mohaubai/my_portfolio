from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bio')
def bio():
    user_info = {
        "name": "John Doe",
        "skills" : "Python, Flask, SQL, Git",
        "intro": "I am an aspiring software engineer, currently building my project."
    }
    return render_template('bio.html', **user_info)


if __name__ == '__main__':
    app.run(debug=True)
