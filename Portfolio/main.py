from flask import Flask, request, render_template
import mysql.connector


app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MySQL',
    'database': 'profile'
}

@app.route("/")
def loading():
    return render_template("index.html")

@app.route("/portfolio")
def home():
    return render_template("portfolio.html")

@app.route('/submit', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    subject = request.form.get('subject')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    try:
        query = "INSERT INTO hire_me (name, email, subject, message) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, subject, message))
        conn.commit()
        return render_template('portfolio.html', success="Message sent!")
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)