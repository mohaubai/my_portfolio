from flask import Flask, render_template, request

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        user_name = request.form['name']
        user_message = request.form['message']

        return f'<h1>Thank You, {user_name}!</h1><p>Your Message: {user_message}</p>'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
