
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__, template_folder= "templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite.///friends.db'
# Initilize the  database
db= SQLAlchemy(app)

# Create Database Model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    data = db.Column(db.DateTime, default= datetime.utcnow)

    # Create a function to return string when we add something
    def __repr__(self):
        return '<Name %r>' % self.id

subscribers = []

@app.route('/')
def index():
    title = "Minbayev Bolatbek's Blog"
    return render_template("index.html", title=title), url_for('index')

@app.route('/about')
def about():
    title = "About Bolatbek Minbayev!"
    return render_template("about.html", title = title), url_for('about')

@app.route('/subscribe')
def subscribe():
    title = "Subscribe to my Blog"
    return render_template("subscribe.html", title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name= request.form.get("first_name")
    last_name= request.form.get("last_name")
    email = request.form.get("email")

    conditions = [first_name, last_name, email]
    if any(conditions) and not all(conditions) :
        error_statement = "All Form Fields Required..."
        return render_template('subscribe.html', error_statement= error_statement,
        first_name =first_name, last_name=last_name, email=email)

    subscribers.append(f"{first_name} {last_name} | {email}")
    title = "Thank you!"
    return render_template("form.html", title=title, subscribers=subscribers)

if __name__ == "__main__":
    app.run(debug=True)
