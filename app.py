from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL           
        )
""")
    
    conn.commit()
    conn.close()

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

        if not user_name or not user_message:
            return "Error: Both Name and message are required"
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (user_name, user_message))
        conn.commit()
        conn.close()

        return f"<h1>Thank You, {user_name}!</h1><p>Your Message has been saved.</p>"
    
    return render_template('contact.html')

@app.route('/messages')
def show_messages():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, message FROM messages")
    all_messages = cursor.fetchall()
    conn.close()

    return render_template('messages.html', messages=all_messages)

create_database()
if __name__ == '__main__':
    app.run(debug=True)
